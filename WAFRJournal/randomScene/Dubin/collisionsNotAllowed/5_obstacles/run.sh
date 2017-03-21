#! /bin/bash

unset output
start_index=1

if [ $1 != "" ] 
then
    start_index=$1
fi

for (( i=$start_index; i < 11; i++ ))
do  
  cd $i
  for ((a=0; a < 5; a++))
  do
    if [ -z "$output" ]
    then
      output=$(sbatch jobs_abt_dubin_$a.sh)      
    else
      output=$(sbatch --dependency=afterok:$jid jobs_abt_dubin_$a.sh)
    fi
    jid=$(echo $output | tr -cd '[[:digit:]]')
  done
  cd ..
done
