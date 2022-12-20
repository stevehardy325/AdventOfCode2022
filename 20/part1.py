from collections import deque

ex_input_filename = 'example.txt'
input_filename = 'input.txt'



def process(fname):
    print('processing...')
    lookup_table = {}
    lines = open(fname).read().splitlines()
    for i in range(len(lines)):
        lookup_table[i] = int(lines[i])

    d = deque(list(lookup_table))
    print( [lookup_table[n] for n in d])
    for n in lookup_table:
        idx = d.index(n)
        d.rotate(-idx)
        d.popleft()
        val = lookup_table[n]
        d.rotate(-val)
        d.appendleft(n)
        #print( [lookup_table[n] for n in d])

    mixed = [lookup_table[n] for n in d]
    print(mixed)
    idx_0 = mixed.index(0)
    idx_1000 = (idx_0 + 1000) % len(mixed)
    idx_2000 = (idx_0 + 2000) % len(mixed)
    idx_3000 = (idx_0 + 3000) % len(mixed)

    print(mixed[idx_1000]+mixed[idx_2000]+mixed[idx_3000])




def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
