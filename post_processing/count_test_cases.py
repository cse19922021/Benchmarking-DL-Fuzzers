import os, re


def read_txt(fname):
    with open(fname, "r") as fileReader:
        data = fileReader.read().splitlines()
    return data


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


def match_involved_API(_path):
    flag = False
    actual_API = read_txt(
        "/media/nimashiri/DATA/vsprojects/benchmarkingDLFuzzers/data/involved_APIs.txt"
    )
    for _api in actual_API:
        if re.findall(_api, _path):
            flag = True
    return flag


for root, dir, files in os.walk("/media/nimashiri/SSD/testing_results/FreeFuzz/torch"):
    tool = "FreeFuzz"
    for release in dir:
        current_release = os.path.join(root, release)
        lof = getListOfFiles(current_release)
        file_counter = 0
        for j, f in enumerate(lof):
            if tool == "FreeFuzz":
                if re.findall(r"(potential-bug)", f) or re.findall(
                    r"(FreeFuzz_bugs)", f
                ):
                    if match_involved_API(f):
                        file_counter = file_counter + 1
            else:
                if re.findall(r"((\/bug\/))", f) or re.findall(r"(\/neq\/)", f):
                    if match_involved_API(f):
                        file_counter = file_counter + 1
        print(f"Total number of PyTorch {release}: {file_counter}")
