#! /bin/bash
jid=$(sbatch jobs_abt_dubin_0.sh)
for ((a=1; a <= 10 ; a++))
do
  jid=$(sbatch --dependency=afterany:$jid jobs_abt_dubin_$a.sh)    
done 

