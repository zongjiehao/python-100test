# encoding:utf-8
# author:haozj 
# create_time: 2019/6/20
import itertools

for i in itertools.permutations('xyz'):
    if i[0] != 'x' and i[2] != 'x' and i[2] != 'z':
        print('a vs %s, b vs %s, c vs %s' % (i[0], i[1], i[2]))