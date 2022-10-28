#! python3
# DownloadPapers 批量下载文献
import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
paper_fn = os.path.join(current_dir, "papers.txt")
paper = open(paper_fn)
Lines = paper.readlines()
for line in Lines:
    source = line.strip().split("\t")
    print(source)
    subprocess.run(["scidownl", "download", "--"+source[2], source[0],
                    "--out", os.path.join(current_dir, "paper", source[1]+".pdf")])
