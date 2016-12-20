#
# Undirected graph - shortest path. G(50000, 255750). Diam: avg:4.48  eff:4.94  max:7 (Fri Sep 23 19:41:22 2016)
#

set title "Undirected graph - shortest path. G(50000, 255750). Diam: avg:4.48  eff:4.94  max:7"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png size 1000,800
set output 'diam.shortest_path_plotsteam-sweden-sample.txt.png'
plot 	"diam.shortest_path_plotsteam-sweden-sample.txt.tab" using 1:2 title "" with linespoints pt 6
