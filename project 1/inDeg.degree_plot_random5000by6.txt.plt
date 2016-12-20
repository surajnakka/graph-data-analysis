#
# Undirected graph - Degree Distribution. G(834, 347361). 0 (0.0000) nodes with in-deg > avg deg (833.0), 0 (0.0000) with >2*avg.deg (Fri Sep 23 20:01:35 2016)
#

set title "Undirected graph - Degree Distribution. G(834, 347361). 0 (0.0000) nodes with in-deg > avg deg (833.0), 0 (0.0000) with >2*avg.deg"
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
set output 'inDeg.degree_plot_random5000by6.txt.png'
plot 	"inDeg.degree_plot_random5000by6.txt.tab" using 1:2 title "" with linespoints pt 6
