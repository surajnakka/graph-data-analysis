import snap
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

#graph loading
Graph1 = snap.LoadEdgeList(snap.PUNGraph,'myrecipe.elist.txt', 0, 1)
Graph2 = snap.LoadEdgeList(snap.PUNGraph,'South-America_recipes.elist.txt', 0, 1)
Graph3 = snap.LoadEdgeList(snap.PUNGraph,'American_recipes.elist.txt', 0, 1)
Graph4 = snap.LoadEdgeList(snap.PUNGraph,'India_recipes.elist.txt', 0, 1)

#metrics
#1. Eigen Vector Centrality - most influencing ingredients
#2. Degree Centrality - most used ingredients

#Graph1

eigen1 = set()
degree1 = set()

#Eigen Vector Centrality - Graph1
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(Graph1, NIdEigenH)

maxd = 0.0
maxnode = 0
for node in NIdEigenH:
	if maxd<NIdEigenH[node]:
		maxd = NIdEigenH[node]
		maxnode = node
	eigen1.add(NIdEigenH[node])

print "Max Eigen node ->",maxnode
print "Max Eigen Value ->",maxd
#Degree Centrality - Graph1
maxd = 0.0
maxnode = 0
for node in Graph1.Nodes():

	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph1, node.GetId())
	degree1.add(DegCentr)
	if maxd < DegCentr:
		maxd = DegCentr
		maxnode = node.GetId()

fp = open('myrecipe.names.txt')
for i in fp.readlines():
	ar = i.rstrip('\n').split('\t')
	if int(ar[0]) == maxnode:
		print "Max. Degree Centrality Node in 'My Recipes' network is ",maxnode," : ",ar[1]," with centrality: ",maxd
		print "i.e.,",ar[1],"ingredient is used ",round(maxd*100,2),"% of the time in My Recipes network\n"
fp.close()
#Graph2

eigen2 = set()
degree2 = set()

#Eigen Vector Centrality - Graph2
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(Graph2, NIdEigenH)

maxd = 0.0
maxnode = 0
for node in NIdEigenH:
	if maxd<NIdEigenH[node]:
		maxd = NIdEigenH[node]
		maxnode = node
	eigen2.add(NIdEigenH[node])

print "Max Eigen node ->",maxnode
print "Max Eigen Value ->",maxd
#Degree Centrality - Graph2
maxd = 0.0
maxnode = 0
for node in Graph2.Nodes():

	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph2, node.GetId())
	degree2.add(DegCentr)
	if maxd < DegCentr:
		maxd = DegCentr
		maxnode = node.GetId()

fp = open('South-America_recipes.names.txt')
fp.readline()
for i in fp.readlines():
	ar = i.rstrip('\n').split(' ')
	if int(ar[0]) == maxnode:
		print "Max. Degree Centrality Node in 'South-America Recipes' network is ",maxnode," : ",ar[1]," with centrality: ",maxd
		print "i.e.,",ar[1],"ingredient is used ",round(maxd*100,2),"% of the time in South-America Recipes network\n"
fp.close()

#Graph3

eigen3 = set()
rank3 = set()
degree3 = set()

#Eigen Vector Centrality - Graph3

NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(Graph3, NIdEigenH)

maxd = 0.0
maxnode = 0
for node in NIdEigenH:
	if maxd<NIdEigenH[node]:
		maxd = NIdEigenH[node]
		maxnode = node
	eigen3.add(NIdEigenH[node])

print "Max Eigen node ->",maxnode
print "Max Eigen Value ->",maxd


#Degree Centrality - Graph3
maxd = 0.0
maxnode = 0
for node in Graph3.Nodes():

	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph3, node.GetId())
	degree3.add(DegCentr)
	if maxd < DegCentr:
		maxd = DegCentr
		maxnode = node.GetId()

fp = open('American_recipes.names.txt')
fp.readline()
for i in fp.readlines():
	ar = i.rstrip('\n').split(' ')
	if int(ar[0]) == maxnode:
		print "Max. Degree Centrality Node in 'American_recipes' network is ",maxnode," : ",ar[1]," with centrality: ",maxd
		print "i.e.,",ar[1],"ingredient is used ",round(maxd*100,2),"% of the time in American_recipes network\n"
fp.close()

#Graph4

eigen4 = set()
rank4 = set()
degree4 = set()

#Eigen Vector Centrality - Graph4
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(Graph4, NIdEigenH)

maxd = 0.0
maxnode = 0
for node in NIdEigenH:
	if maxd<NIdEigenH[node]:
		maxd = NIdEigenH[node]
		maxnode = node
	eigen4.add(NIdEigenH[node])

print "Max Eigen node ->",maxnode
print "Max Eigen Value ->",maxd


#Degree Centrality - Graph4
maxd = 0.0
maxnode = 0
for node in Graph4.Nodes():

	#degree centrality
	DegCentr = snap.GetDegreeCentr(Graph4, node.GetId())
	degree4.add(DegCentr)
	if maxd < DegCentr:
		maxd = DegCentr
		maxnode = node.GetId()

fp = open('India_recipes.names.txt')
fp.readline()
for i in fp.readlines():
	ar = i.rstrip('\n').split(' ')
	if int(ar[0]) == maxnode:
		print "Max. Degree Centrality Node in 'India_recipes' network is ",maxnode," : ",ar[1]," with centrality: ",maxd
		print "i.e.,",ar[1],"ingredient is used ",round(maxd*100,2),"% of the time in India_recipes network\n"
fp.close()

#sort by decreasing centrality for ranking

#Graph1 
eigen1 = sorted(eigen1,key=float,reverse=True)
degree1 = sorted(degree1,key=float,reverse=True)

#Graph2 
eigen2 = sorted(eigen2,key=float,reverse=True)
degree2 = sorted(degree2,key=float,reverse=True)

#Graph3 
eigen3 = sorted(eigen3,key=float,reverse=True)
degree3 = sorted(degree3,key=float,reverse=True)

#Graph4
eigen4 = sorted(eigen4,key=float,reverse=True)
degree4 = sorted(degree4,key=float,reverse=True)



#eigen plot
plt.plot(np.arange(1,len(eigen1)+1,1),eigen1,'bo',label='My recipes')
plt.plot(np.arange(1,len(eigen2)+1,1),eigen2,'ro',label='South_america recipes')
plt.plot(np.arange(1,len(eigen3)+1,1),eigen3,'go',label='American recipes')
plt.plot(np.arange(1,len(eigen4)+1,1),eigen4,'yo',label='Indian recipes')
plt.legend()

plt.xlabel('Rank')
plt.ylabel('Eigen Vector Centrality')
plt.savefig('compare.eigen_plot.png')
plt.close()


#Degree Centrality plot
plt.plot(np.arange(1,len(degree1)+1,1),degree1,'bo',label='My recipes')
plt.plot(np.arange(1,len(degree2)+1,1),degree2,'ro',label='South_america recipes')
plt.plot(np.arange(1,len(degree3)+1,1),degree3,'go',label='American recipes')
plt.plot(np.arange(1,len(degree4)+1,1),degree4,'yo',label='Indian recipes')
plt.legend()

plt.xlabel('Rank')
plt.ylabel('Degree Centrality')
plt.savefig('compare.degree_centrality_plot.png')
plt.close()

print "The Correlation plots are in\nMetrics:"
print "\tEigen Vector Centrality: compare.eigen_plot.png"
print "\tDegree Centrality: compare.degree_centrality_plot.png"
