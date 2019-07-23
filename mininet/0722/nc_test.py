from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel

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

    # Generate the file of specified size
    # 'truncate stdfile -s 250M' also works
    h2.cmd("dd if=/dev/zero of=./stdfile bs=250M count=1")
    # Server: send data to TCP port, and listen for requests
    h1.cmd("nc -l 8888 < stdfile &")
    # Client: send request to server, receive the file
    h2.cmd("nc %s 8888 > newfile" % h1.IP())

    net.stop()

if __name__ == '__main__':
    # setLogLevel( 'info' )
    perfTest()
