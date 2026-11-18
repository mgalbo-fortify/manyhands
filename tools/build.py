#!/usr/bin/env python3
"""Builds index.html for the Many Hands site.

Run from the repo root:  python3 tools/build.py
index.html is generated. Edit this file, then rebuild.

Two motion rules, borrowed from the best sites we studied:
1. Drawn things jump, UI glides. Illustrations move in steps and their lines "boil";
   cards, text and buttons ease.
2. Scroll drives the story. Pinned sections read their own scroll progress (0 to 1),
   so scrolling back up reverses everything. See story.js.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INK = "#1E2A24"
LINE = "#26332D"
GREEN = "#2C5A47"
DEEP = "#22463A"
BG = "#FAF7F2"
WHITE = "#FFFFFF"
SAND = "#EFE4D2"
SAGE = "#D5E2D1"
SKY = "#D3E2EA"
PEACH = "#F3D9C8"
BUTTER = "#F3D18A"
MUSTARD = "#E3B04B"
MUTED = "#55635B"
RULE = "#E6DFD3"
SKIN = ["#F1C7A0", "#C68A62", "#8D5A3B", "#E9B48A"]


def L(w=2.0):
    return f'fill="none" stroke="{LINE}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'


S = f'stroke="{LINE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'

# ---------------------------------------------------------------- shared SVG defs
DEFS = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="2.6" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="b1" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="b2" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
<filter id="b3" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="2" seed="13"/><feDisplacementMap in="SourceGraphic" scale="3" xChannelSelector="R" yChannelSelector="G"/></filter>
</defs></svg>'''


# ---------------------------------------------------------------- people
def face(mood):
    eyes = f'<circle cx="-9" cy="-2" r="2.4" fill="{LINE}"/><circle cx="9" cy="-2" r="2.4" fill="{LINE}"/>'
    if mood == "stressed":
        return (eyes + f'<path d="M-15 -11 L-5 -8 M15 -11 L5 -8" {L(1.8)}/>'
                f'<path d="M-6 12 Q-3 9 0 12 Q3 15 6 12" {L(1.8)}/>'
                f'<path d="M22 -16 Q26 -10 22 -6 Q18 -10 22 -16 Z" fill="{SKY}" {S} stroke-width="1.5"/>')
    if mood == "happy":
        return (f'<path d="M-12 -2 Q-9 -6 -6 -2 M6 -2 Q9 -6 12 -2" {L(1.8)}/>'
                f'<path d="M-9 8 Q0 17 9 8" {L(1.9)}/><circle cx="-15" cy="6" r="4" fill="{PEACH}"/><circle cx="15" cy="6" r="4" fill="{PEACH}"/>')
    return eyes + f'<path d="M-6 10 Q0 14 6 10" {L(1.8)}/>'


def maria(mood):
    """Maria behind her counter: waist up. Counter top is y=0, she's centred on x=0."""
    skin = SKIN[0]
    out = [f'<g class="mood mood-{mood}">']
    # torso, apron
    out.append(f'<path d="M-46 0 L-40 -96 Q0 -112 40 -96 L46 0 Z" fill="{BUTTER}" {S}/>')
    out.append(f'<path d="M-26 0 L-24 -70 L24 -70 L26 0 Z" fill="{SAGE}" {S}/><path d="M-24 -70 L-30 -98 M24 -70 L30 -98" {L(1.8)}/>')
    out.append(f'<rect x="-12" y="-46" width="24" height="16" rx="3" fill="none" {S} stroke-width="1.6"/>')
    # arms
    if mood == "stressed":
        out.append(f'<path d="M34 -94 Q60 -70 46 -132" {L(2.2)}/><g transform="translate(40,-140)"><rect x="-6" y="-18" width="14" height="26" rx="4" fill="{WHITE}" {S}/><circle cx="2" cy="4" r="9" fill="{skin}" {S}/></g>')
        out.append(f'<path d="M-34 -94 Q-64 -50 -70 -6" {L(2.2)}/><circle cx="-70" cy="-6" r="9" fill="{skin}" {S}/>')
        out.append(f'<g class="ring"><path d="M60 -168 Q68 -160 62 -150 M68 -176 Q80 -160 70 -144" {L(1.8)}/></g>')
    elif mood == "happy":
        out.append(f'<path d="M34 -94 Q72 -70 96 -86" {L(2.2)}/><g transform="translate(100,-88) rotate(-20)"><path d="M-8 -8 Q2 -14 10 -8 Q14 0 8 8 Q-2 12 -8 6 Z" fill="{skin}" {S}/><path d="M6 -10 L14 -18 M10 -4 L20 -10" {L(1.6)}/></g>')
        out.append(f'<path d="M-34 -94 Q-40 -40 -10 -8" {L(2.2)}/><circle cx="-8" cy="-6" r="9" fill="{skin}" {S}/>')
    else:
        out.append(f'<path d="M34 -94 Q58 -50 50 -8" {L(2.2)}/><circle cx="50" cy="-6" r="9" fill="{skin}" {S}/>')
        out.append(f'<path d="M-34 -94 Q-58 -50 -50 -8" {L(2.2)}/><circle cx="-50" cy="-6" r="9" fill="{skin}" {S}/>')
    # neck, head, hair
    out.append(f'<path d="M-7 -104 L-7 -114 M7 -104 L7 -114" {L(2)}/>')
    out.append(f'<g transform="translate(0,-142)"><circle cx="0" cy="0" r="30" fill="{skin}" {S}/>'
               f'<path d="M-30 -2 Q-32 -34 0 -34 Q30 -34 30 -4 Q22 -22 0 -22 Q-20 -22 -30 -2 Z" fill="#5B3A2A" {S}/>'
               f'<circle cx="12" cy="-38" r="12" fill="#5B3A2A" {S}/>{face(mood)}</g>')
    out.append("</g>")
    return "".join(out)


def customer(happy):
    skin = SKIN[2]
    f = face("happy" if happy else "neutral")
    cls = "cust-happy" if happy else "cust-wait"
    return (f'<g class="{cls}"><path d="M-8 -84 L-12 0 M8 -84 L12 0" {L(2.4)}/><path d="M-18 0 H-6 M6 0 H18" {L(2.4)}/>'
            f'<path d="M-30 -84 L-24 -170 Q0 -182 24 -170 L30 -84 Z" fill="{PEACH}" {S}/>'
            f'<path d="M-24 -162 Q-44 -120 -40 -96" {L(2.2)}/><circle cx="-40" cy="-92" r="8" fill="{skin}" {S}/>'
            f'<path d="M24 -162 Q34 -130 26 -110" {L(2.2)}/>'
            f'<g transform="translate(26,-102)"><rect x="-10" y="-4" width="26" height="22" rx="3" fill="{SKY}" {S}/><path d="M-4 -4 Q3 -14 10 -4" {L(1.8)}/></g>'
            f'<g transform="translate(0,-204) scale(0.85)"><circle cx="0" cy="0" r="28" fill="{skin}" {S}/>'
            f'<path d="M-28 -4 Q-26 -32 0 -32 Q26 -32 28 -4 Q18 -18 0 -16 Q-16 -18 -28 -4 Z" fill="{LINE}"/>{f}</g></g>')


def small_person(x, y, s, shirt, skin, hair=LINE, wave=False, bun=False, apron=False, facing=1):
    arm_r = (f'<path d="M9 -52 Q20 -64 24 -80" {L(2)}/><circle cx="25" cy="-83" r="4" fill="{skin}" {S} stroke-width="1.6"/>'
             if wave else f'<path d="M9 -52 Q14 -38 12 -26" {L(2)}/><circle cx="12" cy="-24" r="3.5" fill="{skin}" {S} stroke-width="1.6"/>')
    ap = f'<path d="M-7 -44 L-8 -24 L8 -24 L7 -44 Z" fill="{SAGE}" {S} stroke-width="1.5"/>' if apron else ""
    b = f'<circle cx="6" cy="-92" r="6" fill="{hair}" {S} stroke-width="1.5"/>' if bun else ""
    return f'''<g transform="translate({x},{y}) scale({s * facing},{s})"><g class="boil">
  <path d="M-5 -24 L-6 0 M5 -24 L6 0" {L(2)}/><path d="M-10 0 H-4 M4 0 H10" {L(2)}/>
  <path d="M-12 -58 Q0 -64 12 -58 L14 -24 L-14 -24 Z" fill="{shirt}" {S} stroke-width="1.8"/>{ap}
  <path d="M-9 -52 Q-14 -38 -12 -26" {L(2)}/><circle cx="-12" cy="-24" r="3.5" fill="{skin}" {S} stroke-width="1.6"/>{arm_r}
  {b}<circle cx="0" cy="-74" r="10" fill="{skin}" {S} stroke-width="1.8"/>
  <path d="M-10 -76 Q-10 -86 0 -86 Q10 -86 10 -76 Q4 -81 -10 -76 Z" fill="{hair}"/>
  <circle cx="-3.5" cy="-73" r="1.2" fill="{LINE}"/><circle cx="3.5" cy="-73" r="1.2" fill="{LINE}"/><path d="M-3 -68 Q0 -66 3 -68" {L(1.3)}/>
</g></g>'''


# ---------------------------------------------------------------- objects
def envelope(x, y, r=0):
    return (f'<g transform="translate({x},{y}) rotate({r})"><rect x="-26" y="-8" width="52" height="16" rx="2" fill="{WHITE}" {S} stroke-width="1.6"/>'
            f'<path d="M-26 -8 L0 2 L26 -8" {L(1.4)}/></g>')


def folder(x, y, r=0, c=BUTTER):
    return (f'<g transform="translate({x},{y}) rotate({r})"><path d="M-28 -9 H-10 L-6 -13 H28 V9 H-28 Z" fill="{c}" {S} stroke-width="1.6"/></g>')


def paper(x, y, r=0):
    return (f'<g transform="translate({x},{y}) rotate({r})"><rect x="-24" y="-6" width="48" height="12" rx="1.5" fill="{WHITE}" {S} stroke-width="1.5"/>'
            f'<path d="M-16 0 H12" {L(1.2)}/></g>')


def stack(kind, n):
    """A wobbly stack sitting on y=0, centred on x=0, growing upward."""
    out = []
    rots = [-3, 4, -2, 5, -4, 2, -5, 3, -1]
    offs = [0, 4, -3, 5, -4, 2, -5, 3, 0]
    for i in range(n):
        y = -10 - i * 15
        if kind == "mail":
            out.append(envelope(offs[i], y, rots[i]))
        elif kind == "folders":
            out.append(folder(offs[i], y, rots[i], [BUTTER, SKY, PEACH, SAGE][i % 4]))
        else:
            out.append(paper(offs[i], y, rots[i]))
    return "".join(out)


def reach_hand(sleeve, skin):
    """An arm reaching in. Wrist at origin, pointing +x. The sleeve runs off to the left."""
    return (f'<g class="boil"><path d="M-520 -15 H-4 Q4 0 -4 15 H-520 Z" fill="{sleeve}" {S}/>'
            f'<path d="M-14 -15 V15" {L(1.6)}/>'
            f'<path d="M-4 -12 Q14 -20 32 -14 Q44 -9 44 0 Q44 9 32 12 L10 14 Q-2 14 -4 10 Z" fill="{skin}" {S}/>'
            f'<path d="M12 -14 Q20 -28 30 -26 Q36 -24 32 -16" fill="{skin}" {S}/>'
            f'<path d="M30 -4 H44 M28 5 H42" {L(1.5)}/></g>')


# ---------------------------------------------------------------- hero
def building(x, w, h, fill, sign, kind):
    base = 380
    top = base - h
    out = [f'<rect x="{x + 10}" y="{top + 8}" width="{w}" height="{h}" rx="3" fill="{fill}"/>']
    g = [f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="3" {L(2.4)}/>']
    if kind == "gable":
        g.append(f'<path d="M{x - 8} {top + 2} L{x + w / 2} {top - 40} L{x + w + 8} {top + 2}" {L(2.4)}/>')
    else:
        g.append(f'<path d="M{x - 6} {top} H{x + w + 6}" {L(2.6)}/>')
    cols = 3 if w >= 190 else 2
    gap = w / (cols + 1)
    rows = [top + 22] + ([top + 76] if h >= 240 else [])
    for ry in rows:
        for i in range(cols):
            cx = x + gap * (i + 1)
            g.append(f'<rect x="{cx - 15}" y="{ry}" width="30" height="38" rx="2" {L(1.6)}/><path d="M{cx} {ry} V{ry + 38}" {L(1.3)}/>')
    sy = base - 118
    g.append(f'<rect x="{x + 18}" y="{sy}" width="{w - 36}" height="22" rx="3" fill="{WHITE}" {S} stroke-width="1.6"/>')
    if kind == "awning":
        ay = base - 88
        n = 7
        sw = (w - 12) / n
        d = f"M{x + 6} {ay} H{x + w - 6} "
        for i in range(n):
            x0 = x + w - 6 - i * sw
            d += f"Q{x0 - sw / 2} {ay + 16} {x0 - sw} {ay} "
        g.append(f'<path d="{d}" {L(1.8)}/>')
    g.append(f'<rect x="{x + 16}" y="{base - 60}" width="{w * 0.5}" height="44" rx="2" {L(1.8)}/>')
    dx = x + w - 52
    g.append(f'<rect x="{dx}" y="{base - 66}" width="34" height="66" rx="2" {L(1.8)}/><circle cx="{dx + 27}" cy="{base - 32}" r="1.8" fill="{LINE}"/>')
    txt = (f'<text x="{x + w / 2}" y="{sy + 15}" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="10.5" '
           f'font-weight="600" letter-spacing="2" fill="{INK}">{sign}</text>')
    extra = ""
    if sign.startswith("WINDOWS"):
        extra = (f'<g transform="translate({dx + 17},{base - 50})"><g class="sign-swing"><path d="M-8 -12 L0 -20 L8 -12" {L(1.4)}/>'
                 f'<rect x="-14" y="-12" width="28" height="13" rx="2" fill="{BUTTER}" {S} stroke-width="1.4"/>'
                 f'<text x="0" y="-2.5" text-anchor="middle" font-family="DM Sans, sans-serif" font-size="7.5" font-weight="700" fill="{INK}">OPEN</text></g></g>')
    return "".join(out) + '<g filter="url(#rough)">' + "".join(g) + "</g>" + txt + extra


def tree(x, r=24, fill=SAGE):
    return (f'<circle cx="{x + 7}" cy="{380 - 46 - r + 6}" r="{r}" fill="{fill}"/>'
            f'<g filter="url(#rough)"><circle cx="{x}" cy="{380 - 46 - r}" r="{r}" {L(2)}/><path d="M{x} {380 - 46} V380" {L(2.2)}/></g>')


def cloud(x, y, s, cls):
    return (f'<g transform="translate({x},{y}) scale({s})"><g class="{cls}"><path filter="url(#rough)" {L(1.8)} '
            f'd="M-50 16 C-58 0 -38 -12 -24 -6 C-18 -24 12 -26 18 -8 C32 -16 54 -4 46 12 C56 16 52 26 40 26 L-42 26 C-56 26 -60 20 -50 16 Z"/></g></g>')


def hero_svg():
    p = [f'<path d="M0 300 C160 250 300 280 430 262 C600 238 720 286 880 258 C1010 236 1110 262 1200 248 L1200 380 L0 380 Z" fill="{SAGE}" opacity="0.5"/>',
         f'<circle cx="1010" cy="96" r="36" fill="{BUTTER}"/>',
         cloud(180, 92, 1.0, "drift-a"), cloud(820, 70, 0.8, "drift-b")]
    blds = [(70, 190, 210, PEACH, "WINDOWS &amp; DOORS", "flat"),
            (290, 160, 192, SAND, "BAKERY", "awning"),
            (480, 200, 250, SAGE, "INSURANCE", "gable"),
            (710, 170, 190, SKY, "HARDWARE", "awning"),
            (910, 200, 224, PEACH, "VET CLINIC", "flat")]
    for i, b in enumerate(blds):
        p.append(f'<g class="rise" style="animation-delay: {0.1 + i * 0.1:.2f}s">{building(*b)}</g>')
    p.append(tree(36, 20) + tree(1150, 26))
    p.append(f'<path d="M0 380 H1200" {L(2.4)} filter="url(#rough)"/>')
    p.append(small_person(118, 410, 1.25, BUTTER, SKIN[0], hair="#5B3A2A", wave=True, bun=True, apron=True))
    p.append(small_person(172, 410, 1.2, SKY, SKIN[1], facing=-1))
    p.append(small_person(640, 410, 1.2, PEACH, SKIN[2]))
    p.append(small_person(1010, 410, 1.2, SAGE, SKIN[3], wave=True))
    return ('<svg viewBox="0 0 1200 440" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" '
            'style="display: block; width: 100%; height: auto; overflow: visible">' + "".join(p) + '</svg>')


# ---------------------------------------------------------------- story stage
def stage_svg():
    p = []
    # back wall
    p.append(f'<rect x="0" y="0" width="800" height="600" fill="{BG}"/>')
    p.append(f'<g filter="url(#rough)"><rect x="470" y="70" width="230" height="150" rx="4" fill="{SKY}" {S} stroke-width="2.2"/><path d="M585 70 V220 M470 145 H700" {L(1.6)}/></g>')
    p.append(f'<g filter="url(#rough)"><path d="M90 170 H330" {L(2.4)}/>'
             + "".join(f'<rect x="{x}" y="{170 - h}" width="22" height="{h}" rx="2" fill="{c}" {S} stroke-width="1.6"/>'
                       for x, h, c in [(104, 54, PEACH), (130, 62, SAGE), (156, 48, BUTTER), (182, 58, SKY), (250, 40, PEACH)])
             + f'<g transform="translate(296,150)"><circle r="18" fill="{WHITE}" {S}/><path d="M0 -10 V0 L7 5" {L(1.8)}/></g></g>')
    p.append(f'<path d="M0 520 H800" {L(2.4)} filter="url(#rough)"/>')
    # Maria (three moods, one visible at a time)
    p.append('<g transform="translate(330,380)"><g class="boil">' + maria("stressed") + maria("neutral") + maria("happy") + '</g></g>')
    # customer
    p.append('<g transform="translate(680,520)"><g class="boil">' + customer(False) + customer(True) + '</g></g>')
    p.append(f'<g class="bubble" transform="translate(560,250)"><g class="boil"><path d="M-40 -16 C-40 -42 40 -42 40 -16 C40 4 20 8 10 8 L-4 24 L-4 8 C-24 8 -40 2 -40 -16 Z" fill="{WHITE}" {S}/>'
             f'<path d="M0 0 C-8 -6 -12 -10 -12 -14 C-12 -20 -5 -22 0 -16 C5 -22 12 -20 12 -14 C12 -10 8 -6 0 0 Z" fill="{MUSTARD}"/></g></g>')
    # counter (in front of Maria, behind the stacks)
    p.append(f'<rect x="196" y="388" width="380" height="132" fill="{SAND}"/>')
    p.append(f'<g filter="url(#rough)"><rect x="186" y="380" width="380" height="140" rx="3" {L(2.4)}/><path d="M176 380 H576" {L(3)}/>'
             f'<path d="M226 410 V500 M376 410 V500 M526 410 V500" {L(1.4)}/></g>')
    # the three stacks, each in a wrapper JS can move
    homes = {"mail": (240, 380), "folders": (390, 380), "drafts": (500, 380)}
    counts = {"mail": 6, "folders": 5, "drafts": 8}
    for k, (x, y) in homes.items():
        p.append(f'<g class="pile" data-pile="{k}" data-home="{x},{y}" transform="translate({x},{y})"><g class="boil">{stack(k, counts[k])}</g></g>')
    # the hands, parked off stage; JS moves them
    hands = [("mail", "#B9D3C5", SKIN[1], 0, 0), ("folders", "#C9D9E6", SKIN[0], 90, 0), ("drafts", "#F2CDB8", SKIN[2], 110, 0)]
    for k, sleeve, skin, rot, _ in hands:
        p.append(f'<g class="hand" data-hand="{k}" transform="translate(-200,-200)"><g transform="rotate({rot})">{reach_hand(sleeve, skin)}</g></g>')
    return ('<svg class="stage-svg" viewBox="120 60 640 480" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Maria at her shop counter. Helping hands lift away her piles of paperwork until she is free to talk with her customer.">'
            + "".join(p) + '</svg>')


# ---------------------------------------------------------------- small icons & misc
def step_svg(n):
    if n == 1:
        body = (small_person(64, 140, 1.35, PEACH, SKIN[0]) + small_person(164, 140, 1.35, SKY, SKIN[2], facing=-1) +
                f'<g filter="url(#rough)"><path d="M88 100 H140 M96 100 V140 M132 100 V140" {L(2)}/><path d="M102 100 V90 H112 V100 M120 100 V92 H130 V100" {L(1.6)}/></g>')
        blob = SAND
    elif n == 2:
        body = (f'<g filter="url(#rough)"><rect x="62" y="56" width="96" height="62" rx="5" {L(2)}/><path d="M50 128 H170 L160 118 H60 Z" {L(2)}/>'
                f'<circle cx="88" cy="87" r="7" {L(1.8)}/><circle cx="132" cy="76" r="7" {L(1.8)}/><circle cx="132" cy="100" r="7" {L(1.8)}/><path d="M95 85 L125 77 M95 89 L125 99" {L(1.6)}/></g>'
                f'<g transform="translate(176,46)"><g class="spin"><circle cx="0" cy="0" r="10" {L(1.8)}/>'
                + "".join(f'<path d="M0 -10 V-15" {L(1.8)} transform="rotate({a})"/>' for a in range(0, 360, 45)) + '</g></g>')
        blob = SAGE
    else:
        bars = "".join(f'<rect x="{x}" y="{128 - h}" width="18" height="{h}" rx="2" fill="{c}" {S}/>'
                       for x, h, c in [(102, 28, WHITE), (128, 46, WHITE), (154, 70, BUTTER)])
        body = small_person(64, 140, 1.35, SAGE, SKIN[3], wave=True) + bars + f'<path d="M92 128 H184" {L(2)}/>'
        blob = PEACH
    return (f'<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="display: block; width: 100%; max-width: 220px; height: auto; overflow: visible">'
            f'<ellipse cx="114" cy="92" rx="94" ry="54" fill="{blob}"/>{body}</svg>')


def mike_svg():
    return (f'<svg viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="display: block; width: 200px; height: 200px">'
            f'<circle cx="110" cy="112" r="96" fill="{SAGE}"/>' + small_person(110, 214, 2.2, BUTTER, SKIN[0], hair="#6B4B35", wave=True) + '</svg>')


def train_svg():
    cars = ""
    for x, w, r in [(10, 100, 10), (118, 100, 10), (226, 84, 18)]:
        cars += f'<rect x="{x + 5}" y="22" width="{w}" height="36" rx="{r}" fill="{SKY if x < 226 else PEACH}"/><rect x="{x}" y="18" width="{w}" height="36" rx="{r}" {L(2)}/>'
        for wx in range(x + 12, x + w - 20, 26):
            cars += f'<rect x="{wx}" y="27" width="18" height="12" rx="2" {L(1.5)}/>'
    return (f'<div style="overflow: hidden; width: 100%; max-width: 360px"><svg viewBox="0 0 320 70" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="display: block; width: 100%; height: auto">'
            f'<path d="M0 62 H320" {L(2)}/><g class="train"><g filter="url(#rough)">{cars}</g></g></svg></div>')


def logo(size=38):
    return (f'<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="display: block; width: {size}px; height: {size}px">'
            f'<circle cx="24" cy="24" r="21" fill="{BUTTER}" stroke="{LINE}" stroke-width="1.8"/>'
            f'<path d="M13 25 L24 15.5 L35 25 V35 H13 Z" fill="none" stroke="{LINE}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M24 31.5 C20.5 28.5 19.5 27 19.5 25.6 C19.5 23.8 22 23 24 25 C26 23 28.5 23.8 28.5 25.6 C28.5 27 27.5 28.5 24 31.5 Z" fill="{MUSTARD}"/></svg>')


def wave(top, bottom, flip=False):
    d = "M0 44 C240 10 480 66 720 38 C960 10 1200 60 1440 30 L1440 80 L0 80 Z"
    tr = ' transform="scale(1,-1) translate(0,-80)"' if flip else ""
    return (f'<div style="background: {top}; line-height: 0"><svg viewBox="0 0 1440 80" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" '
            f'aria-hidden="true" style="display: block; width: 100%; height: 56px"><path d="{d}" fill="{bottom}"{tr}/></svg></div>')


ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true" style="width: 16px; height: 16px"><path d="M3 8 H13 M9 4 L13 8 L9 12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CHECK = f'<svg viewBox="0 0 16 16" aria-hidden="true" style="flex: none; width: 16px; height: 16px; margin-top: 4px"><circle cx="8" cy="8" r="8" fill="{SAGE}"/><path d="M4.5 8.2 L7 10.5 L11.5 5.8" fill="none" stroke="{GREEN}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

GRAIN = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' "
         "baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0.12 0 0 0 0 0.16 0 0 0 0 0.14 0 0 0 0.55 0'/%3E%3C/filter%3E"
         "%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")

CSS = f"""
:root{{--ink:{INK};--green:{GREEN};--deep:{DEEP};--bg:{BG};--sand:{SAND};--sage:{SAGE};--butter:{BUTTER};--mustard:{MUSTARD};--muted:{MUTED};--rule:{RULE};
--serif:Fraunces,Georgia,serif;--glide:cubic-bezier(.2,.7,.2,1)}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:'DM Sans',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
body::after{{content:"";position:fixed;inset:0;pointer-events:none;z-index:50;background-image:url("{GRAIN}");opacity:.07;mix-blend-mode:multiply}}
a{{color:var(--green)}}a:hover{{color:var(--deep)}}
:focus-visible{{outline:3px solid var(--mustard);outline-offset:3px}}
.wrap{{max-width:1160px;margin:0 auto;padding:0 24px}}
h1,h2,h3{{font-family:var(--serif);font-weight:500;font-variation-settings:'SOFT' 40,'opsz' 96;color:var(--ink);margin:0}}
h2{{font-size:clamp(32px,4vw,50px);line-height:1.08;letter-spacing:-.015em}}
h3{{font-size:24px;line-height:1.2}}
.eyebrow{{margin:0;font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--green)}}
.body{{font-size:18px;line-height:1.65;color:var(--muted);margin:0}}
.small{{font-size:16px;line-height:1.6;color:var(--muted);margin:0}}
.card{{background:#fff;border:1px solid var(--rule);border-radius:22px;box-shadow:0 1px 2px rgba(30,42,36,.04),0 18px 40px -24px rgba(30,42,36,.18)}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:52px;padding:0 26px;border-radius:999px;background:var(--green);color:#fff;font-weight:700;font-size:16px;text-decoration:none;border:none;transition:transform .25s var(--glide),box-shadow .25s var(--glide),background-color .25s}}
.btn:hover{{color:#fff;transform:translateY(-2px);box-shadow:0 10px 24px -12px rgba(34,70,58,.55)}}
.btn.ghost{{background:transparent;color:var(--ink);border:1.5px solid var(--ink)}}
.btn.ghost:hover{{color:var(--ink)}}
.lift{{transition:transform .35s var(--glide),box-shadow .35s var(--glide)}}
.lift:hover{{transform:translateY(-4px);box-shadow:0 2px 4px rgba(30,42,36,.05),0 28px 48px -26px rgba(30,42,36,.28)}}

/* drawn things jump: lines boil in steps */
@keyframes boil{{0%{{filter:url(#b1)}}33%{{filter:url(#b2)}}66%{{filter:url(#b3)}}}}
.boil{{animation:boil .5s steps(1) infinite}}
@keyframes rise{{from{{opacity:0;transform:translateY(24px)}}to{{opacity:1;transform:none}}}}
.rise{{animation:rise .9s var(--glide) both}}
@keyframes drift{{0%{{transform:translateX(-12px)}}50%{{transform:translateX(4px)}}100%{{transform:translateX(16px)}}}}
.drift-a{{animation:drift 9s steps(9) infinite alternate}}
.drift-b{{animation:drift 12s steps(12) infinite alternate-reverse}}
@keyframes swing{{0%,100%{{transform:rotate(-7deg)}}50%{{transform:rotate(7deg)}}}}
.sign-swing{{transform-box:fill-box;transform-origin:50% 0;animation:swing 2.4s steps(6) infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.spin{{animation:spin 8s steps(16) infinite}}
@keyframes train{{from{{transform:translateX(-330px)}}to{{transform:translateX(330px)}}}}
.train{{animation:train 14s linear infinite}}
@keyframes ring{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
.ring{{animation:ring .6s steps(1) infinite}}

/* UI glides: reveal on scroll */
.reveal{{opacity:0;transform:translateY(26px);transition:opacity .8s var(--glide),transform .8s var(--glide)}}
.reveal.in{{opacity:1;transform:none}}
.no-js .reveal{{opacity:1;transform:none}}

/* floating nav pill */
.pill{{position:fixed;top:14px;left:50%;z-index:40;display:flex;align-items:center;gap:16px;padding:8px 8px 8px 14px;border-radius:999px;background:rgba(255,255,255,.86);
backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid var(--rule);box-shadow:0 12px 30px -16px rgba(30,42,36,.35);
transform:translate(-50%,-140%);transition:transform .5s var(--glide)}}
.pill.show{{transform:translate(-50%,0)}}
.pill .dots{{display:flex;gap:6px}}
.pill .dots a{{display:flex;align-items:center;gap:6px;padding:8px 10px;border-radius:999px;font-size:14px;font-weight:500;color:var(--muted);text-decoration:none;transition:background-color .3s,color .3s}}
.pill .dots a::before{{content:"";width:7px;height:7px;border-radius:50%;border:1.5px solid currentColor;transition:background-color .3s}}
.pill .dots a.on{{color:var(--ink);background:var(--sand)}}
.pill .dots a.on::before{{background:var(--mustard);border-color:var(--mustard)}}
.pill .btn{{min-height:40px;font-size:14px;padding:0 16px}}

/* the story: pinned, scroll-scrubbed */
.story{{position:relative;background:var(--bg)}}
.story-stick{{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:40px;align-items:center;max-width:1240px;margin:0 auto;padding:0 24px}}
.stage{{position:relative;border-radius:28px;overflow:hidden;background:#F7F2E9;border:1px solid var(--rule)}}
.stage-svg{{display:block;width:100%;height:auto}}
.beats{{position:relative}}
.beat{{display:flex;flex-direction:column;gap:14px;padding:22px 0}}
.beat .tag{{display:inline-flex;align-self:flex-start;padding:5px 12px;border-radius:999px;background:var(--sand);font-size:13px;font-weight:700;color:var(--ink)}}
.beat blockquote{{margin:4px 0 0;padding:14px 16px;border-radius:16px 16px 16px 4px;background:#fff;border:1px solid var(--rule);font-size:15px;line-height:1.55;color:var(--ink)}}
.beat blockquote b{{display:block;margin-bottom:4px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--green)}}
.mood{{display:none}}
.stage .mood-happy,.stage .cust-happy{{display:none}}
.stage .mood-stressed{{display:inline}}
.stage .bubble{{opacity:0;transition:opacity .5s var(--glide)}}
.stage[data-mood="neutral"] .mood-stressed{{display:none}}.stage[data-mood="neutral"] .mood-neutral{{display:inline}}
.stage[data-mood="happy"] .mood-stressed{{display:none}}.stage[data-mood="happy"] .mood-happy{{display:inline}}
.stage[data-mood="happy"] .cust-wait{{display:none}}.stage[data-mood="happy"] .cust-happy{{display:inline}}
.stage[data-mood="happy"] .bubble{{opacity:1}}
.progress-dots{{display:flex;gap:8px;margin-top:6px}}
.progress-dots span{{width:28px;height:4px;border-radius:2px;background:var(--rule);transition:background-color .4s}}
.progress-dots span.on{{background:var(--mustard)}}
.js-story .story{{height:520vh}}
.js-story .story-stick{{position:sticky;top:0;height:100vh}}
.js-story .beats{{height:min(440px,56vh)}}
.js-story .beat{{position:absolute;inset:0;justify-content:center;opacity:0;transform:translateY(18px);transition:opacity .5s var(--glide),transform .5s var(--glide);pointer-events:none}}
.js-story .beat.on{{opacity:1;transform:none;pointer-events:auto}}
html:not(.js-story) .stage .mood-stressed{{display:none}}html:not(.js-story) .stage .mood-happy,html:not(.js-story) .stage .cust-happy{{display:inline}}html:not(.js-story) .stage .cust-wait{{display:none}}html:not(.js-story) .stage .bubble{{opacity:1}}html:not(.js-story) .pile{{display:none}}html:not(.js-story) .progress-dots{{display:none}}

/* how it works: pinned, scroll-scrubbed */
.how{{background:var(--deep);color:#fff}}
.how-stick{{max-width:1160px;margin:0 auto;padding:56px 24px 72px;display:flex;flex-direction:column;gap:34px}}
.weeks{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}}
.week{{display:flex;flex-direction:column;gap:8px;font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#B7CABF}}
.week .bar{{height:10px;border-radius:5px;background:rgba(255,255,255,.12);overflow:hidden}}
.week .bar i{{display:block;height:100%;width:calc(var(--f,1)*100%);background:var(--butter);border-radius:5px}}
.steps{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:28px;margin:0;padding:0;list-style:none}}
.steps li{{display:flex;flex-direction:column;gap:14px;transition:opacity .5s var(--glide),transform .5s var(--glide)}}
.steps .art{{padding:18px;border-radius:20px;background:#fff;display:flex;justify-content:center}}
.steps h3{{color:#fff}}
.steps p{{font-size:16px;line-height:1.6;margin:0;color:#D6E3DB}}
.js-story .how{{height:300vh}}
.js-story .how-stick{{position:sticky;top:0;min-height:100vh;justify-content:center}}
.js-story .steps li{{opacity:.28;transform:translateY(14px)}}
.js-story .steps li.on{{opacity:1;transform:none}}

@media (max-width:860px){{
  .story-stick{{grid-template-columns:1fr;gap:6px;align-content:center}} .stage{{order:-1}}
  .js-story .story-stick{{grid-template-rows:auto auto;padding-top:72px}}
  .js-story .beats{{height:min(400px,calc(100vh - 72px - 74vw - 40px))}}
  .beat{{gap:8px;padding:12px 0}} .beat .body{{font-size:15.5px;line-height:1.55}} .beat h3{{font-size:22px!important}} .beat blockquote{{font-size:14px;padding:10px 12px}}
  .js-story .how{{height:auto}} .js-story .how-stick{{position:static;min-height:0}} .js-story .steps li{{opacity:1;transform:none}}
  header.wrap{{flex-wrap:nowrap!important}} header .btn{{min-height:40px!important;font-size:14px!important;padding:0 14px!important}}
  .steps{{grid-template-columns:1fr;gap:16px}}
  .js-story .how{{height:260vh}}
  .js-story .steps .art{{display:none}}
  .pill .dots{{display:none}}
  .navlink{{display:none}}
}}
@media (prefers-reduced-motion: reduce){{
  *,*::before,*::after{{animation:none!important;transition:none!important}}
}}
"""

chips = ["Contractors and trades", "Window and door showrooms", "Insurance agencies", "Dental and vet offices",
         "Property managers", "Bookkeepers and accountants", "Landscapers", "Salons and studios"]

beats = [
    ("Monday, 7:40am", "This is Maria's counter.",
     "She runs a small window and door shop. Customers love her because she remembers every job. But before the doors open, she's already behind on email, quotes and paperwork.", None),
    ("Less copying", "The email pile goes first.",
     "Quote requests, web forms and phone notes get turned into organized records in her CRM. Someone on her team checks them. Nobody retypes them.",
     "Three quote requests came in over the weekend. They are in your CRM now, with the missing measurements flagged."),
    ("Less searching", "Then the folders.",
     "When a customer calls, the details she needs are pulled together in one place: last order, install date, notes.",
     "Mrs. Alvarez is on line two. Here is her last order, the install date, and the note about her side gate."),
    ("Less prep", "Then the routine drafts.",
     "Follow-ups, summaries and routine documents are drafted for a person to review and send.",
     "Five follow-up emails from today's site visits are drafted and waiting for your OK."),
    ("10:15am", "And Maria gets back to the counter.",
     "That's the whole point. The busywork gets lighter, so she has time for the person in front of her.", None),
]

steps = [
    ("Week 1", "Get to know the work", "We sit with your team, learn where personal attention matters most, and map the tasks that eat the week. We check the tools you already pay for first."),
    ("Weeks 2 and 3", "Build it with the people who use it", "We set up one agreed improvement, connect your existing tools, and test it against real examples, odd cases included."),
    ("Week 4", "Train, measure, hand over", "We train your team, write down who owns what, and compare results to where you started."),
]

plans = [
    ("Intro call", "$0", "20 minutes", "We look at your week together and tell you honestly whether we can help.",
     ["A quick look at where time goes", "One or two ideas you can use anyway", "No pressure, no pitch deck"], "Book a call", False),
    ("Your first month", "$3,500", "fixed, one time", "One real improvement, built inside the tools you already use and running by the end of the month.",
     ["Discovery with your team", "One workflow set up and tested on real examples", "Training for everyone who uses it", "Before and after numbers", "30 days of follow-up help"], "Start with a call", True),
    ("Keep it running", "$750", "per month, optional", "For after your first month. We keep things working and keep improving them.",
     ["Monitoring and fixes", "Small improvements as your work changes", "A monthly check-in", "Cancel anytime"], "Ask about it", False),
]

faqs = [
    ("Will customers still deal with a real person?", "Yes. For your first project, customer conversations stay with your team. AI helps prepare and organize information behind the scenes."),
    ("Will this make our service feel less personal?", "We start by finding the parts of your service customers value most, then choose what to automate around them. Your team keeps control of customer-facing messages and decisions."),
    ("What if we don't know where to start?", "Pick one task your team repeats every week. We will tell you honestly whether AI, a feature in software you already own, or a simpler process is the right fix."),
    ("Do we need to buy new software?", "Usually not. We start with what you already use, like your email, calendar, CRM or accounting system. If something new would help, we explain the cost before you decide. Any subscription is billed by the vendor, not marked up by us."),
    ("What does it cost?", "Your first month is $3,500, fixed and agreed in writing before any work begins. Ongoing help is optional at $750 a month. The first conversation is always free."),
]


def nav():
    links = "".join(f'<a href="#{h}" class="navlink" style="color: {INK}; text-decoration: none; font-weight: 500; font-size: 15px; padding: 10px 2px">{t}</a>'
                    for h, t in [("story", "How it helps"), ("pricing", "Pricing"), ("questions", "Questions")])
    pill_links = "".join(f'<a href="#{h}" data-sec="{h}">{t}</a>' for h, t in [("story", "Story"), ("how", "How it works"), ("pricing", "Pricing"), ("questions", "Questions")])
    return f'''<header class="wrap" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; padding-top: 20px; padding-bottom: 20px">
  <a href="#top" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: {INK}">{logo()}<span style="font-family: var(--serif); font-weight: 600; font-size: 24px; letter-spacing: -0.01em">Many Hands</span></a>
  <nav aria-label="Main" style="display: flex; flex-wrap: wrap; align-items: center; gap: 26px">{links}<a href="#talk" class="btn" style="min-height: 44px; font-size: 15px; padding: 0 20px">Book a free call</a></nav>
</header>
<div class="pill" aria-label="Sections"><a href="#top" aria-label="Back to top" style="display: flex">{logo(30)}</a><nav class="dots" aria-label="Page sections">{pill_links}</nav><a href="#talk" class="btn">Book a call</a></div>'''


def hero():
    return f'''<section id="top" style="padding-top: 36px">
  <div class="wrap" style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 22px">
    <p class="rise" style="margin: 0; display: inline-flex; align-items: center; gap: 10px; padding: 7px 16px; border-radius: 999px; background: #fff; border: 1px solid {RULE}; font-size: 14px; font-weight: 500">
      <span style="width: 8px; height: 8px; border-radius: 50%; background: {MUSTARD}; display: inline-block"></span>Practical AI for small businesses in NY, NJ and CT</p>
    <h1 class="rise" style="animation-delay: .08s; font-size: clamp(42px, 6vw, 82px); line-height: 1.04; letter-spacing: -0.025em; max-width: 960px">
      Keep the personal touch.<br><span style="background: linear-gradient(transparent 80%, {BUTTER} 80%, {BUTTER} 94%, transparent 94%); padding: 0 4px; font-style: italic">Hand off the busywork.</span></h1>
    <p class="body rise" style="animation-delay: .16s; font-size: clamp(17px, 1.5vw, 20px); max-width: 680px">We find the repetitive admin that pulls your team away from customers, set up AI inside the tools you already use, and train your people to run it. One month. One real improvement. A fixed price.</p>
    <div class="rise" style="animation-delay: .24s; display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 4px">
      <a href="#talk" class="btn">Book a free 20-minute call {ARROW}</a><a href="#story" class="btn ghost">See how it helps</a></div>
    <p class="rise" style="animation-delay: .3s; margin: 0; font-size: 14px; color: {MUTED}">$3,500 fixed for your first month. No long contracts. Your team stays in charge.</p>
  </div>
  <div style="margin-top: 28px; line-height: 0; overflow: hidden; background: linear-gradient(to bottom, {BG} 86.4%, {SAND} 86.4%)"><div style="max-width: 1360px; min-width: 760px; position: relative; left: 50%; transform: translateX(-50%); padding: 0 12px">{hero_svg()}</div></div>
</section>'''


def who():
    chip_html = "".join(f'<li style="list-style: none; padding: 9px 16px; border-radius: 999px; background: #fff; border: 1px solid {RULE}; font-size: 15px">{c}</li>' for c in chips)
    return f'''<section style="background: {SAND}; padding: 4px 0 52px">
  <div class="wrap reveal" style="display: flex; flex-direction: column; align-items: center; gap: 20px; text-align: center">
    <p style="margin: 0; font-family: var(--serif); font-size: clamp(20px, 2vw, 26px)">Made for the shops, offices and crews that keep a town running</p>
    <ul style="margin: 0; padding: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; max-width: 960px">{chip_html}</ul>
  </div>
</section>'''


def story():
    bhtml = ""
    for i, (tag, title, body, ex) in enumerate(beats):
        quote = f'<blockquote><b>For example</b>"{ex}"</blockquote>' if ex else ""
        lead = '<p class="eyebrow">Why we do this</p>' if i == 0 else ""
        bhtml += f'<article class="beat{" on" if i == 0 else ""}" data-beat="{i}">{lead}<span class="tag">{tag}</span><h3 style="font-size: clamp(26px, 2.6vw, 34px)">{title}</h3><p class="body">{body}</p>{quote}</article>'
    dots = "".join(f'<span{" class=on" if i == 0 else ""}></span>' for i in range(len(beats)))
    return f'''<section id="story" class="story" aria-label="How Many Hands helps: Maria's morning">
  <div class="story-stick">
    <div><div class="beats">{bhtml}</div><div class="progress-dots" aria-hidden="true">{dots}</div></div>
    <div class="stage" data-mood="stressed">{stage_svg()}</div>
  </div>
</section>'''


def how():
    weeks = "".join(f'<div class="week">Week {i}<span class="bar"><i></i></span></div>' for i in range(1, 5))
    lis = "".join(f'''<li data-step="{i}"><div class="art">{step_svg(i)}</div>
      <p style="margin: 0; font-size: 13px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: {BUTTER}">{w}</p>
      <h3>{t}</h3><p>{b}</p></li>''' for i, (w, t, b) in enumerate(steps, start=1))
    return f'''{wave(BG, DEEP)}
<section id="how" class="how">
  <div class="how-stick">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 760px">
      <p class="eyebrow" style="color: {BUTTER}">How it works</p>
      <h2 style="color: #fff">One month. One real improvement.</h2>
      <p class="body" style="color: #D6E3DB">It starts with a free conversation to see if we are a good fit. If we are, you get one fixed fee for the month, agreed in writing before any work begins.</p>
    </div>
    <div class="weeks" aria-hidden="true">{weeks}</div>
    <ol class="steps">{lis}</ol>
  </div>
</section>
{wave(BG, DEEP, flip=True)}'''


def pricing():
    html = ""
    for name, price, unit, desc, items, cta, featured in plans:
        lis = "".join(f'<li style="display: flex; gap: 10px; font-size: 15px; line-height: 1.5">{CHECK}<span>{t}</span></li>' for t in items)
        badge = (f'<p style="margin: 0; align-self: flex-start; padding: 5px 12px; border-radius: 999px; background: {BUTTER}; font-size: 12px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase">Most businesses start here</p>' if featured else "")
        border = f"border: 2px solid {GREEN}" if featured else ""
        html += f'''<article class="card lift reveal" style="flex: 1 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 16px; padding: 30px; {border}">
      {badge}<h3>{name}</h3>
      <p style="margin: 0; display: flex; align-items: baseline; gap: 8px"><span style="font-family: var(--serif); font-weight: 500; font-size: 48px; letter-spacing: -0.02em">{price}</span><span style="font-size: 15px; color: {MUTED}">{unit}</span></p>
      <p class="small">{desc}</p>
      <ul style="margin: 4px 0 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 10px">{lis}</ul>
      <a href="#talk" class="btn{"" if featured else " ghost"}" style="margin-top: auto">{cta}</a></article>'''
    return f'''<section id="pricing" style="padding: 88px 0 40px">
  <div class="wrap" style="display: flex; flex-direction: column; gap: 40px">
    <div class="reveal" style="display: flex; flex-direction: column; gap: 16px; max-width: 720px">
      <p class="eyebrow">Pricing</p><h2>Simple, fixed and agreed up front.</h2>
      <p class="body">No hourly billing and no surprise invoices. You know the price before we start.</p></div>
    <div style="display: flex; flex-wrap: wrap; gap: 24px; align-items: stretch">{html}</div>
    <p class="small reveal" style="font-size: 15px">Prices are for teams of up to 25 people. Larger team or more than one workflow? We will quote it on the call.</p>
  </div>
</section>'''


def questions():
    q_html = "".join(f'<div class="card reveal" style="padding: 22px 26px; display: flex; flex-direction: column; gap: 8px"><h3 style="font-size: 21px">{q}</h3><p class="small">{a}</p></div>' for q, a in faqs)
    return f'''<section id="questions" style="padding: 72px 0 104px">
  <div class="wrap" style="display: flex; flex-wrap: wrap; gap: 48px; align-items: flex-start">
    <div class="reveal" style="flex: 1 1 300px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p class="eyebrow">Questions</p><h2>You decide where AI belongs.</h2><p class="body">Straight answers to what owners ask us first.</p></div>
    <div style="flex: 2 1 520px; min-width: 0; display: flex; flex-direction: column; gap: 14px">{q_html}</div>
  </div>
</section>'''


def founder():
    return f'''<section style="background: {SAND}; padding: 92px 0">
  <div class="wrap reveal" style="display: flex; flex-wrap: wrap; align-items: center; gap: 48px">
    <div style="flex: 0 0 auto">{mike_svg()}</div>
    <div style="flex: 1 1 460px; min-width: 0; display: flex; flex-direction: column; gap: 16px">
      <p class="eyebrow">Who you work with</p><h2>A local partner, not a call center.</h2>
      <p class="body">Hi, I'm Mike. I live in Fairfield County and have spent my career helping businesses use technology safely. Right now I'm helping a small window and door company set up AI across sales, operations and the back office.</p>
      <p class="body">When you work with Many Hands, you work with me. I'll come by in person when it helps, and I'll tell you plainly when something isn't worth automating.</p>
      <div style="margin-top: 8px; display: flex; flex-wrap: wrap; align-items: center; gap: 20px">{train_svg()}<p style="margin: 0; font-size: 14px; font-weight: 700">From Fairfield County to Westchester, North Jersey and the city.</p></div>
    </div>
  </div>
</section>'''


def field(label, fid, kind="text", optional=False, area=False):
    opt = f' <span style="font-weight: 400; color: {MUTED}">(optional)</span>' if optional else ""
    req = "" if optional else " required"
    common = f'id="{fid}" name="{fid}"{req} style="width: 100%; padding: 14px 16px; font: inherit; font-size: 16px; color: {INK}; background: #fff; border: 1px solid #CFC6B6; border-radius: 12px"'
    inp = f'<textarea {common} rows="4"></textarea>' if area else f'<input type="{kind}" {common}>'
    flex = "none" if area else "1 1 220px"
    return f'<div style="display: flex; flex-direction: column; gap: 8px; flex: {flex}; min-width: 0"><label for="{fid}" style="font-weight: 600; font-size: 14px">{label}{opt}</label>{inp}</div>'


def cta():
    return f'''<section id="talk" style="padding: 96px 0">
  <div class="wrap">
    <div class="reveal" style="display: flex; flex-wrap: wrap; gap: 48px; padding: clamp(28px, 5vw, 56px); border-radius: 32px; background: {DEEP}">
      <div style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 18px">
        <h2 style="color: #fff">What would give your team more time for customers?</h2>
        <p class="body" style="color: #D6E3DB">Tell us about the admin that interrupts conversations, slows down replies, or keeps people working after the day should be done. We will find one practical place to start.</p>
        <p style="margin: 0; font-size: 15px; line-height: 1.6; color: {BUTTER}">The first conversation is free. Any paid work starts only after we agree on the scope and the fee.</p>
      </div>
      <form name="contact" method="POST" data-netlify="true" netlify-honeypot="company_url" action="/thanks.html" style="flex: 1 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 16px; padding: 28px; background: {BG}; border-radius: 22px">
        <input type="hidden" name="form-name" value="contact"><p hidden><label>Leave blank <input name="company_url"></label></p>
        <div style="display: flex; flex-wrap: wrap; gap: 16px">{field("Your name", "name")}{field("Business name", "business", optional=True)}</div>
        <div style="display: flex; flex-wrap: wrap; gap: 16px">{field("Email", "email", "email")}{field("Phone", "phone", "tel", optional=True)}</div>
        {field("What eats up your week?", "message", area=True)}
        <button type="submit" class="btn" style="cursor: pointer; font-family: inherit; width: 100%">Tell us about your workflow {ARROW}</button>
      </form>
    </div>
  </div>
</section>'''


def footer():
    return f'''<footer style="border-top: 1px solid {RULE}; padding: 40px 0">
  <div class="wrap" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px">
    <div style="display: flex; align-items: center; gap: 12px">{logo(40)}<div><p style="margin: 0; font-family: var(--serif); font-weight: 600; font-size: 21px">Many Hands</p><p style="margin: 0; font-size: 14px; color: {MUTED}">Many hands make light work.</p></div></div>
    <p style="margin: 0; font-size: 14px; color: {MUTED}">Practical AI for small businesses in New York, New Jersey and Connecticut</p>
    <a href="mailto:hello@manyhandsco.com" style="font-weight: 700; font-size: 15px">hello@manyhandsco.com</a>
  </div>
</footer>'''


FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100&amp;family=DM+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet">'

html = f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Many Hands | Practical AI for small businesses in NY, NJ and CT</title>
<meta name="description" content="We find the repetitive admin that pulls your team away from customers, set up AI inside the tools you already use, and train your people to run it. One month, one real improvement, $3,500 fixed.">
<meta property="og:title" content="Many Hands | Practical AI for small businesses">
<meta property="og:description" content="Keep the personal touch. Hand off the busywork. One month, one real improvement, a fixed price.">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E%3Ccircle cx='24' cy='24' r='22' fill='%23F3D18A'/%3E%3Cpath d='M13 25 L24 15 L35 25 V35 H13 Z' fill='none' stroke='%2326332D' stroke-width='2.4' stroke-linejoin='round'/%3E%3C/svg%3E">
{FONTS}
<script>document.documentElement.classList.replace('no-js','js');</script>
<style>{CSS}</style>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Many Hands","description":"Practical AI implementation for small businesses","areaServed":["New York","New Jersey","Connecticut"],"url":"https://hellomanyhands.com"}}</script>
</head>
<body>
{DEFS}
{nav()}
<main>
{hero()}
{who()}
{story()}
{how()}
{pricing()}
{questions()}
{founder()}
{cta()}
</main>
{footer()}
<script src="/story.js" defer></script>
</body>
</html>
'''

with open(os.path.join(ROOT, "index.html"), "w") as f:
    f.write(html)
print("wrote index.html", len(html))
