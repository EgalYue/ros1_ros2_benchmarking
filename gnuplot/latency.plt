set terminal postscript eps size 3.5,2.62 enhanced color
set output output
set datafile missing "NA"
set title title
set offset graph 0, 0, 0.1, 0
set yr [0:]
set ylabel "Latency [ms]"
set xlabel xlabel
set style line 1 lc rgb '#0060ad' lt 1 lw 2 pt 7 ps 1.5
plot input using 1:2:3 with yerrorbars ls 1 title "", "" using 1:2 w lines ls 1 title ""
