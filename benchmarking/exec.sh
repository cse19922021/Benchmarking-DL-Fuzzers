#!/bin/bash

env_name=$1
pt_version=$2
library=$3
target=$4

source /home/nimashiri/anaconda3/etc/profile.d/conda.sh
conda activate "$env_name"

python $target

source /home/nimashiri/anaconda3/etc/profile.d/conda.sh
conda deactivate
