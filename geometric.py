import math

# def _info(k, p = 1/2):
#     if k == 1:
#         return p * math.log2(1/p)
#     else:
#         return _info(k-1, p) + pow(p, k) * math.log(pow(1/p, k))

def prob(n, p = 1/2):
    return pow(1 - p, n - 1) * p

def infoMeasure(n, p = 1/2):
    return -math.log2(prob(n, p))

def _sumProb(k, p):
    if k == 1:
        return prob(1, p)
    else:
        return _sumProb(k - 1, p) + prob(k, p)

"""
    sumProb có thể chứng minh tổng xác suất của phân bố geometric bằng 1 bởi:
        sumProb(500) = 1.0
    * Hàm không hỗ trợ tới 1000 vì người viết sử dụng đệ quy thay vì vòng lặp
"""
def sumProb(n, p = 1/2):
    return _sumProb(n, p)

def _approxEntropy(k, p = 1/2):
    if k == 1:
        return prob(k, p) * infoMeasure(k, p)
    else:
        return _approxEntropy(k - 1, p) + prob(k, p) * infoMeasure(k, p)

"""
    approxEntropy tính được xấp xỉ entropy của nguồn tin geometric bởi entropy của nguồn tin này là có giới hạn,
    bằng cách tăng dần số n, ta có thể dùng hàm này để tính gần đúng giá trị entropy.
    thực nghiệm: approxEntropy(500) ~= approxEntropy(700) = 2
"""
def approxEntropy(n, p = 1/2):
    return _approxEntropy(n, p)

# print(sumProb(500))