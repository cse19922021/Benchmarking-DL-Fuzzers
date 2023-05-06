#!/bin/bash

declare -A pyversion
pyversion["1.13.0"]="3.9"
pyversion["1.12.0"]="3.9"
pyversion["1.11.0"]="3.9"
pyversion["1.10.1"]="3.9"
pyversion["1.10.0"]="3.9"
pyversion["1.9.1"]="3.9"
pyversion["1.9.0"]="3.9"
pyversion["1.8.2"]="3.9"
pyversion["1.8.1"]="3.9"
pyversion["1.8.0"]="3.9"
pyversion["1.7.1"]="3.9"
pyversion["1.7.0"]="3.7"
pyversion["1.6.0"]="3.7"
pyversion["1.5.1"]="3.7"
pyversion["1.5.0"]="3.7"
pyversion["1.4.0"]="3.7"
pyversion["1.1.0"]="3.7"
pyversion["1.0.0"]="3.7"

env_name=$1
pt_version=$2
library=$3
setup_command=$4

conda create --name $env_name python=${pyversion[$pt_version]} -y

source /home/anaconda3/etc/profile.d/conda.sh
conda activate "$env_name"

$setup_command

pip install pandas
pip install pymongo
pip install textdistance
pip install munkres
pip install tensorflow

# python /media/DATA/vsprojects/benchmarkingDLFuzzers/fuzzers/DeepREL/pytorch/src/DeepREL.py $pt_version $library

ROOT_DIR="outdir/$pt_version"

for dir in $(find "$ROOT_DIR" -type d); do
    if echo "$dir" | grep -Eq "neq" || echo "$dir" | grep -Eq "bug"; then
        find "$dir" -type f | while read file
        do
            find "$file" -name "*.py" -exec sh -c 'echo "Processing file: $1"; python "$1"' sh {} \; |& tee -a "/media/DATA/vsprojects/benchmarkingDLFuzzers/logs/DeepRel/torch/$pt_version.txt";
        done
    fi
done

# python /media/DATA/vsprojects/benchmarkingDLFuzzers/benchmarking/run_deep_rel_tests.py $pt_version $library $ROOT_DIR $env_name

source /home/anaconda3/etc/profile.d/conda.sh
conda deactivate

conda env remove --name $env_name -y
