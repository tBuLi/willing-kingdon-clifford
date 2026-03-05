from ..config import alg3d, alg2d, clrs
import timeit
import numpy as np


def arrow(from_point, to_point, w=0.03, aspect=0.8, camera=1 ):
    # TODO: make this into a proper arrow
    return [from_point, to_point]
     # from_point = from_point/(-from_point|!1e0); to_point = to_point/(-to_point|!1e0);
     # var line = ( from_point & to_point ), l = line.Length;
     # var shape = [[0,w],[l-5*w,w],[l-5*w,aspect*5*w],[l,0],[l-5*w,-aspect*5*w],[l-5*w,-w],[0,-w]].map(([x,y])=>!(1e0+x*1e1+y*1e2));
     # var sqrt = R => R==-1?1e12:(1+R).Normalized;
     # var R = ((to_point - from_point).UnDual).Normalized * 1e1;
     # var R2 = sqrt(from_point/!1e0) * sqrt(R);
     # var p2 = R2 >>> 1e3;
     # if (p2 != 0) { var p1 = (((~(camera+0e1) >>> 1e3)|line)/line).Normalized; return sqrt(p1/p2) * R2 >>> shape; }
     # return  R2  >>> shape;

def train(x):
    return f'''<g transform="translate({(4*-x.e023+1.2)},{4*x.dual().e2-1.44}) scale(-.0075,.0075)">
      <!-- frame -->
      <rect x="150" y="145" width="280" height="34" rx="8" fill="#1f2937"/>

      <!-- boiler -->
      <rect x="150" y="88" width="260" height="68" rx="34" fill="#374151"/>
      <!-- front plate -->
      <rect x="395" y="92" width="35" height="60" rx="12" fill="#4b5563"/>
      <circle cx="412" cy="122" r="16" fill="none" stroke="#9ca3af" stroke-width="4"/>

      <!-- cab -->
      <rect x="300" y="58" width="120" height="92" rx="12" fill="#111827"/>
      <rect x="288" y="48" width="145" height="16" rx="8" fill="#0b1220"/>
      <rect x="322" y="80" width="42" height="34" rx="5" fill="#93c5fd" opacity="0.85"/>
      <rect x="372" y="80" width="42" height="34" rx="5" fill="#93c5fd" opacity="0.7"/>

      <!-- chimney -->
      <rect x="185" y="60" width="24" height="34" rx="7" fill="#111827"/>
      <rect x="177" y="54" width="40" height="10" rx="6" fill="#0b1220"/>

      <!-- headlamp -->
      <circle cx="432" cy="132" r="8" fill="#fde68a"/>
      <circle cx="432" cy="132" r="10" fill="none" stroke="#f59e0b" stroke-width="3"/>

      <!-- wheels -->
      <g>
        <circle cx="175" cy="184" r="14" fill="#111827"/>
        <circle cx="175" cy="184" r="9" fill="none" stroke="#9ca3af" stroke-width="3" opacity="0.9"/>

        <circle cx="245" cy="182" r="26" fill="#111827"/>
        <circle cx="325" cy="182" r="26" fill="#111827"/>
        <circle cx="405" cy="182" r="26" fill="#111827"/>

        <g fill="none" stroke="#9ca3af" stroke-width="4" opacity="0.9">
          <circle cx="245" cy="182" r="18"/>
          <circle cx="325" cy="182" r="18"/>
          <circle cx="405" cy="182" r="18"/>
        </g>
      </g>

      <!-- connecting rod -->
      <rect x="262" y="173" width="160" height="8" rx="4" fill="#9ca3af" opacity="0.9"/>
      <circle cx="272" cy="177" r="6" fill="#e5e7eb"/>
      <circle cx="412" cy="177" r="6" fill="#e5e7eb"/>

      <!-- outline accents -->
      <g fill="none" stroke="#0b0f14" stroke-width="3" opacity="0.45">
        <rect x="150" y="145" width="280" height="34" rx="8"/>
        <rect x="150" y="88" width="260" height="68" rx="34"/>
        <rect x="300" y="58" width="120" height="92" rx="12"/>
        <rect x="395" y="92" width="35" height="60" rx="12"/>
      </g>
    </g>
'''

def bullet(x):
    return f'''<g transform="translate({(-4*x.e023)},{4*x.dual().e2-0.5}) scale(.2,-0.2)">
  <!-- Bullet body -->
  <rect x="-1.6" y="-0.32" width="2.0" height="0.64" rx="0.12" fill="#6b7280"/>

  <!-- casing base (not wider than body) -->
  <rect x="-1.6" y="-0.28" width="0.22" height="0.56" rx="0.1" fill="#4b5563"/>

  <!-- rounded bullet tip -->
  <path
    d="
      M 0.4 -0.32
      Q 1.6 0
        0.4 0.32
      Z
    "
    fill="#9ca3af"
  />

  <!-- subtle outline -->
  <g fill="none" stroke="#111827" stroke-width="0.06" opacity="0.6">
    <rect x="-1.6" y="-0.32" width="2.0" height="0.64" rx="0.12"/>
    <path d="M 0.4 -0.32 Q 1.6 0 0.4 0.32 Z"/>
  </g>
</g>
'''

def spaceship(x):
    return f'''<g transform="translate({(-4*x.e023)},{4*x.dual().e2-1.2}) scale(.003,0.003)">
    <!-- SAUCER -->
    <ellipse cx="420" cy="130" rx="160" ry="60" fill="#374151"/>
    <ellipse cx="420" cy="130" rx="120" ry="42" fill="#4b5563"/>
    <ellipse cx="420" cy="130" rx="70" ry="22" fill="#93c5fd" opacity="0.85"/>
    <ellipse cx="420" cy="130" rx="160" ry="60"
             fill="none" stroke="#9ca3af" stroke-width="6" opacity="0.6"/>

    <!-- NECK -->
    <rect x="300" y="155" width="60" height="70" rx="16" fill="#1f2937"/>

    <!-- SECONDARY HULL -->
    <ellipse cx="280" cy="245" rx="95" ry="40" fill="#1f2937"/>
    <ellipse cx="280" cy="245" rx="60" ry="24" fill="#374151"/>

    <!-- DEFLECTOR -->
    <circle cx="255" cy="260" r="14" fill="#f59e0b"/>
    <circle cx="255" cy="260" r="20"
            fill="none" stroke="#fde68a" stroke-width="4" opacity="0.7"/>

    <!-- STRUTS -->
    <rect x="260" y="165" width="40" height="18" rx="8" fill="#111827"/>
    <rect x="260" y="195" width="40" height="18" rx="8" fill="#111827"/>

    <!-- NACELLES -->
    <rect x="120" y="150" width="140" height="36" rx="18" fill="#111827"/>
    <rect x="130" y="155" width="120" height="26" rx="13" fill="#374151"/>
    <rect x="150" y="161" width="80" height="14" rx="7" fill="#60a5fa"/>

    <rect x="120" y="210" width="140" height="36" rx="18" fill="#111827"/>
    <rect x="130" y="215" width="120" height="26" rx="13" fill="#374151"/>
    <rect x="150" y="221" width="80" height="14" rx="7" fill="#60a5fa"/>

    <!-- AGGRESSIVE WARP PLASMA -->
    <!-- TOP -->
    <polygon points="120,168 60,150 40,155 20,160 10,168 20,176 40,181 60,186"
             fill="#7dd3fc" opacity="0.75"/>
    <polygon points="120,168 30,140 0,150 -10,168 0,186 30,196"
             fill="none" stroke="#38bdf8" stroke-width="8" opacity="0.5"/>
    <polygon points="120,168 70,162 40,168 70,174"
             fill="#e0f2fe" opacity="0.9"/>

    <!-- BOTTOM -->
    <polygon points="120,228 60,210 40,215 20,220 10,228 20,236 40,241 60,246"
             fill="#7dd3fc" opacity="0.75"/>
    <polygon points="120,228 30,200 0,210 -10,228 0,246 30,256"
             fill="none" stroke="#38bdf8" stroke-width="8" opacity="0.5"/>
    <polygon points="120,228 70,222 40,228 70,234"
             fill="#e0f2fe" opacity="0.9"/>

    <!-- WINDOW STRIP -->
    <g fill="#9ca3af">
      <rect x="340" y="144" width="12" height="6" rx="3"/>
      <rect x="370" y="144" width="12" height="6" rx="3"/>
      <rect x="400" y="144" width="12" height="6" rx="3"/>
      <rect x="430" y="144" width="12" height="6" rx="3"/>
      <rect x="460" y="144" width="12" height="6" rx="3"/>
    </g>

    <!-- OUTLINES -->
    <g fill="none" stroke="#0b0f14" stroke-width="6" opacity="0.35">
      <ellipse cx="420" cy="130" rx="160" ry="60"/>
      <ellipse cx="280" cy="245" rx="95" ry="40"/>
      <rect x="120" y="150" width="140" height="36" rx="18"/>
      <rect x="120" y="210" width="140" height="36" rx="18"/>
    </g>
</g>
</g>
'''

def torpedo(x):
    return f'''<g transform="translate({(-4*x.e023+1.3)},{4*x.dual().e2-0.6}) scale(.1,-0.1)">
  <!-- Photon torpedo, facing RIGHT -->
  <!-- Original design ~260x70, scaled to width=4 -->
  <g transform="translate(-2,-0.3) scale(0.0145)">

    <!-- MAIN CASING -->
    <rect x="90" y="85" width="130" height="50" rx="24" fill="#1f2937"/>

    <!-- FORWARD EMITTER RING -->
    <rect x="210" y="90" width="18" height="40" rx="8" fill="#f59e0b"/>

    <!-- NOSE CONE -->
    <polygon points="228,85 270,110 228,135" fill="#374151"/>

    <!-- CONTAINMENT BANDS -->
    <rect x="120" y="88" width="10" height="44" rx="5" fill="#111827"/>
    <rect x="144" y="88" width="10" height="44" rx="5" fill="#111827"/>
    <rect x="168" y="88" width="10" height="44" rx="5" fill="#111827"/>

    <!-- STABILIZATION FINS -->
    <polygon points="110,85 130,60 146,85" fill="#111827"/>
    <polygon points="110,135 130,160 146,135" fill="#111827"/>

    <!-- PHOTON CORE -->
    <circle cx="90" cy="110" r="14" fill="#fde68a"/>
    <circle cx="90" cy="110" r="22" fill="none" stroke="#f59e0b" stroke-width="6" opacity="0.8"/>

    <!-- PHOTON EXHAUST (SHORT, VIOLENT) -->
    <polygon points="90,110 40,92 40,128"
             fill="#fde68a" opacity="0.85"/>
    <polygon points="90,110 18,78 -10,110 18,142"
             fill="none" stroke="#f59e0b" stroke-width="7" opacity="0.55"/>

    <!-- ENERGY SPIKE -->
    <polygon points="90,110 56,106 38,110 56,114"
             fill="#fff7ed" opacity="0.95"/>

    <!-- OUTLINE -->
    <g fill="none" stroke="#0b0f14" stroke-width="5" opacity="0.45">
      <rect x="90" y="85" width="130" height="50" rx="24"/>
      <polygon points="228,85 270,110 228,135"/>
    </g>
</g>
</g>
'''

def alice(x):
    return f'''<g transform="translate({(-4*x.e023)},{4*x.dual().e2-0.0}) scale(.4,-0.4)">
  <!-- head (slimmer) -->
  <circle cx="0" cy="1.1" r="0.30" fill="#fde68a"/>

  <!-- hair (full, blonde, reduced width) -->
  <path
    d="
      M -0.38 1.18
      Q  0    1.52
         0.38 1.18
      L  0.34 0.80
      Q  0    0.70
        -0.34 0.80
      Z
    "
    fill="#facc15"
  />

  <!-- bow -->
  <circle cx="-0.15" cy="1.36" r="0.07" fill="#ef4444"/>
  <circle cx="0.15"  cy="1.36" r="0.07" fill="#ef4444"/>
  <circle cx="0" cy="1.34" r="0.045" fill="#b91c1c"/>

  <!-- dress (narrow A-line) -->
  <path
    d="
      M -0.40 0.60
      L  0.40 0.60
      L  0.62 -0.90
      L -0.62 -0.90
      Z
    "
    fill="#60a5fa"
  />

  <!-- arms (closer to body, symmetric) -->
  <rect x="-0.70" y="0.24" width="0.28" height="0.10" rx="0.05" fill="#fde68a"/>
  <rect x="0.42"  y="0.24" width="0.28" height="0.10" rx="0.05" fill="#fde68a"/>

  <!-- legs (closer together) -->
  <rect x="-0.12" y="-1.40" width="0.16" height="0.50" rx="0.08" fill="#1f2937"/>
  <rect x="0.12"  y="-1.40" width="0.16" height="0.50" rx="0.08" fill="#1f2937"/>

  <!-- shoes -->
  <rect x="-0.24" y="-1.45" width="0.26" height="0.12" rx="0.06" fill="#111827"/>
  <rect x="-0.02" y="-1.45" width="0.26" height="0.12" rx="0.06" fill="#111827"/>

</g>
'''

def earth(x):
    return f'''<g transform="translate({(-4*x.e023)},{4*x.dual().e2-0.8}) scale(1.5,1.5)">
  <!-- Single Earth circle with oceans + continents -->

  <!-- EARTH OCEAN -->
  <circle cx="0" cy="3.6" r="3.0" fill="#2563eb"/>

  <!-- CONTINENTS -->
  <!-- Top continent (highest point = land) -->
  <path d="
    M -0.8 0.95
    Q -0.4 0.75 0 0.85
    Q 0.4 0.75 0.9 0.95
    Q 0.6 1.1 0.1 1.15
    Q -0.4 1.1 -0.8 0.95
    Z"
    fill="#16a34a"/>

  <!-- Secondary land masses -->
  <path d="
    M -1.6 1.35
    Q -1.3 1.15 -1.0 1.3
    Q -0.9 1.55 -1.2 1.6
    Q -1.5 1.55 -1.6 1.35
    Z"
    fill="#15803d"/>

  <path d="
    M 0.9 1.45
    Q 1.2 1.25 1.5 1.4
    Q 1.4 1.7 1.1 1.75
    Q 0.85 1.65 0.9 1.45
    Z"
    fill="#166534"/>

  <!-- DESERT / VARIATION -->
  <ellipse cx="0.2" cy="1.05" rx="0.25" ry="0.12"
           fill="#ca8a04" opacity="0.85"/>

  <!-- ATMOSPHERE RIM -->
  <circle cx="0" cy="3.6" r="3.04"
          fill="none"
          stroke="#7dd3fc"
          stroke-width="0.06"
          opacity="0.6"/>

  <!-- HORIZON EDGE HIGHLIGHT -->
  <circle cx="0" cy="3.6" r="3.0"
          fill="none"
          stroke="#bfdbfe"
          stroke-width="0.035"
          opacity="0.8"/>
</g>    
'''

alg = alg3d
A = alg.vector(e0=1, e3=1).dual()
B = alg.vector(e0=1, e3=0, e2=0).dual()
_track = (B | alg.blades.e1)
Tp = alg.evenmv(e=1, e03=0.1)
Tm = alg.evenmv(e=1, e03=-0.1)
Tp2 = alg.evenmv(e=1, e03=0.15)
Tm2 = alg.evenmv(e=1, e03=-0.15)
Tw = alg.evenmv(e=1, e01=0.02)
Th = alg.evenmv(e=1, e02=0.02)
track1 = Tp >> _track
track2 = Tm >> _track
sleeper = [Tp2 >> B, Tp2*Tw >> B, Tm2*Tw >> B, Tm2 >> B]
# sleeper += Th >> sleeper
# sleeper = [Tp >> B, Tp*Tw >> B, Tm*Tw >> B, Tm >> B]
sleepers = [alg.evenmv(e=1, e01=x) >> sleeper for x in np.arange(-0.9, 1, 0.1)]

v1 = alg.bivector(e01=1)
v2 = alg.bivector(e01=1)
v3 = alg.bivector(e01=1)
v4 = alg.bivector(e01=1)
B = (0.5*v1).exp() >> B

t0 = None

def addition_of_velocity():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = ((timeit.default_timer() - t0) / 5) % 3.5
    frame, bullet_time = divmod(t, 1.75)
    R = (-0.5*(t-0.6)*v1).exp()
    R_bullet = (-0.5 * bullet_time * v2).exp()
    subjects = [
        # str(t),
        # str(frame),
        # str(bullet_time),
        # B, "Bob",
        track1,
        track2,
        0x7B3F00,
        *sleepers,
        0,
        Bp := R >> B, train(Bp := R >> B), #"Bob",
        '<G fill-opacity=0.0 stroke-opacity=0.0>' if frame == 0 else '<G>',
        0xffffff if frame == 0 else clrs[6],
        bullet(R_bullet*alg.evenmv(e=1, e03=0.93) >> Bp), #'bullet',
        '</G>',
        '<G fill-opacity=0.0>',
        alg.vector(e0=1, e2=-0.3).dual(),
        '</G>',
        0,
        # bullet(alg.blades.e0.dual()),
        # '$v_1$',
        alice(A),
    ]
    # if frame > 0:
    #     subjects.extend([])
    return subjects

def addition_of_velocity_spaceship():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = ((timeit.default_timer() - t0) / 5) % 3.4
    frame, bullet_time = divmod(t, 1.7)
    R = (-0.5*(t-0.9)*v3).exp()
    R_bullet = (-0.5 * (bullet_time) * v4).exp()
    subjects = [
        0,
        # Bp := R >> B, 
        spaceship(Bp := R >> B), #"Bob",
        '<G fill-opacity=0.0 stroke-opacity=0.0>' if frame == 0 else '<G>',
        0xffffff if frame == 0 else clrs[6],
        torpedo(R_bullet >> Bp), #'bullet',
        '</G>',
        0xffffff, alg.vector(e0=1, e2=-0.3).dual(),
        0,
        earth(A),
        alice(A),
    ]
    # if frame > 0:
    #     subjects.extend([])
    return subjects