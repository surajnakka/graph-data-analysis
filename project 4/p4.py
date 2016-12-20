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

n = Graph.GetNodes()

#declaring required lists
degl = list()   #degree sequence list
cuml = list()   #stores cumulative number of nodes greater than k
countdl = list() #stores count of each degree
ddl = list()  #stores distinct degree values


#obtaining degree sequence
result_degree = snap.TIntV()
snap.GetDegSeqV(Graph, result_degree)
for i in range(0, result_degree.Len()):
    degl.append(result_degree[i])


#obtaining degree count for each degree
DegToCntV = snap.TIntPrV()
snap.GetDegCnt(Graph, DegToCntV)
for item in DegToCntV:
	countdl.append(item.GetVal2())
	ddl.append(item.GetVal1())


#plot 8.3

#considering only till 60 bins, since further will make graph right-skewed
if str(input_file) == 'imdb_actor.elisr.txt':
	degl2 = [i for i in degl if i <= 180]
	plt.hist(degl2,bins=180,normed=1,alpha = 0.5)
else:
	degl2 = [i for i in degl if i <= 60]
	plt.hist(degl2,bins=60,normed=1,alpha = 0.5)
plt.xlabel('Degree k')
plt.ylabel('Fraction Pk of vertices having Degree k')
plt.title('Degree Distribution Plot')
plt.savefig(input_file+'_plot1.png')
plt.close()


#plot 8.5
#log scale histogram generation
m = max(degl)
#Num of bins should be equal to no of distinct degrees, in this way each distinct degree gets one bin each
plt.hist(degl,bins=m,normed = 1,alpha = 0.5,log=True)
plt.xscale('log', nonposy='clip')
plt.xlabel('Degree k')
plt.ylabel('Fraction Pk of vertices having Degree k')
plt.title('Degree Distribution on Logarithmic Scale')
plt.savefig(input_file+'_plot2.png')
plt.close()

#plot 8.6
#logarithmic binning
m = max(degl) #identify the max degree since we only require logarithmic range till max degree

#initialize bin range
b = (range(0,1,1))
i=1

#this loop runs and adds the log range till max is in between the logarithmic range
while True:
	if m>= pow(2,i) and m<= pow(2,i+1):
		b = b + range(pow(2,i),pow(2,i+1)-1,pow(2,i))
		break
	else:
		b = b + range(pow(2,i),pow(2,i+1)-1,pow(2,i))		
	i = i+1

plt.hist(degl,bins=b,normed=1,alpha = 0.5,log=True)
plt.xscale('log', nonposy='clip')
plt.xlabel('Degree k')
plt.ylabel('Fraction Pk of vertices having Degree k')
plt.title('Degree Distribution on log scale with Logarithmic binning')
plt.savefig(input_file+'_plot3.png')
plt.close()

#plot 8.7
#cumulative distribution
s = 0

#compute the cumulative degree count list
for item in countdl:
	cuml.append(float(n-s)/n)
	s = s+item

plt.loglog(ddl,cuml,basex=10)
plt.xlabel('Degree k')
plt.ylabel('Fraction Pk of vertices having Degree k or greater')
plt.title('Cumulative Degree Distribution on log scale')
plt.savefig(input_file+'_plot4.png')
plt.close()

#calculating alpha
a = 0

#considering kmin=4 for imdb_actors
if str(input_file) == 'imdb_actor.elisr.txt':
	for i in degl[3:]:
		ki = float(i)/3.5
		a = a + math.log(ki)
	a = 1/float(a)
	N = n - (countdl[0]+countdl[1]+countdl[2])
else:
	for i in degl:
		ki = float(i)/0.5
		a = a + math.log(ki)
	a = 1/float(a)
	N = n
#considering kmin=1 for as19981010.txt
a = a*N
a = 1 + a

print ""
print "Alpha = ",a

#calculating sigma (statistical error)

sig = a-1
rtN = math.sqrt(N)
sig = sig/rtN

print "Statistical error = ",sig

print ""

print "The plots are in"
print "Plot 1 : "+input_file+"_plot1.png"
print "Plot 2 : "+input_file+"_plot2.png"
print "Plot 3 : "+input_file+"_plot3.png"
print "Plot 4 : "+input_file+"_plot4.png"