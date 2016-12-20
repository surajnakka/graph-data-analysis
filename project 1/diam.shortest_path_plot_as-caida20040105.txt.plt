#
# Undirected graph - shortest path. G(16301, 32955). Diam: avg:3.75  eff:4.56  max:10 (Fri Sep 23 20:13:35 2016)
#

set title "Undirected graph - shortest path. G(16301, 32955). Diam: avg:3.75  eff:4.56  max:10"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png size 1000,800
set output 'diam.shortest_path_plot_as-caida20040105.txt.png'
plot 	"diam.shortest_path_plot_as-caida20040105.txt.tab" using 1:2 title "" with linespoints pt 6
