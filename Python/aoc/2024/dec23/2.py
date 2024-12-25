import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    lines = f.readlines()

computers, connections = set(), set()
for line in lines:
    a, b = line.strip().split('-')
    computers.update([a, b])
    connections.update([(a, b), (b, a)])

networks = [{c} for c in computers]
for network in networks:
    for computer in computers:
        if all((computer, connected) in connections for connected in network):
            network.add(computer)

print(*sorted(max(networks, key=len)), sep=',')  # cl,df,ft,ir,iy,ny,qp,rb,sh,sl,sw,wm,wy