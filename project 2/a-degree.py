import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

input_file = sys.argv[1]
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)


dc = set()
degree = dict()

for node in Graph.Nodes():
	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph, node.GetId())
	degree[node.GetId()] = DegCentr

for item in degree:
	dc.add(degree[item])

with open (sys.argv[1]+'.degree.txt','w+') as fp:
	for p in sorted(degree.items(), key=lambda (k,v): (v,k),reverse=True):
		fp.write("%s : %s\n" % p)

dc = sorted(dc,key=float,reverse=True)

#plotting degree centrality
plt.plot(np.arange(1,len(dc)+1,1),dc,'b.')
plt.xlabel('Rank')
plt.ylabel('Degree Centrality')
plt.savefig(sys.argv[1]+'.degree_plot.png')
plt.close()