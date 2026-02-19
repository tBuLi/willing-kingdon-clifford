from ..config import ptap, clrs, alg2d

alg = ptap
T = alg.evenmv(e=1, e02=0.7)
earth = alg.vector(e0=1, e1=0, e2=0).dual()
mars = alg.vector(e0=1, e1=1, e2=1.1).dual()
jupiter = alg.vector(e0=1, e1=0, e2=2).dual()
earth, mars, jupiter = T >> [earth, mars, jupiter]

def normalized(x):
    if alg is alg2d:
        return x.normalized()
    return x / (-x.normsq().e)**0.5

def norm(x):
    if x > 0:
        return x**0.5
    return (-x)**0.5

def journey():
    l_em = earth & mars
    l_mj = mars & jupiter
    l_je = jupiter & earth
    # bip = normalized(l_em) + normalized(l_mj)
    # bim = normalized(l_em) - normalized(l_mj)
    bip_m = l_em + l_mj
    bim_m = l_em - l_mj
    bim_e = l_em - l_je
    bim_j = l_je - l_mj
    half = normalized(bim_m ^ l_je)
    return [
        # str(l_em),
        # str(l_mj),
        # str(l_em+l_mj),
        # str(l_je),
        # str(l_em + l_mj + l_je),
        earth, 'earth',
        mars, 'mars',
        jupiter, 'jupiter',
        str(norm(l_je.normsq().e)),
        l_em, 'l_em',
        l_mj, 'l_mj',
        # l_je, 'l_je',
        clrs[0],
        bip_m, 'l_em+l_mj',
        bim_m, 'l_em-l_mj',
        bim_e,
        bim_j,
        half,
        str(norm((earth & half).normsq().e)),
        earth + jupiter + mars, 'C',
        bip_m @ earth,
    ]