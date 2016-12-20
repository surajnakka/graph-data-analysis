


import snap

Graph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor.elist.txt', 0, 1)
n = Graph.GetNodes()
p = float(Graph.GetEdges())/(n*(n-1)/2)

SumDeg = 0

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	SumDeg += item.Val2()
MeanDeg = SumDeg/n

BAGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_ba.elist.txt', 0, 1)
#BA Graph
print ""
print "------BA Graph-------"
#nodes
n = BAGraph.GetNodes()
print "Nodes:",n
#edges
print "Edges:",BAGraph.GetEdges()
#triads
NumTriads = snap.GetTriads(BAGraph,-1)  
print "Number of triads: "+str(NumTriads)
#params to generate graph
print "Params to graph: Mean node degree k",MeanDeg
#avg path length
alist = list()
i=0
for node in BAGraph.Nodes():
	avg = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(BAGraph,node.GetId(),ndh)
	for item in ndh:
		avg = avg + ndh[item]
	alist.append(avg/len(ndh))

print "Avg path length",float(sum(alist))/len(alist)
#diameter
diam = snap.GetBfsFullDiam(BAGraph, n, False)
print "diameter",diam
#avg clus cf
GraphClustCoeff = snap.GetClustCf (BAGraph, -1)
print "Avg Clustering Coefficient",GraphClustCoeff
#model specific metrics
