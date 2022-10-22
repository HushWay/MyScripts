#! python3
# DownloadPapers 批量下载文献
# 参考：https://github.com/Tishacy/SciDownl/blob/v1.0/example/simple.py
# https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory

import os
import subprocess

# 根据需要存储的位置更改
current_dir = os.path.dirname(os.path.abspath(__file__))
paper_fn = os.path.join(current_dir, "papers.txt")
paper = open(paper_fn)
Lines = paper.readlines()
for line in Lines:
    source = line.strip().split("\t")
    subprocess.run(["scidownl", "download", "--"+source[2], source[0],
                    "--out", os.path.join(current_dir, "paper", source[1]+".pdf")])
