from string import ascii_letters
from collections import defaultdict

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def process(fname):
    print('processing...')
    data = [list(l) for l in open(fname).read().split('\n')]

    print(len(data))


def main():
    print('running for example ------')
    process(ex_input_filename)

    #print('running for real input ------')
    # process(input_filename)


if __name__ == '__main__':
    main()
