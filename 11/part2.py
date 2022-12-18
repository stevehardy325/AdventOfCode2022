
from math import prod


ex_input_filename = 'example.txt'
input_filename = 'input.txt'



def process(fname):
    print('processing...')
    data = open(fname).read().split('\n\n')
    print(data)
    monkeys = []
    for m_chunk in data:
        lines = [l.strip() for l in m_chunk.split('\n')]
        monkey_num = int(lines[0][-2])
        monkey_items = [int(s) for s in lines[1][16:].split(', ')]
        monkey_op = lines[2][17:]
        test_val = int(lines[3][19:])
        true_target = int(lines[4][25])
        false_target = int(lines[5][26])
        print(monkey_num)
        print(monkey_items)
        print(monkey_op)
        print(test_val)
        print(true_target)
        print(false_target)

        monkeys.append([monkey_items, monkey_op, test_val, true_target, false_target])

    counts = [0 for i in monkeys]
    for roundnum in range(10000):
        for monkey_num in range(len(monkeys)):
            monkey =  monkeys[monkey_num]
            while len(monkey[0]) > 0:
                counts[monkey_num] += 1
                old = monkey[0].pop(0)
                ew = eval(monkey[1])
                #ew //= 3
                ew %= prod([m[2] for m in monkeys])
                if ew % monkey[2] == 0:
                    target_monkey_num = monkey[3]
                else:
                    target_monkey_num = monkey[4]
                monkeys[target_monkey_num][0].append(ew)
                    
            





    
    print(counts)
    counts.sort(reverse=True)
    print(counts[0] * counts[1])



def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()

    
