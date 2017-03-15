#! /bin/bash
jid1=$(sbatch jobs_abt_dubin_1.sh)
echo $jid1
jid2=$(sbatch --dependency=afterok:$jid1 jobs_abt_dubin_2.sh)


