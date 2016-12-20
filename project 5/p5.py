import snap
import sys
import math
import matplotlib
matplotlib.use('Agg')

length = len(sys.argv)

import matplotlib.pyplot as plt

import numpy as np

#checking if input is correctly given
if length==1 :
	print "Please enter a file"
	sys.exit()
elif length==2 :	
	input_file = sys.argv[1]
else:
	print "Please enter only one file"
	sys.exit()

#loading the graph given
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)

labels = snap.TIntStrH()
for NI in Graph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
snap.DrawGViz(Graph, snap.gvlDot, "output.png", " ", labels)