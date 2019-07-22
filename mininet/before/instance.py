from mininet.topo import Topo
from mininet.net import Mininet

class InstanceTopo(Topo):
    '''实例:
     1. 搭建一个4节点集群（节点ABCD），节点间网络带宽均为1Gbps。
     2. 节点ABCD目前带宽分别被占用200M，500M，900M，400M。
     3. 通过SDN得到当前网络状态，找到带宽占用最小的节点（节点A）。
     4.  从节点D向节点A传输一个1MB大小的数据，并得到传输时间。'''
    
    def __init__(self):
        Topo.__init__(self)

        switch = self.addSwitch("s1")

        host = []
        bandwidth = {
            'a': 800,
            'b': 500,
            'c': 100,
            'd': 600
        }
        for x in bandwidth:
            host.append(self.addHost("host_" + x))
            self.addLink(switch, host[-1], bd=bandwidth[x])

topos = {
    'instance': (lambda :InstanceTopo())
}