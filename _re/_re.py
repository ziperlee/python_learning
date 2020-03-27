"""
 Created by liwei on 2019/12/20.
"""

import re

line = "Cats are smarter than dogs"


# match 重字符串起始位置匹配
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

print("matchObj.group() : ", matchObj.group())
print("matchObj.group(1) : ", matchObj.group(1))
print("matchObj.group(2) : ", matchObj.group(2))


# search 字符串内查找匹配
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

print("searchObj.group() : ", searchObj.group())
print("searchObj.group(1) : ", searchObj.group(1))
print("searchObj.group(2) : ", searchObj.group(2))


# pattern
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')


if __name__ == '__main__':
    pattern = re.compile(r'^\d+$')
    print(pattern.match('122'))
    print(pattern.search('122'))