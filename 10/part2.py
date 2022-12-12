
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def process(fname):
    print('processing...')
    data = [l.strip().split(' ') for l in open(fname).readlines()]
    cycle_num, x_val = 0, 1
    samples = []
    
    overlaps=lambda cycle, x: cycle_num % 40 in range(x-1, x+2)
    
    for instruction_num in range(len(data)):
        instruction = data[instruction_num][0]
        samples.append(overlaps(cycle_num, x_val))
        cycle_num += 1

        if instruction == 'addx':
            samples.append(overlaps(cycle_num, x_val))
            x_val += int(data[instruction_num][1])
            cycle_num += 1

    pixels = {True: '█', False:'-'}
    screen = [ pixels[i] for i in samples]
    for i in range(len(screen) // 40):
        print(''.join(screen[40*(i):40*(i+1)]))


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()

    
