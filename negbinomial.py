import math

def c(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


def prob(n, p, r):
    return c(n + r - 1, n) * pow(p, r) * pow(1 - p, n)

def infoMeasure(n, p, r):
    return -math.log2(prob(n, p, r))

def _sumProb(k, p, r):
    if k == 0:
        return prob(k, p, r)
    else:
        return _sumProb(k - 1, p, r) + prob(k, p, r)

def sumProb(n, p, r):
    return _sumProb(n, p, r)

def _approxEntropy(k, p, r):
    if k == 0:
        return prob(k, p, r) * infoMeasure(k, p, r)
    else:
        return _approxEntropy(k - 1, p, r) + prob(k, p, r) * infoMeasure(k, p, r)

def approxEntropy(n, p, r):
    return _approxEntropy(n, p, r)


# print(approxEntropy(200, 1/2, 5))