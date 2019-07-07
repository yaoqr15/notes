# Notes for Mininet

## 目标

1. 搭建集群
2. 模拟网络状态
3. 节点间传输指定数据量
4. 做SDN，监测当前网络状态

## 学习过程记录

### 0.Mininet特点

* 网络仿真系统，可自定义拓扑结构，指定网络参数，运行特定程序及进行网络测试

* 借助轻量级虚拟化技术来创建虚拟节点

* 可通过CLI或Python API操作

### 1.安装流程

这里选择**从源代码安装**的方式。首先从Github中克隆mininet源代码，并执行安装脚本。其中```-a```参数表示安装所有组件与支撑软件，```-s```参数可指定Mininet的安装目录。

```bash
$ git clone git://github.com/mininet/mininet
$ sudo sh ./mininet/util/install.sh -a -s /usr/local/etc/mininet
```

随后通过自带测试来验证mininet的成功安装。当未指定拓扑结构和网络参数时，Mininet默认使用一个包含2个主机和1个交换机的网络。```--test```参数指定节点初始化完成后自动进行的测试，```pingall```即测试各节点两两之间的连通性。

![pingall_test](./pingall_test.jpg)

### 2.搭建集群

Mininet支持使用Python脚本自定义网络拓扑结构。核心在于编写一个继承```Topo```的类，在该类的对象创建时声明网络中包含的主机、交换机以及它们之间的连接线。以下是一个关于自定义拓扑结构的例子：

```python
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

        
# Adding the 'topos' dict with a key/value pair to generate our newly define topology enables one to pass in '--topo=mytopo' from the command line.        
topos = { 'mytopo': ( lambda: MyTopo() ) }
```

其中在最后一行代码中，```topos```是约定用于检索拓扑结构的字典。通过```--custom```参数指定Python源文件，可在mininet的命令行参数中引入用户自定义拓扑结构，并在```--topo```参数处声明当前使用的拓扑名称。

```bash
$ sudo mn --custom /usr/local/etc/mininet/custom/topo-2sw-2host.py --topo mytopo --test pingall
```

**<u>// to be moved</u>**

假设需要搭建一个包含16个主机和1个交换机的星型拓扑结构网络，步骤如下：

- 编写自定义拓扑文件
是
- 命令行参数引入，并测试
  ```bash
  $ sudo mn --custom /usr/local/etc/mininet/custom/topo-2sw-2host.py --topo mytopo --test pingall
  ```

  