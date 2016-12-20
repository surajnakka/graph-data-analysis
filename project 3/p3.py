import snap

p=0.1
l = (101,1001,10001,100001,1000001)
for n in l:
	e = n*(n-1)/2
	e = int(e*p)
	print str(p)
	Graph = snap.GenRndGnm(snap.PUNGraph, n, e)
	p = p/10
	snap.SaveEdgeList(Graph,'randomgraph.meandegree.10.nodes.'+str(n)+'.elist.txt')