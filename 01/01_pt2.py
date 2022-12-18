
day_num = 'base'
ex_input_filename = '01_example.txt'
input_filename = '01_input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        text = fobj.read()
        elves = text.split('\n\n')
        
    return elves

def getSum(elf):
    total = 0
    items = elf.split('\n')
    
    for i in items:
        total += int(i)
    return total

def process(elves):
    print('processing {}'.format(elves))

    totals = [getSum(e) for e in elves]
    totals.sort(reverse=True)
    top_three = totals[0:3]

    highest_three_sum = sum(top_three)
        
    return highest_three_sum


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result: {}'.format(ex_result))
    assert ex_result == 45000

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('final result: {}'.format(real_result))
    #assert real_result == 20


if __name__ == '__main__':
    main()

    