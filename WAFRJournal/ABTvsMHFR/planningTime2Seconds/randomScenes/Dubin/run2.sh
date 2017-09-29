#! /bin/bash
unset output
robot=""
algorithm=""

if [ -z $1 ]
then
    echo "No robot provided"
    exit    
fi

robot=$1

if [ -z $2 ]
then
    echo "No algorithm provided"
    exit    
fi

algorithm=$2

obst=0
for ((o=0; o < 6; o++))
do   
   obst=`expr $obst + 5`
   cd ${obst}_obstacles
   for ((a=0; a < 1; a++))
   do
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
     sleep 0.1
   done   
   cd ..
done
