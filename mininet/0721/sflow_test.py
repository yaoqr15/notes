from collections import defaultdict
import requests
import json

# get topology data to identify the interfaces
r = requests.get("http://192.168.248.129:8008/topology/json")
topo = json.loads(r.text)
nodes = topo['nodes']

# build a dict with an index-to-name relationship
indexToName = defaultdict()
for switch in nodes:
    # all interfaces of a single switch
    ports = nodes[switch]['ports']
    for name in ports:
        # a single interface
        index = ports[name]["ifindex"]
        indexToName[index] = name


# get the current meric value of mininet bytes
# 'TOPOLOGY' is the agent's name, 'sort:mn_bytes:-' means results will be sorted in reverse order
r = requests.get("http://192.168.248.129:8008/table/TOPOLOGY/sort:mn_bytes:-/json")
portsData = json.loads(r.text)

# build a dict with an name-to-metricValue relationship
portsSpeed = defaultdict()
for port in portsData:
    index = port[0]['dataSource']
    name = indexToName[index]
    portsSpeed[name] = port[0]['metricValue']

print(portsSpeed)