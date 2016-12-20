import snap

Graph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor.elist.txt', 0, 1)


WSGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_ws.elist.txt', 0, 1)

n = Graph.GetNodes()
p = float(Graph.GetEdges())/(n*(n-1)/2)

SumDeg = 0

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	SumDeg += item.Val2()
MeanDeg = SumDeg/n
#WS Graph
print "------WS Graph-------"
#nodes
n = WSGraph.GetNodes()
print "Nodes:",n
#edges
print "Edges:",WSGraph.GetEdges()
#triads
NumTriads = snap.GetTriads(WSGraph,-1)  
print "Number of triads: "+str(NumTriads)
#params to generate graph
print "Params to graph: Mean node degree k",MeanDeg
#avg path length
alist = list()
i=0
for node in WSGraph.Nodes():
	avg = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(WSGraph,node.GetId(),ndh)
	for item in ndh:
		avg = avg + ndh[item]
	alist.append(avg/len(ndh))

print "Avg path length",float(sum(alist))/len(alist)
#diameter
diam = snap.GetBfsFullDiam(WSGraph, n, False)
print "diameter",diam
#avg clus cf
GraphClustCoeff = snap.GetClustCf (WSGraph, -1)
print "Avg Clustering Coefficient",GraphClustCoeff

