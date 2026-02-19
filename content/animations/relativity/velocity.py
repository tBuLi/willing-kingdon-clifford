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
v3 = alg.bivector(e13=1) @ A
B = (0.5*v1).exp() >> B

t0 = None

def addition_of_velocity():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = ((timeit.default_timer() - t0) / 5) % 2
    frame, bullet_time = divmod(t, 1)
    R = (-0.5*t*v1).exp()
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
        0xffffff, alg.vector(e0=1, e2=-0.3).dual(),
        0,
        # bullet(alg.blades.e0.dual()),
        # '$v_1$',
        alice(A),
    ]
    # if frame > 0:
    #     subjects.extend([])
    return subjects

def addition_of_velocity_rot():
    global t0
    if t0 is None:
        t0 = timeit.default_timer()
    t = ((timeit.default_timer() - t0) / 5) % 2
    frame, bullet_time = divmod(t, 1)
    R = (-0.5*t*v1).exp()
    R_bullet = (-0.5 * bullet_time * v3).exp()
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
        (R_bullet*alg.evenmv(e=1, e03=0.93) >> Bp), #'bullet',
        '</G>',
        0xffffff, alg.vector(e0=1, e2=-0.3).dual(),
        0,
        # bullet(alg.blades.e0.dual()),
        # '$v_1$',
        alice(A),
        v3,
    ]
    # if frame > 0:
    #     subjects.extend([])
    return subjects