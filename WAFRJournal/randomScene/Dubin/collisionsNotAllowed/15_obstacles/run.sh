#! /bin/bash
# Usage: ./run.sh robot start_index (should be 1 when starting from the beginning) algorithm

unset output
start_index=1
algorithm=""

if [ -z $1 ]
then
    echo "No robot provided"
    exit    
fi

robot=$1

if [ -z $2 ]
then
    echo "No start index provided"
    exit
fi

start_index=$2

#if [ $# -eq 0 ]
#then
#   echo "No robot provided"
#   exit
#else
#   robot=$1
#fi

#if [ $2 != "" ] 
#then
#    start_index=$2
#fi

if [ -z $3 ]
then
    echo "No algorithm provided"
    exit 
fi

algorithm=$3 

echo "START INDEX $start_index"

for (( i=$start_index; i < 11; i++ ))
do  
  echo "idx: $i"
  cd $i
  for ((a=0; a < 5; a++))
  do
    echo "a: $a"
    if [ -z "$output" ]
    then      
      echo "Exec jobs_${algorithm}_${robot}_${a}.sh"
      output=$(sbatch jobs_${algorithm}_${robot}_${a}.sh)      
    else
      echo "Exec jobs_${algorithm}_${robot}_${a}.sh"
      output=$(sbatch --dependency=afterany:$jid jobs_${algorithm}_${robot}_${a}.sh)
    fi
    jid=$(echo $output | tr -cd '[[:digit:]]')
    echo "jobID: ${jid}"
  done
  cd ..
done
