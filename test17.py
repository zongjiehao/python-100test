str = input("请输入一串字符:")
letter = 0
space = 0
number = 0
other = 0
for s in str:
    if s.isalpha():
        letter +=1
    elif s.isspace():
        space += 1
    elif s.isdigit():
        number += 1
    else:
        other +=1
print('字符中共有%d个字母,%d个空格,%d个数字,%d个其他字符'%(letter,space,number,other))