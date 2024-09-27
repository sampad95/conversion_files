#!/bin/bash
for fl in POSCAR_*
do
# fl $fl
# echo fl
# echo "${fl%%-*}"
 echo "${fl##*_}"
for i in ${fl##*_}; do
 mkdir ad_$i;
 mv POSCAR_$i ad_$i/POSCAR;
 cp INCAR KPOINTS POTCAR ad_$i;
done
done
