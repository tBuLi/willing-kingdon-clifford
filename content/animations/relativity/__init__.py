def normalized(x):
    sq = x.normsq().e
    if sq >= 0:
        return x / sq**0.5
    return x / (-sq)**0.5