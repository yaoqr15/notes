from mininet.topolib import TreeTopo
from mininet.net import Mininet
from mininet.log import setLogLevel

def demo():
    "Simple Demo of Tree Topo"

    topo = TreeTopo(depth=2, fanout=3)
    net = Mininet(topo)
    net.start()
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    demo()