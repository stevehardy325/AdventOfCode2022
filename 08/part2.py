
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [[int(i) for i in l.strip()] for l in fobj.readlines()]
    return data

def getViewDistDir(data, x, y, dx, dy):
    height = data[y][x]
    x_view = x + dx
    y_view = y + dy
    count = 0
    while x_view >= 0 and x_view < len(data[0]) and y_view >= 0 and y_view < len(data):
        count += 1

        if data[y_view][x_view] >= height:
            break
        x_view += dx
        y_view += dy
    return count

def getScenic(data, x, y):
    directions = [(-1, 0), (1,0), (0, 1), (0, -1)]
    views = []
    for d in directions:
        dx, dy = d
        views.append(getViewDistDir(data, x, y, dx, dy))
    
    return views[0] * views[1] * views[2] * views[3]
        
                



def process(data):
    print('processing...')
    print(data)
    maximum = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            scenic = getScenic(data, x, y)
            if scenic > maximum:
                maximum = scenic
            


    return maximum


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)

    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 8

    input()
    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    