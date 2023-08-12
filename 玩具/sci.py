#! python3
# findSciInfo - 通过剪贴板搜索文章的PMID号，杂志，年份与影响因子，粘贴到剪切板

import pyperclip, re

# 创建PMID正则
pmid_regex = re.compile(r'PMID: (\d+)')

# 创建影响因子、杂志与年份正则
magzine_year_regex = re.compile(r'''
    (\d+\.\d+)          # 影响因子
    \s                  # 影响因子与杂志间空格
    ([A-Za-z\s]+)# 杂志名称
    \r\n                  # 一般复制的时候会换行
    \.\s                # 年份前的多余
    (\d{4}             # 年份
)''',re.VERBOSE)

# 从剪贴板搜索相关内容
text = pyperclip.paste()

pmid = ''
magzazine = ''
year = ''
if_factor = ''

pmid_result = pmid_regex.search(text)
if pmid_result == None:
    print("未识别到PMID.")
else:
    pmid = pmid_result.group(1)
infor = magzine_year_regex.search(text)
if infor == None:
    print("未识别到杂志信息.")
else:
    magzazine = infor.group(2)
    year = infor.group(3)
    if_factor = infor.group(1)

# 将结果粘到剪贴板，以\t分隔便于贴到excel中
result = '\t'.join([pmid, magzazine, year, if_factor])
pyperclip.copy(result)
print('PMID: ' + pmid + ', 杂志: ' + magzazine + ', 年份：' + year +', IF:' + if_factor)