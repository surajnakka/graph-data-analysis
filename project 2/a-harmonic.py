
import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

input_file = sys.argv[1]
Graph1 = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)


hc = set()
harmonic = dict()

NIdV = snap.TIntV()
for i in range(1, 10000):
	rm_node = Graph1.GetRndNId()
	if (rm_node not in NIdV):
		NIdV.Add(rm_node)

print NIdV.Len()

Graph = snap.GetSubGraph(Graph1, NIdV)
nodecount = Graph.GetNodes()

for node in Graph.Nodes():
	invdij = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(Graph,node.GetId(),ndh)
	for item in ndh:
		if ndh[item] != 0:
			invdij = invdij + (1.0/ndh[item])
	hcentr = invdij/(nodecount-1)
	harmonic[node.GetId()] = hcentr

for item in harmonic:
	hc.add(harmonic[item])

with open (sys.argv[1]+'.harmonic.txt','w+') as fp:
	for p in sorted(harmonic.items(), key=lambda (k,v): (v,k),reverse=True):
		fp.write("%s : %s\n" % p)
		
hc = sorted(hc,key=float,reverse=True)

#plotting harmonic closeness centrality
plt.plot(np.arange(1,len(hc)+1,1),hc,'b.')
plt.xlabel('Rank')
plt.ylabel('Harmonic Closness Centrality')
plt.savefig(sys.argv[1]+'.harmonic_plot.png')
plt.close()