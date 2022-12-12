
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip().split(' ') for l in fobj.readlines()]
    return data

directions = {'L': (-1, 0), 'R': (1, 0), 'U':(0,1), 'D':(0,-1)}

def getCloserToZeroByVal(n, v):
    if n > 0:
        new_n= n -v
    elif n < 0:
        new_n = n+v
    else:
        new_n = 0
    return new_n

def getNewTailPos(head_x, head_y, tail_x, tail_y):
    tail_dx = head_x - tail_x
    tail_dy = head_y - tail_y

    if tail_dx == 0 or tail_dy == 0 or (abs(tail_dx) == 1 and abs(tail_dy) == 1):
        tail_dy = getCloserToZeroByVal(tail_dy, 1)
        tail_dx = getCloserToZeroByVal(tail_dx, 1)
    else:
        tail_dy = tail_dy // abs(tail_dy)
        tail_dx = tail_dx // abs(tail_dx)
        

    new_tail_y = tail_y + tail_dy
    new_tail_x = tail_x + tail_dx
    print('{},{}  {},{} -> {},{}'.format(head_x, head_y, tail_x, tail_y, new_tail_x, new_tail_y))
    return new_tail_x, new_tail_y

def process(data):
    head_x, head_y, tail_x, tail_y = 0,0,0,0
    tail_places = set()
    tail_places.add((tail_x, tail_y))
    print('processing...')
    print(data)
    for move_dir_str, num_str in data:
        move_num = int(num_str)
        dx, dy = directions[move_dir_str]
        for i in range(move_num):
            head_x += dx
            head_y += dy
            tail_x, tail_y = getNewTailPos(head_x, head_y, tail_x, tail_y)
            tail_places.add((tail_x, tail_y))
    print(tail_places)
    return len(tail_places)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 13

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    