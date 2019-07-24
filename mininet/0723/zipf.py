from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
import numpy as np

TOTAL_BW = 1000

class ZipfGenerator:

    def __init__(self, n=TOTAL_BW, alpha=0.8):
        tmp = np.power(np.arange(1, n + 1), -alpha)
        zeta = np.r_[0., np.cumsum(tmp)]
        self.dist = zeta / zeta[-1]

    def getBandwidth(self, size):
        randList = np.random.rand(size)
        pos = np.searchsorted(self.dist, randList) - 1
        bandwidth = TOTAL_BW - pos
        bandwidth[bandwidth <= 1] = 1
        return bandwidth


class CustomTopo(Topo):
    "Single switch with 4 hosts"

    def __init__(self, n=4):
        # Initialize topology
        Topo.__init__(self)
        # Add switch
        z = ZipfGenerator()
        switch = self.addSwitch('s1')
        # Add hosts and links
        zipfBw = z.getBandwidth(n)
        print zipfBw
        for i in range(n):
            host = self.addHost('h%d' % (i + 1))
            self.addLink(host, switch, bw=zipfBw[i])


def perfTest():
    topo = CustomTopo(n=100)
    # Initialize network with custom topo
    net = Mininet(topo, link=TCLink)
    net.start()
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    perfTest()