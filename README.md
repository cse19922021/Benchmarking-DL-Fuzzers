# Benchmarking-DL-Fuzzers
This is the source repository of the paper titled "Benchmarking Deep Learning (DL) Fuzzers", which is submitted to the 38th IEEE/ACM International Conference on Automated Software Engineering (ASE 2023).

# About
The aim of this study is to assess the effectiveness of three advanced Deep Learning (DL) fuzzers, namely FreeFuzz, DeepRel, and DocTer, on two commonly used open-source DL libraries: PyTorch and TensorFlow. The evaluation involves running the fuzzers on various versions of the DL libraries, starting from the earliest releases up to the latest ones. The study analyzes the outcomes and identifies the reasons behind any undetected bugs, proposing enhancements to the fuzzers.

# Warning

It is highly recommended that to use UNIX-based operating systems to test and run Orion, preferebly ubuntu-22.04.

FreeFuzz, DeepRel, and DocTer are test case generation tools that may harm SUT. They may generate test cases that freez or halt your operating system. Take extreme cautios when running them.

# Requirements
You need the following dependencies to be able to run the fuzzers:
```
requests
pandas
numpy
pymongo
anaconda
```
[FreeFuzz](https://github.com/ise-uiuc/FreeFuzz), [DeepRel](https://github.com/ise-uiuc/DeepREL), and [DocTer](https://github.com/lin-tan/DocTer) also need their own dependencies, please visit their home page to install the dependencies.

# Bug collection
First, you need to mine issues from Github repository of PyTorch and TensorFlow libraries. If you want to use our data, please jump to the next section. 
To collect issues, you need four github access tokens. To collect PyTorch issues, run the following script:

```
python github mining/collect_issues_torch.py
```
To collect TensorFlow issues, run:
```
python github mining/collect_issues_tf.py
```
Please put your github access tokens at the top of the previous scripts after the import statements. You can access our mined issues for [PyTorch](https://github.com/cse19922021/Benchmarking-DL-Fuzzers/blob/main/github%20mining/issues/pytorch.csv) and [TensorFlow](https://github.com/cse19922021/Benchmarking-DL-Fuzzers/blob/main/github%20mining/issues/tensorflow.csv).

# Manual Analysis
We performed manual analysis on the collected issues in two major rounds. We resolved the disagreements in multiple rounds to get the final data to run the DL fuzzers. The following Table shows the disagreement rates:

| Library    | Round 1 #samples | Round 1 disagreement (%) | Round 2 #samples | Round 2 disagreement (%) | Final fuzzable samples |
|------------|------------------|-------------------------|------------------|---------------------------|------------------------|
| PyTorch    | 728              | 27.6                    | 429              | 0.02                      | 400                    |
| TensorFlow | 146              | 19.1                    | 58               | 0.01                      | 235                    |

You can access the step by step data in the following [link](https://docs.google.com/spreadsheets/d/1cT6vbF36_x9YXmk1XK1LKSNJEdscLXd36wTMmMe-3zU/edit?usp=sharing).

# Running the fuzzers

For example, if you want to run DeepRel on TensorFlow releases, just execute the following command:
```
python exec_tf_deeprel.py
```
Do not directly run the bash scripts, you need to run the Python scripts. 
