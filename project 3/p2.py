import snap
import sys

#load graph
input_file = sys.argv[1]

Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)

n = Graph.GetNodes()
e = Graph.GetEdges()
SumDeg = 0

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	SumDeg += item.Val2()
MeanDeg = SumDeg/n

#ER Graph
ERGraph = snap.GenRndGnm(snap.PUNGraph, n, e)
snap.SaveEdgeList(ERGraph,'USairport_2010_er.elist.txt')

#WS Graph
WSGraph = snap.GenSmallWorld(n, MeanDeg, 0.12)
snap.SaveEdgeList(WSGraph,'USairport_2010_ws.elist.txt')

#BA Graph
BAGraph = snap.GenPrefAttach(n, MeanDeg)
snap.SaveEdgeList(BAGraph,'USairport_2010_ba.elist.txt')