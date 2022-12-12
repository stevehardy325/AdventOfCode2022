from string import ascii_letters

def priority(letter):
    print(letter)
    return ascii_letters.index(letter) + 1


day_num = 'base'
ex_input_filename = '03_example.txt'
input_filename = '03_input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        lines = fobj.readlines()
        while len(lines) > 0:
            e1 = lines.pop(0).strip()
            e2 = lines.pop(0).strip()
            e3 = lines.pop(0).strip()
            data += [[e1, e2, e3]]
    return data

def getCommonItem(c1, c2, c3):
    common_items_1_2 = [i for i in c1 if i in c2]
    common_items = [i for i in common_items_1_2 if i in c3]
    common_items = set(common_items)
    common_items = list(common_items)
    return common_items

def getPointsFromLine(t):
    item = getCommonItem(*t)[0]
    return priority(item)

def process(data):
    print('processing {}'.format(data))
    priorties = [getPointsFromLine(l) for l in data]
    print(priorties)

    return sum(priorties)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result: {}'.format(ex_result))
    assert ex_result == 70

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('example result: {}'.format(real_result))
    assert real_result == 20


if __name__ == '__main__':
    main()

    