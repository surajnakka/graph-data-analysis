#
# Undirected graph - shortest path. G(7115, 100762). Diam: avg:3.25  eff:3.78  max:7 (Fri Sep 23 19:18:09 2016)
#

set title "Undirected graph - shortest path. G(7115, 100762). Diam: avg:3.25  eff:3.78  max:7"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png size 1000,800
set output 'diam.shortest_path_plotWiki-Vote.txt.png'
plot 	"diam.shortest_path_plotWiki-Vote.txt.tab" using 1:2 title "" with linespoints pt 6
