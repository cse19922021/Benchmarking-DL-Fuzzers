import subprocess

TF_RELEASE_CUDA_MAP = {
    "2.11.0": "11.2",
    "2.10.0": "11.2",
    "2.9.0": "11.2",
    "2.8.0": "11.2",
    "2.7.0": "11.2",
    "2.6.0": "11.2",
    "2.4.0": "11.0",
    "2.3.0": "10.1",
}

TF_RELEASE_CUDNN_MAP = {
    "2.11.0": "11.2",
    "2.10.0": "11.2",
    "2.9.0": "11.2",
    "2.8.0": "8.1",
    "2.7.0": "8.1",
    "2.6.0": "8.1",
    "2.4.0": "8.0",
    "2.3.0": "7.6",
}

# Loop over TensorFlow releases
for tf_version, _ in TF_RELEASE_CUDA_MAP.items():

    env_name_tf = f"fuzzer_deeprel_tf_{tf_version}"
    shell_command = [
        "benchmarking/setup_and_run_tf_deep_rel.sh",
        env_name_tf,
        tf_version,
        "tensorflow",
    ]
    subprocess.call(
        shell_command,
        shell=False,
    )

    print("")
