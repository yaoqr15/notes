from collections import defaultdict
import requests
import json

r = requests.get("http://192.168.248.129:8008/topology/json")
topo = json.loads(r.text)
nodes = topo['nodes']

indexToName = defaultdict()
for switch in nodes:
    ports = nodes[switch]['ports']
    for name in ports:
        indexToName[ports[name]["ifindex"]] = name


r = requests.get("http://192.168.248.129:8008/table/TOPOLOGY/sort:mn_bytes:-/json")
portsData = json.loads(r.text)

portsSpeed = defaultdict()
for i in range(len(portsData)):
    index = portsData[i][0]['dataSource']
    portsSpeed[index] = portsData[i][0]['metricValue']

print(portsSpeed)