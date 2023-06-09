import pandas as pd
import csv
import os
import re

cwd = os.getcwd()

REG = re.compile("Processing file:")


def read_txt(fname):
    with open(fname, "r") as fileReader:
        data = fileReader.read().splitlines()
    return data


def decompose_detections(splitted_lines):
    super_temp = []
    j = 0
    indices = []
    while j < len(splitted_lines):
        if REG.search(splitted_lines[j]):
            indices.append(j)
        j += 1

    if len(indices) == 1:
        for i, item in enumerate(splitted_lines):
            if i != 0:
                super_temp.append(item)
        super_temp = [super_temp]
    else:
        i = 0
        j = 1
        while True:
            temp = []
            for row in range(indices[i], indices[j]):
                temp.append(splitted_lines[row])
            super_temp.append(temp)
            if j == len(indices) - 1:
                temp = []
                for row in range(indices[j], len(splitted_lines)):
                    temp.append(splitted_lines[row])
                super_temp.append(temp)
                break
            i += 1
            j += 1

    return super_temp


def main():
    for root, dir, files in os.walk(
        "logs/"
    ):
        root = "logs"
        for tool in ["DeepRel"]:
            current_tool = os.path.join(root, tool)
            for lib in ["torch"]:
                current_lib = os.path.join(current_tool, lib)
                for f in sorted(os.listdir(current_lib), key=len):
                    current_file = os.path.join(current_lib, f)
                    data = read_txt(current_file)
                    decomposed_logs = decompose_detections(data)

                    release = f.replace(".txt", "")

                    mydata = []
                    for i, log in enumerate(decomposed_logs):
                        decomposed_log_path = log[0].split("/")
                        API_name = [
                            item
                            for item in decomposed_log_path
                            if re.search(r"(torch\.)", item)
                            or re.search(r"(tf\.)", item)
                            or re.search(r"(tensorflow\.)", item)
                        ]

                        log = "\n".join(log)

                        if API_name:
                            if re.findall(f"(\+torch\.)", API_name[0]) or re.findall(
                                f"(\+tf\.)", API_name[0]
                            ):
                                pass
                            else:
                                API_name[0] = API_name[0].replace(".py", "")

                            mydata = mydata + [[API_name[0], log]]

                        else:
                            mydata = mydata + [["NoName", log]]

                    for item in mydata:
                        if not os.path.exists(
                            f"results/{tool}/{lib}/"
                        ):
                            os.makedirs(
                                f"results/{tool}/{lib}/"
                            )
                        with open(
                            f"results/{tool}/{lib}/DetectionMat_{release}.csv",
                            "a",
                            newline="\n",
                        ) as fd:
                            writer_object = csv.writer(fd)
                            writer_object.writerow(item)


if __name__ == "__main__":
    main()
