#! /bin/bash
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
for ((a=0; a < 6; a++))
do
   obst=`expr $obst + 5`
   cd ${obst}_obstacles
   ./run.sh $robot 1 afterIndex $algorithm
   cd ..
done
