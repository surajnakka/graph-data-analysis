import snap 

Rnd = snap.TRnd(1,0)
Graph = snap.GenSmallWorld(1000, 5, 0.12, Rnd)

snap.SaveEdgeList(Graph, 'mygraph.txt')

