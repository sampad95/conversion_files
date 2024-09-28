#!/bin/bash
#for fl in ad_*
#do
# echo "${fl##*_}"
#vi Evsdisp.dat
#for i in ${fl##*_}; do
#  grep "free  energy" ad_$i/OUTCAR|awk '{print $5}'
 
#done
#done


for i in -0.06 -0.05 -0.04 -0.03 -0.02 -0.01 0.0 0.01 0.02 0.03 0.04 0.05 0.06; do
  echo -n $i 
  grep "free  energy" ad_$i/OUTCAR|awk '{print "  " $5}'
done
