#!/bin/bash
#PBS -N vasp_std
#PBS -l nodes=1:ppn=20
#PBS -q user5
cd $PBS_O_WORKDIR
export FI_PROVIDER=tcp

for fl in ad_*
do
 echo "${fl##*_}"
for i in ${fl##*_}
	do
		cd ad_$i
#		ln -sf ../INCAR
#		ln -sf ../KPOINTS
#		ln -sf ../POTCAR
		mpirun -np 20 vasp_std > vasp.out 
		cd ..
	done 
done
