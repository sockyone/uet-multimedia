import math

def c(N, k):
    return math.factorial(N) / (math.factorial(k) * math.factorial(N - k))


def prob(n, p, N):
    return c(N, n) * pow(p, n) * pow(1 - p, N - n)

def infoMeasure(n, p, N):
    return -math.log2(prob(n, p, N))

def _sumProb(k, p, N):
    if k == 0:
        return prob(k, p, N)
    else:
        return _sumProb(k - 1, p, N) + prob(k, p, N)

def sumProb(n, p, N):
    return _sumProb(n, p, N)

def _approxEntropy(k, p, N):
    if k == 0:
        return prob(k, p, N) * infoMeasure(k, p, N)
    else:
        return _approxEntropy(k - 1, p, N) + prob(k, p, N) * infoMeasure(k, p, N)

def approxEntropy(n, p, N):
    return _approxEntropy(n, p, N)

# print(prob(5, 1/3, 6))