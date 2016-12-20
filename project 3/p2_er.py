

import snap

Graph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor.elist.txt', 0, 1)


ERGraph = snap.LoadEdgeList(snap.PUNGraph,'imdb_actor_er.elist.txt', 0, 1)


n = Graph.GetNodes()
p = float(Graph.GetEdges())/(n*(n-1)/2)
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