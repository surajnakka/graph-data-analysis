#
# Undirected graph - Degree Distribution. G(10876, 39994). 4554 (0.4187) nodes with in-deg > avg deg (7.4), 1339 (0.1231) with >2*avg.deg (Fri Sep 23 19:38:40 2016)
#

set title "Undirected graph - Degree Distribution. G(10876, 39994). 4554 (0.4187) nodes with in-deg > avg deg (7.4), 1339 (0.1231) with >2*avg.deg"
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
set output 'inDeg.degree_plotp2p-Gnutella04.txt.png'
plot 	"inDeg.degree_plotp2p-Gnutella04.txt.tab" using 1:2 title "" with linespoints pt 6
