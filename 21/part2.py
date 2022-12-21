import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def getNums(multiline_str: str):
    lines = []
    for line in multiline_str.splitlines():
        nums = re.search()


def getNum(monkeyName, monkeys):
    #print(monkeyName)
    if len(monkeys[monkeyName]) == 1:
        return int(monkeys[monkeyName][0])
    else:
        ops = {'*': lambda a, b: a*b,
               '-': lambda a, b: a-b, 
               '+': lambda a, b: a+b,
               '/': lambda a, b: a/b,
               '=': lambda a,b: a==b}
        n1 = getNum(monkeys[monkeyName][0], monkeys)
        n2 = getNum(monkeys[monkeyName][2], monkeys)
        op = ops[monkeys[monkeyName][1]]
        return op(n1, n2)

def getAsString(monkey, monkeys):
    base_str = ' '.join(monkeys[monkey])
    unexpanded =  re.findall('[a-z]{4}', base_str)
    for t in unexpanded:
        print(t)
        replacement = getAsString(t, monkeys)
        if 'x' not in replacement:
            replacement = str(int(eval(replacement)))
            base_str = re.sub(t, replacement, base_str)
        else:
            base_str = re.sub(t, '(' + replacement + ')', base_str)
    return base_str

    


def process(fname):
    print('processing...')
    lookup_table = {}
    lines = [l.split(': ') for l in open(fname).read().splitlines()]

    monkeys = {}
    for l in lines:
        monkeys[l[0]] = l[1].split(' ')
    
    monkeys['root'][1] = '='
    monkeys['humn'] = ['x']
        

    out_str = getAsString('root', monkeys)
    print(out_str)
    print(out_str[1])


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
