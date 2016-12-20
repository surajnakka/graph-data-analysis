import snap

Graph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor.elist.txt', 0, 1)

ERGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_er.elist.txt', 0, 1)

WSGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_ws.elist.txt', 0, 1)

BAGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_ba.elist.txt', 0, 1)

#nodes
#edges
#triads
#params to generate graph
#avg path length
#diameter
#avg clus cf
#model specific metrics
n = Graph.GetNodes()
p = float(Graph.GetEdges())/(n*(n-1)/2)

SumDeg = 0

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	SumDeg += item.Val2()
MeanDeg = SumDeg/n
#Main Graph
print "------Original Graph-------"
#nodes
n = Graph.GetNodes()
print "Nodes:",n
#edges
print "Edges:",Graph.GetEdges()
#triads
NumTriads = snap.GetTriads(Graph,-1)  
print "Number of triads: "+str(NumTriads)
#params to generate graph
print "Params to graph: Original Graph"
#avg path length
alist = list()
i=0
for node in Graph.Nodes():
	avg = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(Graph,node.GetId(),ndh)
	for item in ndh:
		avg = avg + ndh[item]
	alist.append(avg/len(ndh))
print "Avg path length",float(sum(alist))/len(alist)
#diameter
diam = snap.GetBfsFullDiam(Graph, n, False)
print "diameter",diam
#avg clus cf
GraphClustCoeff = snap.GetClustCf (Graph, -1)
print "Avg Clustering Coefficient",GraphClustCoeff
#model specific metrics

#ER Graph
print ""
print "------ER Graph-------"
#nodes
n = ERGraph.GetNodes()
print "Nodes:",n
#edges
print "Edges:",ERGraph.GetEdges()
#triads
NumTriads = snap.GetTriads(ERGraph,-1)  
print "Number of triads: "+str(NumTriads)
#params to generate graph
print "Params to graph: probability p = ",p
#avg path length
alist = list()
i=0
for node in ERGraph.Nodes():
	avg = 0.0
	ndh = snap.TIntH()
	snap.GetShortPath(ERGraph,node.GetId(),ndh)
	for item in ndh:
		avg = avg + ndh[item]
	alist.append(avg/len(ndh))

print "Avg path length",float(sum(alist))/len(alist)
#diameter
diam = snap.GetBfsFullDiam(ERGraph, n, False)
print "diameter",diam
#avg clus cf
GraphClustCoeff = snap.GetClustCf (ERGraph, -1)
print "Avg Clustering Coefficient",GraphClustCoeff
#model specific metrics

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
#model specific metrics

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
