#! /bin/bash
# Usage: ./run.sh robot start_index (should be 1 when starting from the beginning) onlyIndex|afterIndex algorithm planningTime

unset output
start_index=1
algorithm=""
endIndex=2
time=1000

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

if [ -z $3 ]
then
    echo "No index count provided"
    exit
fi

if [ $3 = "onlyIndex" ]
then
   endIndex=$start_index
   endIndex=$((endIndex+1))
fi

if [ -z $4 ]
then
    echo "No algorithm provided"
    exit 
fi

algorithm=$4 

if [ -z $5 ]
then
    echo "No planning time provided"
    exit 
fi

time=$5

echo "START INDEX $start_index"

for (( i=$start_index; i < $endIndex; i++ ))
do 
  echo "idx: $i, $i"
folder=mlmc
  #cd ${folder}
  #for variant in noCorrection bias correction pomcp
  for variant in correction
  do
  for ((a=0; a < 1; a++))
    do
    	echo "a: $a"
    	if [ -z "$output" ]
    	then      
    	  echo "Exec jobs_${algorithm}_${variant}_${robot}_${time}_${a}.sh"
    	  output=$(sbatch jobs_${algorithm}_${variant}_${robot}_${time}_${a}.sh)      
    	else
    	  echo "Exec jobs_${algorithm}_${variant}_${robot}_${time}_${a}.sh"
    	  output=$(sbatch --dependency=afterany:$jid jobs_${algorithm}_${variant}_${robot}_${time}_${a}.sh)
    	fi
    	jid=$(echo $output | tr -cd '[[:digit:]]')
    	echo "jobID: ${jid}"
    	sleep 0.1
    done
  done
  cd ..
   
done
