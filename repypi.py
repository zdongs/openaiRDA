import sys

input_file = "D:\\AI\\mbti_town\\generative_agents\\environment\\frontend_server\\requirements.txt"
output_file = "D:\\AI\\mbti_town\\generative_agents\\environment\\frontend_server\\requirements_temp.txt"

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        if line.startswith("https://pypi.python.org/simple"):
            line = line.replace("https://pypi.python.org/simple", "https://pypi.tuna.tsinghua.edu.cn/simple")
        outfile.write(line)

