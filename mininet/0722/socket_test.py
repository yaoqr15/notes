from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
import time

class CustomTopo(Topo):
    "Single switch with 4 hosts"

    def __init__(self, n=4):
        # Initialize topology
        Topo.__init__(self)
        # Add switch
        switch = self.addSwitch('s1')
        # Add hosts and links
        for i in range(1, n + 1):
            host = self.addHost('h%d' % i)
            self.addLink(host, switch, bw=1000)


def perfTest():
    topo = CustomTopo()
    # Initialize network with custom topo
    net = Mininet(topo, link=TCLink)
    net.start()
    # Get the host object
    h1, h2 = net.get('h1', 'h2')
    # Server: waiting to receive file
    h1.cmd("python socket_server.py %s 10086 &" % h1.IP())
    # Client: makes the request to send a file
    h2.cmd("python socket_client.py %s 10086 100M" % h1.IP())

    # Essential !!  Extra time in need to finish the transmission
    time.sleep(1)
    net.stop()

if __name__ == '__main__':
    # setLogLevel( 'info' )
    perfTest()
