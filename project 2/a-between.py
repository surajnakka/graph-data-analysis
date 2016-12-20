
import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

input_file = sys.argv[1]
Graph1 = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)


bc = set()
between = dict()

NIdV = snap.TIntV()
for i in range(1, 10000):
	rm_node = Graph1.GetRndNId()
	if (rm_node not in NIdV):
		NIdV.Add(rm_node)

print NIdV.Len()

Graph = snap.GetSubGraph(Graph1, NIdV)

#computing betweenness centrality
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 0.1)

#storing Nodes : Hash Table data to a dictionary
for node in Nodes:
	between[node] = Nodes[node]

	
for item in between:
	bc.add(between[item])

with open (sys.argv[1]+'.betweenness.txt','w+') as fp:
	for p in sorted(between.items(), key=lambda (k,v): (v,k),reverse=True):
		fp.write("%s : %s\n" % p)

bc = sorted(bc,key=float,reverse=True)

#plotting betweenness centrality
plt.plot(np.arange(1,len(bc)+1,1),bc,'b.')
plt.xlabel('Rank')
plt.ylabel('Betweenness Centrality')
plt.savefig(sys.argv[1]+'.betweenness_plot.png')
plt.close()