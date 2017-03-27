#! /bin/bash

unset output
start_index=1
robot=""

if [ $# -eq 0 ]
then
   echo "No robot provided"
   exit
else
   robot=$1
fi

if [ $2 != "" ] 
then
    start_index=$2
fi

echo "START INDEX $start_index"

for (( i=$start_index; i < 11; i++ ))
do  
  cd $i
  for ((a=0; a < 5; a++))
  do
    if [ -z "$output" ]
    then      
      echo "Exec jobs_abt_${robot}_${a}.sh"
      output=$(sbatch jobs_abt_${robot}_${a}.sh)      
    else
      output=$(sbatch --dependency=afterok:$jid jobs_abt_${robot}_${a}.sh)
    fi
    jid=$(echo $output | tr -cd '[[:digit:]]')
  done
  cd ..
done
