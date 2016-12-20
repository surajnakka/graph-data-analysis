#
# Undirected graph - shortest path. G(10876, 39994). Diam: avg:4.64  eff:5.41  max:10 (Fri Sep 23 19:38:56 2016)
#

set title "Undirected graph - shortest path. G(10876, 39994). Diam: avg:4.64  eff:5.41  max:10"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png size 1000,800
set output 'diam.shortest_path_plotp2p-Gnutella04.txt.png'
plot 	"diam.shortest_path_plotp2p-Gnutella04.txt.tab" using 1:2 title "" with linespoints pt 6
