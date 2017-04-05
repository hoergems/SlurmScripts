#! /bin/bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd /data/hoe01h/Downloads/frapu/abt_stats/abt/bin
for NUM_OBSTACLES in 5 10 15 20 25 30 
do   
   for FOLDER in {1..10}
   do
       ./statsSerializer -p /datastore/hoe01h/WAFRJournal/randomScene/4DOF/collisionsNotAllowed/${NUM_OBSTACLES}_obstacles/$FOLDER
   done
done
