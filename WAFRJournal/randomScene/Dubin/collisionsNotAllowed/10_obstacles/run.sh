#! /bin/bash

for i in $(seq 10)
do
  cd $i
  jid=$(sbatch jobs_abt_dubin_$j.sh)
  for ((a=1; a <= 10 ; a++))
  do
    jid=$(sbatch --dependency=afterany:$jid jobs_abt_dubin_$a.sh)
    echo $?
  done  
  cd ..
done
