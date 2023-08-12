#! python3
# mapIt.py - 使用浏览器打开命令行或者剪贴板地址

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # 从命令行取地址
    address = ' '.join(sys.argv[1:])
else:
    # TODO: 从剪贴板获取地址
    address = pyperclip.paste()

print(address)
webbrowser.open('https://www.amap.com/search?query=' + address)