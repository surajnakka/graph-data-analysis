import matplotlib
matplotlib.use('Agg')


import matplotlib.pyplot as plt


file1 = open('Steam-Sweden.txt.degree.txt','r')
file2 = open('Steam-Sweden.txt.closeness.txt','r')
file3 = open('Steam-Sweden.txt.harmonic.txt','r')
file4 = open('Steam-Sweden.txt.betweenness.txt','r')
file5 = open('Steam-Sweden.txt.clustering.txt','r')

dd = dict()
cd = dict()
hd = dict()
bd = dict()
cld = dict()

dl = list()
cl = list()
hl = list()
bl = list()
cll = list()


for x in file1.readlines():
	line = x.rstrip('\n').split(' : ')
	dd[int(line[0])] = line[1]

for x in file2.readlines():
	line = x.rstrip('\n').split(' : ')
	cd[int(line[0])] = line[1]

for x in file3.readlines():
	line = x.rstrip('\n').split(' : ')
	hd[int(line[0])] = line[1]

for x in file4.readlines():
	line = x.rstrip('\n').split(' : ')
	bd[int(line[0])] = line[1]

for x in file5.readlines():
	line = x.rstrip('\n').split(' : ')
	cld[int(line[0])] = line[1]





for item in sorted(dd):
	dl.append(dd[item])
	cl.append(cd[item])
	hl.append(hd[item])
	bl.append(bd[item])
	cll.append(cld[item])



plt.plot(dl,cl,'b.')
plt.savefig('Steam_scatter_d vs cl.png')
plt.close()

plt.plot(dl,hl,'b.')
plt.savefig('Steam_scatter_d vs hl.png')
plt.close()

plt.plot(dl,bl,'b.')
plt.savefig('Steam_scatter_d vs bl.png')
plt.close()

plt.plot(dl,cll,'b.')
plt.savefig('Steam_scatter_d vs cll.png')
plt.close()

plt.plot(cl,hl,'b.')
plt.savefig('Steam_scatter_cl vs hl.png')
plt.close()

plt.plot(cl,bl,'b.')
plt.savefig('Steam_scatter_cl vs bl.png')
plt.close()

plt.plot(cl,cll,'b.')
plt.savefig('Steam_scatter_cl vs cll.png')
plt.close()


plt.plot(hl,bl,'b.')
plt.savefig('Steam_scatter_hl vs bl.png')
plt.close()

plt.plot(hl,cll,'b.')
plt.savefig('Steam_scatter_hl vs cll.png')
plt.close()

plt.plot(bl,cll,'b.')
plt.savefig('Steam_scatter_bl vs cll.png')
plt.close()

