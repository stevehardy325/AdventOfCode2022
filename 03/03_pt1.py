from string import ascii_letters

def priority(letter):
    return ascii_letters.index(letter) + 1


day_num = 'base'
ex_input_filename = '03_example.txt'
input_filename = '03_input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [l.strip() for l in fobj.readlines()]
    return data

def getCommonItem(s):
    l = len(s)//2
    c1 = s[0:l]
    c2 = s[l:]
    assert len(c1) == len(c2)
    common_items = [i for i in c1 if i in c2]
    common_items = set(common_items)
    common_items = list(common_items)
    assert len(common_items) == 1
    return common_items

def getPointsFromLine(s):
    item = getCommonItem(s)[0]
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
    assert ex_result == 157

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('example result: {}'.format(real_result))
    assert real_result == 20


if __name__ == '__main__':
    main()

    