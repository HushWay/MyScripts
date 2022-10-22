#! python3
# pw.py - 不安全的密码管理程序

import sys
import pyperclip

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'pseudoway@163.com': '' }

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # 第一个参数就是账号
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + '密码已复制到剪切板.')
else:
    print('没有' + account + '账号信息')