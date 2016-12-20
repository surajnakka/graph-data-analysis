import snap


n = 1000
e = n*(n-1)/2
p = 0.65
e = int(e*p)
SumDeg = 0
#problem1
#1
Graph = snap.GenRndGnm(snap.PUNGraph, n, e)

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	SumDeg += item.Val2()
MeanDeg = SumDeg/n
a = pow(MeanDeg,3)/6

TriadV = snap.TIntTrV()
snap.GetTriads(Graph, TriadV,-1)
OpenTriads = 0
ClosedTriads = 0

for triple in TriadV:
	OpenTriads += triple.Val3()
	ClosedTriads += triple.Val2()

ClosedTriads = ClosedTriads/3
TotalTriads = (3.0*ClosedTriads)+OpenTriads
GlobalClcf = (3.0*ClosedTriads)/TotalTriads

print 'number of nodes:',n
print 'number of edges',e
print 'number of open tri %d closed tri %d total tri %d'%(OpenTriads,ClosedTriads,TotalTriads)
print 'Clustering coefficient',GlobalClcf
print 'mean deg:',MeanDeg
print '1(a)',a
print '1(b)(i)',(n*pow(MeanDeg,2))/2
print '2(b)(ii)',float(MeanDeg)/(n-1)
#2
#n = 1000
#e = ((n*(n-1))/2)*0.75
#Graph = snap.GenRndGnm(snap.PUNGraph, n, e)
#3

#Rnd = snap.TRnd(1,0)
#UGraph1 = snap.GenSmallWorld(10, 3, 1, Rnd)