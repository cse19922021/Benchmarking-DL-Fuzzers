import sys, os, re, subprocess


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


if __name__ == "__main__":
    pt_version = sys.argv[1]
    library = sys.argv[2]
    root_file_addr = sys.argv[3]
    env_name_pt = sys.argv[4]

    lof = getListOfFiles(root_file_addr)
    for j, f in enumerate(lof):
        if re.findall(r"((\/bug\/))", f) or re.findall(r"(\/neq\/)", f):
            shell_command = [
                "/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/benchmarking/exec.sh",
                env_name_pt,
                pt_version,
                "torch",
                f,
            ]
            subprocess.call(
                shell_command,
                shell=False,
            )
