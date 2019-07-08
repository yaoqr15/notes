from datetime import datetime
from mininet.topo import Topo
from mininet.net import Mininet

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
            self.addLink(host, switch)


def perfTest():
    topo = CustomTopo()
    # Initialize network with custom topo
    net = Mininet(topo)
    net.start()
    # Get the host object
    h1, h2 = net.get('h1', 'h2')
    
    # Run iperf as server in h1
    h1.cmd('iperf', '-s', '&')

    start = datetime.now()
    # Run iperf as client in h2, h1 as the reciever, size 10GB
    print h2.cmd('iperf', '-c', h1.IP(), '-n', '10G')
    end = datetime.now()
    
    print '\nIt took %f seconds to finish.' % (end - start).total_seconds()
    net.stop()

if __name__ == '__main__':
    perfTest()