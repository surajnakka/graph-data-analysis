import snap
import sys

input_file = sys.argv[1]
#graph loading
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)

nodes = list()
for NI in Graph.Nodes():
	nodes.append(NI.GetId())

nodes.sort()


print nodes[-1]
print len(nodes)