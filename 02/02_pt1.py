
day_num = 'base'
ex_input_filename = '02_example.txt'
input_filename = '02_input.txt'

translations = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip().split(' ') for l in fobj.readlines()]
    return data

def getOutcomePoints(elf, me):
    if me == elf:
        points = 3
    elif (me == 'rock' and elf == 'paper') or (me == 'paper' and elf == 'scissors') or (me == 'scissors' and elf == 'rock'):
        points = 0 # loss
    else:
        points = 6 # win
    return points

def getMatchPoints(elf, me):
    elf = translations[elf]
    me = translations[me]

    if me == 'rock':
        shape_points = 1
    elif me == 'paper':
        shape_points = 2
    elif me == 'scissors':
        shape_points = 3

    outcome_points = getOutcomePoints(elf, me)
    return shape_points + outcome_points


def process(data):
    print('processing {}'.format(data))
    results = [getMatchPoints(*d) for d in data]
    return sum(results)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result: {}'.format(ex_result))
    assert ex_result == 15

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('example result: {}'.format(real_result))


if __name__ == '__main__':
    main()

    