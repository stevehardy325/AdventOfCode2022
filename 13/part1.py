from string import ascii_letters
from collections import defaultdict

import sys
sys.setrecursionlimit(10000)

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def compare(l1, l2, nestlevel=0):
    print('{}{} vs {}'.format(' '*nestlevel, l1, l2))
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        else:
            return l1 < l2
    elif isinstance(l1, list) and isinstance(l2, list):
        if l1 == [] and l2 == []:
            return None
        for i in range(len(l1)):
            if i >= len(l2):
                return False
            comp_res = compare(l1[i], l2[i])
            if comp_res is not None:
                return comp_res
        return True
    elif isinstance(l1, int) and isinstance(l2, list):
        return compare([l1], l2,nestlevel=nestlevel+1)
    elif isinstance(l2, int) and isinstance(l1, list):
        return compare(l1, [l2],nestlevel=nestlevel+1)


def process(fname):
    print('processing...')
    data = [l.split('\n') for l in open(fname).read().split('\n\n')]

    count = 0
    goods = []
    for i in range(len(data)):
        print('input #{}'.format(i))
        lst_str_pair = data[i]
        l1, l2 = [eval(l) for l in lst_str_pair]
    
        if compare(l1, l2):
            print('GOOD')
            count += i + 1
            goods.append(i+1)
        else:
            print('BAD')
    print(goods)
    print(count)



def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
