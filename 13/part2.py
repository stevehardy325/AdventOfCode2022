import functools
from string import ascii_letters
from collections import defaultdict

import sys
sys.setrecursionlimit(10000)

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def compare(l1, l2, nestlevel=0):
    #print('{}{} vs {}'.format(' '*nestlevel, l1, l2))
    
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        elif l1 == l2:
            return 0
        else:
            return 1
    elif isinstance(l1, list) and isinstance(l2, list):
        if l1 == [] and l2 == []:
            return 0
        for i in range(len(l1)):
            if i >= len(l2):
                return 1
            comp_res = compare(l1[i], l2[i])
            if comp_res != 0:
                return comp_res
        return -1
    elif isinstance(l1, int) and isinstance(l2, list):
        return compare([l1], l2,nestlevel=nestlevel+1)
    elif isinstance(l2, int) and isinstance(l1, list):
        return compare(l1, [l2],nestlevel=nestlevel+1)


def process(fname):
    #print('processing...')
    data = [l.strip() for l in open(fname).readlines() if l != '\n'] + ['[[2]]'] + ['[[6]]'] 
    #print(data)
    str_cmp = lambda s1, s2: compare(eval(s1), eval(s2))
    data.sort(key=functools.cmp_to_key(str_cmp))
    #print('\n'.join(data), )
    print((data.index('[[2]]') + 1) * (data.index('[[6]]') + 1))


def main():
    print('running for example ------')
    process(ex_input_filename)
    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
