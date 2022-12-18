from string import ascii_letters
from collections import defaultdict
import time

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def getAdjacent(x, y, z) -> set:
    adjacent_cubes = set()
    for direction_unit in [-1, 1]:
        adjacent_cubes.add((x+direction_unit,y,z))
        adjacent_cubes.add((x,y+direction_unit,z))
        adjacent_cubes.add((x,y,z+direction_unit))
    return adjacent_cubes

def getOutside(present):
    min_y,min_x,min_z,max_y,max_z,max_x = 0,0,0,0,0,0

    for x,y,z in present:
        min_y = min(min_y, y - 5)
        min_x = min(min_x, x - 5)
        min_z = min(min_z, z - 5)
        max_y = max(max_y, y + 5)
        max_x = max(max_x, x + 5)
        max_z = max(max_z, z + 5)

    #bounding box
    all_in_box = set([(x,y,z) for y in range(min_y-1, max_y+1) for z in range(min_z-1, max_z+1) for x in range(min_x-1, max_x+1)])

    #path-walking to see where we can touch from outside, start at a corner outside of the droplet
    seen = set()
    checking = [(max_x,max_y,max_z)]
    while len(checking) > 0:
        check_next = set()
        for x,y,z in checking:
            seen.add((x,y,z))
            # looking for unvisited open spaces only
            adjacent = getAdjacent(x,y,z).difference(seen).difference(present)

            # limit to bounding box so we don't grow infinitely
            adjacent = adjacent.intersection(all_in_box)

            check_next = check_next.union(adjacent)
        checking = check_next

    return seen

def getMissingAdjacentNum(x,y,z,present, outside):
    adjacent = getAdjacent(x,y,z)
    missing = adjacent.difference(present)
    missing = outside.intersection(missing)
    return len(missing)

def process(fname):
    print('processing...')
    nodes = set([tuple(int(n) for n in l.split(',')) for l in open(fname).read().split('\n')])
    outside = getOutside(nodes)
    missing = 0
    for node in nodes:
        missing += getMissingAdjacentNum(*node, nodes, outside)
    
    print(missing)


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
