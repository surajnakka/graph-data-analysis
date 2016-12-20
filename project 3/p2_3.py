import snap

Graph = snap.LoadEdgeList(snap.PUNGraph,'G1.edgelist', 0, 1)

ERGraph = snap.LoadEdgeList(snap.PUNGraph,'G2.edgelist', 0, 1)

WSGraph = snap.LoadEdgeList(snap.PUNGraph,'G3.edgelist', 0, 1)

BAGraph = snap.LoadEdgeList(snap.PUNGraph,'G4.edgelist', 0, 1)

snap.PlotOutDegDistr(Graph, "G1", "degree Distribution")

snap.PlotOutDegDistr(ERGraph, "G2", "degree Distribution")

snap.PlotOutDegDistr(WSGraph, "G3", "degree Distribution")

snap.PlotOutDegDistr(BAGraph, "G4", "degree Distribution")