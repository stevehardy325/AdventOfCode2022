
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip().split(' ') for l in fobj.readlines()]
    return data

directions = {'L': (-1, 0), 'R': (1, 0), 'U':(0,1), 'D':(0,-1)}

def getCloserToZeroByVal(n):
    if n == 0:
        return 0
    else:
        return (abs(n) - 1) * (n // abs(n))


def getNewTailPos(head_x, head_y, tail_x, tail_y):
    tail_dx = head_x - tail_x
    tail_dy = head_y - tail_y

    if tail_dx == 0 or tail_dy == 0 or (abs(tail_dx) == 1 and abs(tail_dy) == 1):
        tail_dy = getCloserToZeroByVal(tail_dy)
        tail_dx = getCloserToZeroByVal(tail_dx)
    else:
        tail_dy //= abs(tail_dy)
        tail_dx //= abs(tail_dx)

    tail_y += tail_dy
    tail_x += tail_dx
    return tail_x, tail_y


def process(data):
    sections = [[0,0] for i in range(10)]
    tail_places = set()
    tail_places.add((0,0))

    print('processing...')
    print(data)

    for move_dir_str, num_str in data:
        move_num = int(num_str)
        dx, dy = directions[move_dir_str]

        for i in range(move_num):
            sections[0][0] += dx
            sections[0][1] += dy

            for section_num in range(1, len(sections)):
                new_sec_pos = getNewTailPos(*sections[section_num - 1], *sections[section_num])
                sections[section_num] = list(new_sec_pos)
            tail_places.add(tuple(sections[-1]))

    return len(tail_places)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 1

    print('running for example ------')
    ex_data2 = get_input('example2.txt')
    ex_result2 = process(ex_data2)
    print('example result:')
    print(ex_result2)
    assert ex_result2 == 36

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    