from string import ascii_letters
from collections import defaultdict
import time

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def getAdjacent(x, y, z) -> set:
    directions = [-1, 1]
    adjacent_cubes = set()
    for direction_unit in directions:
        adjacent_cubes.add((x+direction_unit,y,z))
        adjacent_cubes.add((x,y+direction_unit,z))
        adjacent_cubes.add((x,y,z+direction_unit))
    return adjacent_cubes

def getMissingAdjacentNum(x,y,z,present):
    adjacent = getAdjacent(x,y,z)
    #print(x,y,z, adjacent, present)
    missing = adjacent - present
    return len(missing)

def process(fname):
    print('processing...')
    directions = [-1, 1]

    nodes = set([tuple(int(n) for n in l.split(',')) for l in open(fname).read().split('\n')])

    missing = 0
    for node in nodes:
        missing += getMissingAdjacentNum(*node, nodes)

    
    
    print(missing)


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
