# encoding:utf-8
# author:haozj 
# create_time: 2019/6/20
import itertools
#第一种方法
for i in itertools.permutations('xyz'):
    if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':
        print('a vs %s, b vs %s, c vs %s' % (i[0], i[1], i[2]))
#第二种方法
for a in range(ord('x'), ord('z') + 1):
    for b in range(ord('x'), ord('z') + 1):
        if a != b:
            for c in range(ord('x'), ord('z') + 1):
                if (a != c) and (b != c):
                    if (a != ord('x')) and (c != ord('x')) and (c != ord('z')):
                        print('a vs %s, b vs %s, c vs %s' % (chr(a), chr(b), chr(c)))
