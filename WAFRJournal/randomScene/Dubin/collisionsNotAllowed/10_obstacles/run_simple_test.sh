#! /bin/bash
jid1=$(sbatch jobs_abt_dubin_1.sh)
jid2=$(sbatch --dependency=afterany:$jid1 jobs_abt_dubin_2.sh)


