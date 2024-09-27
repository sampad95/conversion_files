#!/bin/bash
for i in -0.06 -0.05 -0.04 -0.03 -0.02 -0.01 0.00 +0.01 +0.02 +0.03 +0.04 +0.05 +0.06; do
    mkdir ad_$i;
    cp INCAR KPOINTS POSCAR POTCAR ad_$i;
done
