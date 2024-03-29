# Benchmarking-DL-Fuzzers

This is the artifact of the research paper, **Benchmarking Deep Learning Fuzzers**, submitted at ICSE 2024.

## About 
In recent years, fuzzing Deep Learning (DL) libraries have garnered significant attention in the software engineering community. Many DL fuzzers have been proposed to generate malformed inputs to test DL APIs. Although most of these fuzzers have been demonstrated to be effective in detecting bugs and outperform their respective prior work in finding more or different bugs, there remains a gap in benchmarking these DL fuzzers regarding their effectiveness against ground-truth real-world bugs in DL libraries. Since the existing comparisons among these DL fuzzers mainly focus on comparing bugs detected by them, they cannot provide a direct, in-depth evaluation of different DL fuzzers.

In this work, we set out to conduct the first ground-truth empirical evaluation of state-of-the-art DL fuzzers. Specifically, we first manually created an extensive DL bug benchmark dataset, which includes 627 real-world DL bugs from TensorFlow and PyTorch libraries reported by users between 2020 and 2022. Then we run three state-of-the-art DL fuzzers, i.e., FreeFuzz, DeepRel, and DocTer, on the benchmark by following their instructions. We find that these fuzzers are unable to detect many real bugs collected in our benchmark dataset. Specifically, most (235) of the 257 applicable bugs cannot be detected by any fuzzer.

Our systematic analysis further identifies four major, broad, and common factors that affect these fuzzers' ability to detect real bugs. These findings present opportunities to improve the performance of the fuzzers in future work. As a proof of concept, we propose a lightweight corner case generator as an extension to the three DL fuzzers, which simply covers several boundary values as well as DL-specific data types. It helps FreeFuzz, DeepRel, and DocTer detect 12, 12, and 14 more bugs, respectively, that were overlooked by the original fuzzers. Overall, this work complements prior studies on DL fuzzers with an extensive performance evaluation and provides a benchmark for future DL library fuzzing studies. Also, our proposed corner case generator proves that the fuzzers can be extended to detect more bugs by extending their internal fuzzing logic based on the insights provided in root cause analysis.

## Directory structure

- benchmarking DL fuzzers/
    - benchmarking/
        - exec.sh
        - exec_tf_deeprel.py
        - exec_tf_docter.py
        - exec_tf_freefuzz.py
        - exec_torch_deeprel.py
        - exec_torch_docter.py
        - exec_torch_freefuzz.py
        - run_deep_rel_tests.py
        - setup_and_run_pt.sh
        - setup_and_run_tf.sh
        - setup_and_run_tf_deep_rel.sh
        - setup_and_run_tf_docter.sh
        - setup_and_run_torch_deep_rel.sh
        - setup_and_run_torch_docter.sh
    - data/
        - overlap_tf.csv
        - overlap_torch.csv
        - tf_data.csv
        - torch_data.csv
    - database_analysis/
        - db_analysis.py
    - fuzzers/
    - github mining/
        - issues
          - pytorch.csv
          - tensorflow.csv 
        - collect_commits.py
        - collect_issues_tf.py
        - collect_issues_torch.py
        - mine_comments.py
    - post_processing
      - concat.py
      - count_test_cases.py
      - log_parser.py 
    - utils
      - releases.py   
    - README.md
    - gitignore
    - fuzzers-download-link

## TensorFlow and PyTorch issues
The mined issues for [TensorFlow](https://github.com/cse19922021/Benchmarking-DL-Fuzzers/blob/main/github%20mining/issues/tensorflow.csv) and [PyTorch](https://github.com/cse19922021/Benchmarking-DL-Fuzzers/blob/main/github%20mining/issues/pytorch.csv) are available under ```github mining/issues/```.

## Workflow data
Based on issues, we conducted the manual analysis as explained in ***Section 2.4***.
Our workflow data is available at [here](https://docs.google.com/spreadsheets/d/1cT6vbF36_x9YXmk1XK1LKSNJEdscLXd36wTMmMe-3zU/edit?usp=sharing).

## Testcase generation

### Running DocTer

To run DocTer, you need to download the modified version which is available [here](https://drive.google.com/file/d/1TbQn2HEyIbKVVT8H_GDZPkV_0PNu5N7-/view?usp=sharing)

Then, you need to replace the directory named **all_constr** with the following directory which is available [here](https://drive.google.com/file/d/1ZnF2KwIojsBffrnw_Lxb5AIgCvKBBQ4h/view?usp=sharing)

Once you replaced the constraints, you can run the following scripts:

To run DocTer on TensorFlow releases:
```
python benchmarking/exec_tf_docter.py
```
To run DocTer on PyTorch releases:
```
python benchmarking/exec_torch_docter.py
```

### Running FreeFuzz and DeepRel

#### Step 1

In order to run the fuzzers, please first download them from [here](https://github.com/cse19922021/Benchmarking-DL-Fuzzers/blob/main/fuzzers-download-link) and extract the zip filers under **fuzzers**
directory.

#### Step 2

Once you downloaded the fuzzers, you need to cd to the **benchmarking** directory and run the corresponding shell script files.

Once you copy and extract the zip files:

To run FreeFuzz on TensorFlow releases:
```
python benchmarking/exec_tf_freefuzz.py
```
To run FreeFuzz on PyTorch releases:
```
python benchmarking/exec_torch_freefuzz.py
```
To run DeepRel on PyTorch releases:
```
python benchmarking/exec_tf_deeprel.py
```
To run DeepRel on TensorFlow releases:
```
python benchmarking/exec_torch_deeprel.py
```
