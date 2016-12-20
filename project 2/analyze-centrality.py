import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')



import matplotlib.pyplot as plt

length = len(sys.argv)

if length==1 :   #no file passed in the arguments
	print "Please enter a file"
	sys.exit()
elif length==2 :	
	input_file = sys.argv[1]
else:
	print "Please enter only one file"
	sys.exit()

#graph loading
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)

#num of nodes
nodecount = Graph.GetNodes()


#creating required lists 
dc = set()
cc = set()
bc = set()
clc = set()
hc = set()

#creating required dictionaries
degree = dict()
closeness = dict()
between = dict()
cluster = dict()
harmonic = dict()


#computing degree, harmonic closeness centralities and clustering coefficient
for node in Graph.Nodes():

	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph, node.GetId())
	degree[node.GetId()] = DegCentr

    #clustering coefficient
	clustering = snap.GetNodeClustCf(Graph,node.GetId())
	cluster[node.GetId()] = clustering

	#harmonic closeness centrality
	invdij = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(Graph,node.GetId(),ndh)
	for item in ndh:
		if ndh[item] != 0 & node.GetId() != item:
			invdij = invdij + (1.0/ndh[item])
	hcentr = invdij/(nodecount-1)
	harmonic[node.GetId()] = hcentr

#considering only max connected component for closeness
MxScc = snap.GetMxScc(Graph)


for node in MxScc.Nodes():
	#closeness centrality
	Clcentr = snap.GetClosenessCentr(MxScc, node.GetId())
	closeness[node.GetId()] = Clcentr
    
#storing centralities in set to remove duplication
for item in degree:
	dc.add(degree[item])

for item in closeness:
	cc.add(closeness[item])

for item in cluster:
	clc.add(cluster[item])

for item in harmonic:
	hc.add(harmonic[item])

#computing betweenness centrality
Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 1.0)

#storing Nodes : Hash Table data to a dictionary
for node in Nodes:
	between[node] = Nodes[node]

	
for item in between:
	bc.add(between[item])

#writing the data to files in descending order
with open (sys.argv[1]+'.betweenness.txt','w+') as fp:
	for p in sorted(between.items(), key=lambda (k,v): (v,k),reverse=True):
		fp.write("%s : %s\n" % p)

with open (sys.argv[1]+'.degree.txt','w+') as fp:
    for p in sorted(degree.items(), key=lambda (k,v): (v,k),reverse=True):
        fp.write("%s : %s\n" % p)

with open (sys.argv[1]+'.closeness.txt','w+') as fp:
    for p in sorted(closeness.items(), key=lambda (k,v): (v,k),reverse=True):
        fp.write("%s : %s\n" % p)

with open (sys.argv[1]+'.clustering.txt','w+') as fp:
    for p in sorted(cluster.items(), key=lambda (k,v): (v,k),reverse=True):
        fp.write("%s : %s\n" % p)

with open (sys.argv[1]+'.harmonic.txt','w+') as fp:
    for p in sorted(harmonic.items(), key=lambda (k,v): (v,k),reverse=True):
        fp.write("%s : %s\n" % p)

print "The txt files sorted in decreasing order based on centrality values are in\nfiles:"
print "\t",sys.argv[1]+".degree.txt"
print "\t",sys.argv[1]+".closeness.txt"
print "\t",sys.argv[1]+".harmonic.txt"
print "\t",sys.argv[1]+".betweenness.txt"
print "\t",sys.argv[1]+".clustering.txt"
print "respectively."

dc = sorted(dc,key=float,reverse=True)
cc = sorted(cc,key=float,reverse=True)
bc = sorted(bc,key=float,reverse=True)
clc = sorted(clc,key=float,reverse=True)
hc = sorted(hc,key=float,reverse=True)

#plotting degree centrality
plt.plot(np.arange(1,len(dc)+1,1),dc,'b.')
plt.xlabel('Rank')
plt.ylabel('Degree Centrality')
plt.savefig(sys.argv[1]+'.degree_plot.png')
plt.close()

#plotting closeness centrality
plt.plot(np.arange(1,len(cc)+1,1),cc,'b.')
plt.xlabel('Rank')
plt.ylabel('Closeness Centrality')
plt.savefig(sys.argv[1]+'.closeness_plot.png')
plt.close()

#plotting betweenness centrality
plt.plot(np.arange(1,len(bc)+1,1),bc,'b.')
plt.xlabel('Rank')
plt.ylabel('Betweenness Centrality')
plt.savefig(sys.argv[1]+'.betweenness_plot.png')
plt.close()

#plotting clustering coefficient
plt.plot(np.arange(1,len(clc)+1,1),clc,'b.')
plt.xlabel('Rank')
plt.ylabel('Clustering Coefficient')
plt.savefig(sys.argv[1]+'.clustering_plot.png')
plt.close()

#plotting harmonic closeness centrality
plt.plot(np.arange(1,len(hc)+1,1),hc,'b.')
plt.xlabel('Rank')
plt.ylabel('Harmonic Closness Centrality')
plt.savefig(sys.argv[1]+'.harmonic_plot.png')
plt.close()

print "The plot files are in\nfiles:"
print "\t",sys.argv[1]+".degree_plot.png"
print "\t",sys.argv[1]+".closeness_plot.png"
print "\t",sys.argv[1]+".harmonic_plot.png"
print "\t",sys.argv[1]+".betweenness_plot.png"
print "\t",sys.argv[1]+".clustering_plot.png"
print "respectively."
