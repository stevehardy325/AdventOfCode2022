import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def getNums(multiline_str: str):
    lines = []
    for line in multiline_str.splitlines():
        nums = re.search()


def getNum(monkeyName, monkeys):
    print(monkeyName)
    if len(monkeys[monkeyName]) == 1:
        return int(monkeys[monkeyName][0])
    else:
        ops = {'*': lambda a, b: a*b,
               '-': lambda a, b: a-b, 
               '+': lambda a, b: a+b,
               '/': lambda a, b: a/b}
        n1 = getNum(monkeys[monkeyName][0], monkeys)
        n2 = getNum(monkeys[monkeyName][2], monkeys)
        op = ops[monkeys[monkeyName][1]]
        return op(n1, n2)


def process(fname):
    print('processing...')
    lookup_table = {}
    lines = [l.split(': ') for l in open(fname).read().splitlines()]

    monkeys = {}
    for l in lines:
        monkeys[l[0]] = l[1].split(' ')
        print(l)
    print(monkeys['dvpt'])

    print(getNum('root', monkeys))


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
