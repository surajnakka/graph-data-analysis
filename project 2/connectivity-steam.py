import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

#loading steam-sweden dataset
Graph = snap.LoadEdgeList(snap.PUNGraph,"Steam-Sweden.txt", 0, 1)


#calculating number of triads with random sampling
NumTriads = snap.GetTriads(Graph,-1)  
print "Number of triads: "+str(NumTriads)

#selecting  random node
rm_node = Graph.GetRndNId()

#random node clustering coefficient
rm_clus_coeff = snap.GetNodeClustCf(Graph,rm_node)
print "Clustering coefficient of random node ",rm_node," in Steam-Sweden: ",rm_clus_coeff


#Number of triads a randomly selected node participates in
num_triads = snap.GetNodeTriads(Graph,rm_node)
print "Number of triads of node ",rm_node," participates in ",num_triads," triads"

#avg and global clustering coefficient
TriadV = snap.TIntTrV()
snap.GetTriads(Graph, TriadV,-1)
OpenTriads = 0
ClosedTriads = 0
for triple in TriadV:
    OpenTriads += triple.Val3()
    ClosedTriads += triple.Val2()

ClosedTriads = ClosedTriads/3
GlobalClcf = float(ClosedTriads)/(float(ClosedTriads)+float(OpenTriads))

GraphClustCoeff = snap.GetClustCf(Graph, -1)
print "Clustering coefficient of the network: ",GraphClustCoeff," (Watts-Strogatz); ",GlobalClcf," (global)"


#core k vs num of edges in k-core
CoreIDSzV = snap.TIntPrV()
kValue = snap.GetKCoreEdges(Graph, CoreIDSzV)
for item in CoreIDSzV:
	plt.plot(item.GetVal1(),item.GetVal2(),'b*')

plt.xlabel('K core')
plt.ylabel('Number of Edges')
plt.savefig('Steam-Sweden.kcoreedges.plot.png')
plt.close()

print "k-core edge-size distribution is in: Steam-Sweden.kcoreedges.plot.png"

#core k vs num of nodes in k-core
CoreIDSzV = snap.TIntPrV()
kValue = snap.GetKCoreNodes(Graph, CoreIDSzV)
for item in CoreIDSzV:
	plt.plot(item.GetVal1(),item.GetVal2(),'b*')

plt.xlabel('K core')
plt.ylabel('Number of Nodes')
plt.savefig('Steam-Sweden.kcorenodes.plot.png')
plt.close()

print "k-core edge-size distribution is in: Steam-Sweden.kcorenodes.plot.png"
