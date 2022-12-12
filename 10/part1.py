
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip().split(' ') for l in fobj.readlines()]
    return data

def process(data):
    print('processing...')
    print(data)
    cycle_num = 0
    x_val = 1
    samples = []
    for instruction_num in range(len(data)):
        instruction = data[instruction_num][0]
        if instruction == 'noop':
            cycle_num += 1
        elif instruction == 'addx':
            cycle_num += 1
        if (cycle_num - 20) % 40 == 0 and cycle_num <= 220:
            samples.append(x_val*cycle_num)
        if instruction == 'addx':
            cycle_num += 1
           
            if (cycle_num - 20) % 40 == 0 and cycle_num <= 220:
                samples.append(x_val*cycle_num)
            x_val += int(data[instruction_num][1])

            
        

    
    print(samples)
    return sum(samples)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 13140

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    
