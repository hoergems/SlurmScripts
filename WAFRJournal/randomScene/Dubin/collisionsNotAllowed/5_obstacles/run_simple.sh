#! /bin/bash
unset output
for ((a=0; a < 10 ; a++))
do
  if [ -z "$output" ]
  then
    output=$(sbatch jobs_abt_dubin_$a.sh)      
  else
    output=$(sbatch --dependency=afterok:$jid jobs_abt_dubin_$a.sh)
  fi
  jid=$(echo $output | tr -cd '[[:digit:]]')
done

