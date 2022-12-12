
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [[int(i) for i in l.strip()] for l in fobj.readlines()]
    return data

def isVisibleDirection(data, x, y, dx, dy):
    height = data[y][x]
    x_view = x + dx
    y_view = y + dy
    while x_view >= 0 and x_view < len(data[0]) and y_view >= 0 and y_view < len(data):
        if data[y_view][x_view] >= height:
            return False
        x_view += dx
        y_view += dy

    return True

def isVisible(data, x, y):
    directions = [(-1, 0), (1,0), (0, 1), (0, -1)]
    for d in directions:
        dx, dy = d
        if isVisibleDirection(data, x, y, dx, dy):
            return True
    return False
        
                



def process(data):
    print('processing...')
    print(data)
    c = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if isVisible(data, x, y):
                c += 1
                print(x, y)
            


    return c


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    assert isVisible(ex_data, 3,1) == False

    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 21

    input()
    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    