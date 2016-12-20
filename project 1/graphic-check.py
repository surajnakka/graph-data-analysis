import sys

length = len(sys.argv)

if length==1 :
	print "Please enter a file"
	sys.exit()
elif length==2 :	
	input_file = sys.argv[1]
else:
	print "Please enter only one file"
	sys.exit()

file = open(input_file,'r')
degreeseq = file.readlines()
degreeseq = map(int, degreeseq)
oddcount = 0
flag = 0
nodes = len(degreeseq)

for i in range(nodes):
	if degreeseq[i]%2!=0:
		oddcount += 1
	if degreeseq[i]>(nodes-1):
		flag=1



if sum(degreeseq)%2!=0:
	print input_file+" is NOT a graphic degree sequence. It fails test 'Sum of degree sequence should be even'."
elif oddcount%2!=0:
	print input_file+" is NOT a graphic degree sequence. It fails test 'Number of odd degree nodes should be even'."
elif flag==1:
	print input_file+" is NOT a graphic degree sequence. It fails test 'No node should have degree greater than n-1'."
else:
	test = "Havel-Hakimi theorem"
	while len(degreeseq)>=2:
		if degreeseq[len(degreeseq)-1] < 0:
			print input_file+" is NOT a graphic degree sequence. It fails test "+test 
			sys.exit()

		if len(degreeseq)==2:
			if (degreeseq[0]==0 and degreeseq[1]==0) or (degreeseq[0]==1 and degreeseq[1]==1):
				print input_file+" is a graphic degree sequence."
				sys.exit()
			else:
				print input_file+" is NOT a graphic degree sequence. It fails test "+test 
				sys.exit()

		head = degreeseq.pop(0)
		if head > len(degreeseq):
			print input_file+" is NOT a graphic degree sequence. It fails test "+test 
			sys.exit()

		for i in range(head):
			degreeseq[i] = degreeseq[i]-1

		degreeseq.sort(reverse=True)
		