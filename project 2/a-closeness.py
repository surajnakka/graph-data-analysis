
import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt

input_file = sys.argv[1]
SubGraph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)


cc = set()
closeness = dict()


Graph = snap.GetMxScc(SubGraph)

for node in Graph.Nodes():
	print node.GetId()
	Clcentr = snap.GetClosenessCentr(Graph, node.GetId())
	closeness[node.GetId()] = Clcentr
