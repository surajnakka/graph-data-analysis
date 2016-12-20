import snap
import sys
import math

length = len(sys.argv)

if length==1 :
	print "Please enter a file"
	sys.exit()
elif length==2 :	
	input_file = sys.argv[1]
else:
	print "Please enter only one file"
	sys.exit()


if input_file=="random5000by6.txt":
	#create random graph
	Graph = snap.GenRndGnm(snap.PUNGraph, 5000, 5000*(5000-1)/2)
	V = snap.TIntV()
	for i in range(5000):
   		if (i%6!=0):
			V.Add(i)
	snap.DelNodes(Graph, V)
	snap.SaveEdgeList(Graph, 'random5000by6.txt')
else:
	Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)

nodes = snap.CntNonZNodes(Graph)
nodes0 = snap.CntDegNodes(Graph, 0)
final_nodes = nodes+nodes0
edges = snap.CntUniqUndirEdges(Graph)
nodes7 = snap.CntDegNodes(Graph, 7)
DegToCntV = snap.TIntPrV()
snap.GetDegCnt(Graph, DegToCntV)
vector_length = len(DegToCntV)
maxdegreencount = DegToCntV[vector_length-1].GetVal2()

#for item in DegToCntV:
   	# print "%d nodes with degree %d" % (item.GetVal2(), item.GetVal1())
print ""
print "Number of nodes in "+input_file+": ",final_nodes
print "Number of edges in "+input_file+": ",edges
print "Number of nodes with degree=7 in "+input_file+": ",nodes7
print "Node id(s) with highest degree in "+input_file+": ",
for i in range(maxdegreencount):
	NodeId = snap.GetMxDegNId(Graph)
	V1 = snap.TIntV()
	V1.Add(NodeId)
	snap.DelNodes(Graph, V1)
	print str(NodeId)+",",
print ""

Graph1 = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)
snap.PlotInDegDistr(Graph1, "degree_plot_"+input_file, "Undirected graph - Degree Distribution")
print "Degree distribution of "+input_file+" is in: inDeg.degree_plot_"+input_file+".png"
print ""

diameter = [0,0,0]
index = 0
for i in [10,100,1000]:
	diameter[index] = snap.GetBfsFullDiam(Graph1, i, False)
	print "Approx. diameter in "+input_file+" with sampling ",i," nodes: ",diameter[index]
	index = index+1

mean = float(sum(diameter)/3.0)
variance = float((pow((diameter[0]-mean),2)+pow((diameter[1]-mean),2)+pow((diameter[2]-mean),2))/2.0)

print "Approx. diameter in "+input_file+" (mean and variance): ",round(mean,3),", ",round(variance,3)

print ""

diameter = [0,0,0]
index = 0
for i in [10,100,1000]:
	diameter[index] = snap.GetBfsEffDiam(Graph1, i, False)
	print "Approx. effective diameter in "+input_file+" with sampling ",i," nodes: ",round(diameter[index],3)
	index = index+1

mean = float(sum(diameter)/3.0)
variance = float((pow((diameter[0]-mean),2)+pow((diameter[1]-mean),2)+pow((diameter[2]-mean),2))/2.0)

print "Approx. effective diameter in "+input_file+" (mean and variance): ",round(mean,3),", ",round(variance,3)

snap.PlotShortPathDistr(Graph1, "shortest_path_plot_"+input_file, "Undirected graph - shortest path",1000)
print "Shortest path distribution of "+input_file+" is in: diam.shortest_path_plot_"+input_file+".png"

largest_component = snap.TCnComV()
snap.GetSccs(Graph1, largest_component)
largest = 0.0

for item in largest_component:
	if largest < item.Len():
		largest = item.Len()

print ""

print "Fraction of nodes in largest connected component in "+input_file+": ", float(largest)/float(final_nodes)

snap.PlotSccDistr(Graph1, "conn_components_plot_"+input_file, "Undirected graph - Connected components distribution")
print "Component size distribution of "+input_file+" is in: scc.conn_components_plot_"+input_file+".png"