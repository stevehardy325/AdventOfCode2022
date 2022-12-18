
from pprint import pprint


day_num = 'base'
ex_input_filename = '02_example.txt'
input_filename = '02_input.txt'

translations = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'lose', 'Y': 'draw', 'Z': 'win'}

win_list_loop = ['rock', 'paper', 'scissors']

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip().split(' ') for l in fobj.readlines()]
    return data

def getShapePoints(elf, me):
    idx = win_list_loop.index(elf)
    if me == 'lose':
        me_choice = idx - 1
    elif me == 'win':
        me_choice = idx + 1
    else:
        me_choice = idx
    me_points = me_choice % len(win_list_loop) + 1
    return me_points

def getMatchPoints(elf, me):
    elf = translations[elf]
    me = translations[me]

    if me == 'lose':
        outcome_points = 0
    elif me == 'draw':
        outcome_points = 3
    elif me == 'win':
        outcome_points = 6

    shape_points = getShapePoints(elf, me)
    return shape_points + outcome_points


def process(data):
    print('processing {}'.format(data))
    #pprint(data)
    results = [getMatchPoints(*d) for d in data]
    return sum(results)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result: {}'.format(ex_result))
    assert ex_result == 12
    input()

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('example result: {}'.format(real_result))


if __name__ == '__main__':
    main()

    