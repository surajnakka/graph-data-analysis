
import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

input_file = sys.argv[1]
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)


clc = set()
cluster = dict()

for node in Graph.Nodes():
	clustering = snap.GetNodeClustCf(Graph,node.GetId())
	cluster[node.GetId()] = clustering

for item in cluster:
	clc.add(cluster[item])

with open (sys.argv[1]+'.clustering.txt','w+') as fp:
	for p in sorted(cluster.items(), key=lambda (k,v): (v,k),reverse=True):
		fp.write("%s : %s\n" % p)
		
clc = sorted(clc,key=float,reverse=True)

#plotting clustering coefficient
plt.plot(np.arange(1,len(clc)+1,1),clc,'b.')
plt.xlabel('Rank')
plt.ylabel('Clustering Coefficient')
plt.savefig(sys.argv[1]+'.clustering_plot.png')
plt.close()