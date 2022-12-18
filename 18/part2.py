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

def getBubbles(present, missing):
    min_y,min_x,min_z,max_y,max_y,max_y = 0,0,0,0,0,0

    for x,y,z in present:
        if min_x is None or x < min_x:
            min_x = x -1
        if max_x is None or x > max_x:
            max_x = x + 1
        if min_y is None or y < min_y:
            min_y = y - 1
        if max_y is None or y > max_y:
            max_y = y + 1
        if min_z is None or z < min_z:
            min_z = z -1
        if max_z is None or z > max_z:
            max_z = z +1

    in_bubble = set()

    directions = [(0,0,1),(0,1,0),(1,0,0),(0,0,-1),(0,-1,0),(-1,0,0)]
    
    for node in missing:
        x,y,z = node
        hit_count = 0
        for dx, dy, dz in directions:
            while y < max_y and y > min_y and z < max_z and z > min_z and x < max_x and x > min_x:
                x += dx
                y += dy
                z += dz
                if (x,y,z) in present:
                    hit_count += 1
                    break
        if hit_count == 6:
            in_bubble.add(node)


    return in_bubble


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
