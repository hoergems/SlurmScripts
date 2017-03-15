#! /bin/bash

output=$(sbatch jobs_abt_dubin_1.sh)
jid=$(echo $output | tr -cd '[[:digit:]]')
echo $jid

output=$(sbatch --dependency=afterok:$jid jobs_abt_dubin_2.sh)
jid1=$(echo $output | tr -cd '[[:digit:]]')
echo $jid

