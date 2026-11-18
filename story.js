/* Many Hands page motion.
   Two rules run through this file:
   1. Drawn things jump, UI glides. Hands and paper move in steps; cards and text ease (CSS).
   2. Scroll drives the story. Pinned sections read their own scroll progress (0 to 1)
      and set everything from it, so scrolling back up reverses everything.
   Visitors who ask for reduced motion get the static page: no pinning, final scene shown. */
(() => {
  const root = document.documentElement;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const seg = (p, a, b) => clamp((p - a) / (b - a));
  const steps = (t, n) => Math.round(t * n) / n;
  const out = t => 1 - Math.pow(1 - t, 3);
  const inq = t => t * t;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- reveal on scroll (UI glides) */
  const reveals = $$('.reveal');
  if (reduced || !('IntersectionObserver' in window)) {
    reveals.forEach(el => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -12% 0px' });
    reveals.forEach(el => io.observe(el));
  }

  /* ---------- floating pill */
  const pill = $('.pill');
  const hero = $('#top');
  const secs = $$('.pill .dots a').map(a => [a, document.getElementById(a.dataset.sec)]);
  function updatePill() {
    const y = scrollY, vh = innerHeight;
    pill.classList.toggle('show', y > hero.offsetHeight * 0.75);
    const mid = y + vh * 0.45;
    let active = null;
    for (const [a, s] of secs) if (s && s.offsetTop <= mid) active = a;
    secs.forEach(([a]) => a.classList.toggle('on', a === active));
  }

  if (reduced) { addEventListener('scroll', updatePill, { passive: true }); updatePill(); return; }
  root.classList.add('js-story');

  /* ---------- Maria's counter */
  const story = $('#story');
  const stage = $('.stage', story);
  const beats = $$('.beat', story);
  const dots = $$('.progress-dots span', story);
  // Beat windows as fractions of the story's scroll travel.
  const W = [[0, .16], [.16, .38], [.38, .60], [.60, .82], [.82, 1.01]];
  // Each hand: its angle, and the point on the pile it grabs (stage units, 800 x 600).
  const HANDS = {
    mail:    { beat: 1, deg: 0,   grab: [222, 300] },
    folders: { beat: 2, deg: 90,  grab: [390, 312] },
    drafts:  { beat: 3, deg: 110, grab: [500, 270] },
  };
  for (const k in HANDS) {
    const h = HANDS[k], r = h.deg * Math.PI / 180, dir = [Math.cos(r), Math.sin(r)];
    h.el = $(`.hand[data-hand="${k}"]`, story);
    h.pile = $(`.pile[data-pile="${k}"]`, story);
    h.home = h.pile.dataset.home.split(',').map(Number);
    h.target = [h.grab[0] - 34 * dir[0], h.grab[1] - 34 * dir[1]];     // wrist, so the palm sits on the pile
    h.start = [h.target[0] - 620 * dir[0], h.target[1] - 620 * dir[1]]; // well off stage, along the arm
  }
  const at = (el, x, y) => el.setAttribute('transform', `translate(${x.toFixed(1)},${y.toFixed(1)})`);
  const lerp = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t];

  function drawStory(p) {
    for (const k in HANDS) {
      const h = HANDS[k], [a, b] = W[h.beat], t = seg(p, a, b);
      let pos, carry = false;
      if (t < .42) pos = lerp(h.start, h.target, out(steps(t / .42, 9)));
      else if (t < .56) { pos = h.target; carry = t >= .5; }
      else { pos = lerp(h.target, h.start, inq(steps((t - .56) / .44, 9))); carry = true; }
      at(h.el, pos[0], pos[1]);
      if (carry) at(h.pile, h.home[0] + pos[0] - h.target[0], h.home[1] + pos[1] - h.target[1]);
      else at(h.pile, h.home[0], h.home[1]);
    }
    stage.dataset.mood = p < W[2][0] ? 'stressed' : p < W[4][0] ? 'neutral' : 'happy';
    const i = W.findIndex(([a, b]) => p >= a && p < b);
    beats.forEach((el, j) => el.classList.toggle('on', j === i));
    dots.forEach((el, j) => el.classList.toggle('on', j <= i));
  }

  /* ---------- How it works */
  const how = $('#how');
  const howStick = $('.how-stick', how);
  const bars = $$('.week .bar i', how);
  const stepEls = $$('.steps li', how);
  // Pin How it works only when the whole section fits on screen; otherwise it scrolls normally.
  // On phones, crop Maria's scene tighter so she reads larger beside the text.
  const stageSvg = $('.stage-svg', story);
  function fitStage() { stageSvg.setAttribute('viewBox', innerWidth <= 860 ? '190 112 530 424' : '120 60 640 480'); }
  // How it works always pins. If the three steps don't fit side by side, it shows one step
  // at a time (compact), and drops the drawings too if the screen is very short (tight).
  const stepsEl = $('.steps', how);
  const natural = () => { howStick.style.height = 'auto'; const h = howStick.offsetHeight; howStick.style.height = ''; return h; };
  function setStepsHeight() {
    stepsEl.style.height = '';
    if (!how.classList.contains('how-compact')) return;
    stepsEl.style.height = Math.max(...stepEls.map(li => li.offsetHeight)) + 'px';
  }
  function fitHow() {
    fitStage();
    how.classList.remove('how-compact', 'how-tight');
    how.classList.add('how-pinned');
    setStepsHeight();
    const room = innerHeight;
    if (innerWidth > 860 && natural() <= room) return;
    how.classList.add('how-compact'); setStepsHeight();
    if (natural() <= room) return;
    how.classList.add('how-tight'); setStepsHeight();
  }
  function drawHow(q) {
    if (!how.classList.contains('how-pinned')) q = 1;
    bars.forEach((el, k) => el.style.setProperty('--f', clamp(q * 4.4 - k).toFixed(3)));
    const cur = q < .34 ? 0 : q < .7 ? 1 : 2;
    stepEls.forEach((el, k) => { el.classList.toggle('on', k <= cur); el.classList.toggle('cur', k === cur); });
  }

  const progress = el => {
    const r = el.getBoundingClientRect(), travel = el.offsetHeight - innerHeight;
    return travel > 0 ? clamp(-r.top / travel) : 1;
  };
  let ticking = false;
  function frame() {
    ticking = false;
    drawStory(progress(story));
    drawHow(progress(how));
    updatePill();
  }
  const ask = () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
  addEventListener('scroll', ask, { passive: true });
  addEventListener('resize', () => { fitHow(); ask(); });
  addEventListener('load', () => { fitHow(); ask(); });
  if (document.fonts) document.fonts.ready.then(() => { fitHow(); ask(); });
  fitHow();
  frame();
})();
