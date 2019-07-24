import numpy as np

TOTAL_BW = 1000

class ZipfGenerator:

    def __init__(self, n=TOTAL_BW, alpha=1.2):
        tmp = np.power(np.arange(1, n + 1), -alpha)
        zeta = np.r_[0., np.cumsum(tmp)]
        self.dist = zeta / zeta[-1]

    def getBandwidth(self, size):
        randList = np.random.rand(size)
        pos = np.searchsorted(self.dist, randList) - 1
        bandwidth = TOTAL_BW - pos
        bandwidth[bandwidth <= 1] = 1
        return bandwidth


z = ZipfGenerator()
a = z.getBandwidth(100)
a.sort()
print(a)
