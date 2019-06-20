score = int(input('请输入分数:'))
if score >= 90:
    grade = 'A'
elif 90>score >= 60:
    grade = 'B'
else:
    grade = 'C'

print('%d 属于 %s' % (score, grade))
