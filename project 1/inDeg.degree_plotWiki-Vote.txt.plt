#
# Undirected graph - Degree Distribution. G(7115, 100762). 1871 (0.2630) nodes with in-deg > avg deg (28.3), 1141 (0.1604) with >2*avg.deg (Fri Sep 23 19:17:16 2016)
#

set title "Undirected graph - Degree Distribution. G(7115, 100762). 1871 (0.2630) nodes with in-deg > avg deg (28.3), 1141 (0.1604) with >2*avg.deg"
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
set output 'inDeg.degree_plotWiki-Vote.txt.png'
plot 	"inDeg.degree_plotWiki-Vote.txt.tab" using 1:2 title "" with linespoints pt 6
