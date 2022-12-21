import re
import time

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
            # distribute
            if replacement == 'x':
                base_str = re.sub(t, replacement, base_str)
            else:
                base_str = re.sub(t, '(' + replacement + ')', base_str)                
    return base_str

    
def solve(eq_str):
    sides = eq_str.split('=')
    try:
        sides[0] = int(sides[0])
        intside = 0
        solve_side = 1
    except Exception as e:
        sides[1] = int(sides[1])
        intside = 1
        solve_side = 0
    
    while sides[solve_side].strip()  != 'x':
        #time.sleep(1)
        print('='.join([str(s) for s in sides]))
        working_str = sides[solve_side].strip()
        working_str = working_str[1:-1]
        sub_calc = re.findall('\(.*\)', working_str)
        if len(sub_calc) == 0:
            sub_calc = re.findall('x', working_str)
        working_str = working_str.replace(sub_calc[0], 'y')
        #print(working_str)
        a, op, b = working_str.split(' ')
        if op == '+':
            if a.isdigit():
                sides[intside] = '{} - {}'.format(sides[intside],int(a))
            else:
                sides[intside] = '{} - {}'.format(sides[intside],int(b))
        elif op == '-':
            if a.isdigit():
                sides[intside] = '-1 * ({} - {})'.format(sides[intside],int(a))
            else:
                sides[intside] = '{} + {}'.format(sides[intside],int(b))
        elif op == '*':
            if a.isdigit():
                sides[intside] = '{} / {}'.format(sides[intside],int(a))
            else:
                sides[intside] = '{} / {}'.format(sides[intside],int(b))
        elif op == '/':
            if a.isdigit():
                sides[intside] = '{} / {}'.format(int(a), sides[intside])
            else:
                sides[intside] = '{} * {}'.format(sides[intside],int(b)) #int(b) /sides[intside]
        sides[solve_side] = sub_calc[0]
        print('='.join([str(s) for s in sides]))
        sides[intside] = int(eval(sides[intside]))
        

        
    sides = [str(s) for s in sides]
    return '='.join(sides)

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
    #print(out_str)
    print(solve(out_str))


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
