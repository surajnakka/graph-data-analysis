#
# Undirected graph - Degree Distribution. G(50000, 255750). 13200 (0.2640) nodes with in-deg > avg deg (10.2), 6061 (0.1212) with >2*avg.deg (Fri Sep 23 19:43:17 2016)
#

set title "Undirected graph - Degree Distribution. G(50000, 255750). 13200 (0.2640) nodes with in-deg > avg deg (10.2), 6061 (0.1212) with >2*avg.deg"
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
set output 'inDeg.degree_plot_steam-sweden-sample.txt.png'
plot 	"inDeg.degree_plot_steam-sweden-sample.txt.tab" using 1:2 title "" with linespoints pt 6
