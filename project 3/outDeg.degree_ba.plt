#
# degree Distribution. G(17577, 561936). 4515 (0.2569) nodes with out-deg > avg deg (63.9), 1150 (0.0654) with >2*avg.deg (Mon Oct 31 20:49:25 2016)
#

set title "degree Distribution. G(17577, 561936). 4515 (0.2569) nodes with out-deg > avg deg (63.9), 1150 (0.0654) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png size 1000,800
set output 'outDeg.degree_ba.png'
plot 	"outDeg.degree_ba.tab" using 1:2 title "" with linespoints pt 6
