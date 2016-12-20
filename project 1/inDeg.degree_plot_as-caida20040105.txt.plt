#
# Undirected graph - Degree Distribution. G(16301, 32955). 1561 (0.0958) nodes with in-deg > avg deg (4.0), 765 (0.0469) with >2*avg.deg (Fri Sep 23 20:13:20 2016)
#

set title "Undirected graph - Degree Distribution. G(16301, 32955). 1561 (0.0958) nodes with in-deg > avg deg (4.0), 765 (0.0469) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png size 1000,800
set output 'inDeg.degree_plot_as-caida20040105.txt.png'
plot 	"inDeg.degree_plot_as-caida20040105.txt.tab" using 1:2 title "" with linespoints pt 6
