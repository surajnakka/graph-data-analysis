import snap
import math
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

e=math.exp(-10)



input_file = 'randomgraph.meandegree.10.nodes.1001.elist'
Graph = snap.LoadEdgeList(snap.PUNGraph,input_file, 0, 1)
i=0
j=0
n = Graph.GetNodes()
DegToCntV = snap.TIntPrV()
snap.GetDegCnt(Graph, DegToCntV)
for item in DegToCntV:
	k = item.GetVal1()
	if i==0:
		plt.plot(k,float(item.GetVal2())/n,'b.',label = 'Probability Distribution')
		i = i+1
	else:
		plt.plot(k,float(item.GetVal2())/n,'b.')
	y = e*pow(10,k)
	kfac = math.factorial(k)
	y = float(y)/kfac
	if j==0:
		plt.plot(k,y,'r+',label = 'Poisson Distribution')
		j = j+1
	else:
		plt.plot(k,y,'r+')

plt.xlabel('Degree k')
plt.ylabel('Probability of degree k/Poisson Distribution')
plt.legend()
plt.savefig('distr+1001.png')
plt.close()


