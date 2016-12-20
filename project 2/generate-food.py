import snap
import sys

fp = open('allr_recipes.txt')
namelist = open('myrecipe.names.txt','w+')
edgelist = open('myrecipe.elist.txt','w+')

names = []
resultlist = []
namesd = dict()
id = 1
for i in fp.readlines():
    ar = i.rstrip('\n').split('\t')
    if ar[0] == 'Mexico' or ar[0] == 'Italy' or ar[0] == 'Eastern-Europe':
        #print ar[1:len(ar)]
        for item1 in ar[1:len(ar)]:
            if item1 not in names:
                names.append(item1)
                namesd[item1] = id
                id += 1
        for item1 in ar[1:len(ar)]:
            myindex = ar.index(item1)
            newlist = ar[1:myindex]+ar[myindex+1:]   #make a new temp list without the item1 in it
            for item2 in newlist:
                mytuple = (namesd[item1], namesd[item2])
                backtuple = (namesd[item2], namesd[item1])
                if backtuple not in resultlist: #remove any reversed duplicates
                    resultlist.append(mytuple)

for key, value in sorted(namesd.iteritems(), key=lambda (k,v): (v,k)):
    namelist.write(str(value)+'\t'+key+'\n')
for i in resultlist:
    edgelist.write(str(i[0])+' '+str(i[1])+'\n')
fp.close()
nameslist.close()
edgelist.close()
