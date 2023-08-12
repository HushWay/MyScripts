#! python3
# commentLines.py - 在剪贴板内容前面加上#号
import pyperclip
text = pyperclip.paste()
# 分开每行加#号
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '# ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)