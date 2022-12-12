
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = fobj.read().strip()
    return data

def checkdupes(lst):
    return len(lst) == len(set(lst))

def process(data):
    print('processing...')
    print(data)
    start, end = 0, 4
    while end <= len(data):
        if checkdupes(data[start:end]):
            return end
        else:
            start += 1
            end += 1

def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 7

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    