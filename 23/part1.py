from collections import defaultdict
import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

       

def prElves(elves):
    xs = [e[0] for e in elves]
    ys = [e[1] for e in elves]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    for y in range(min_y, max_y + 1):
        outstr = ''
        for x in range(min_x, max_x+1):
            if (x,y) not in elves:
                outstr += '.'
            else:
                outstr += '#'
        print(outstr)
    print()
    return None


    

def getIntendedMove(x, y, elves, directions):
    print('Calculating', x,y)
    nearby = (-1,0,1)
    is_nearby = False
    for dx, dy in [(dx, dy) for dx in nearby for dy in nearby if (dx, dy) != (0,0)]:
        if (x+dx, y+dy) in elves:
            is_nearby = True
    if is_nearby:
        print('Other elf nearby, trying to move')
        for dx, dy in directions:
            clear = True
            if dx == 0:
                for neighboring_dx in (-1,0,1):
                    test_x = x + neighboring_dx
                    test_y = y + dy
                    if (test_x, test_y) in elves:
                        clear = False
            elif dy == 0:            
                for neighboring_dy in (-1,0,1):
                    test_x = x + dx
                    test_y = y + neighboring_dy
                    if (test_x, test_y) in elves:
                        clear = False
            if clear:
                print('can move {}'.format((dx, dy)))
                return x + dx, y + dy
    print('Couldnt move')
    return x, y



def process(fname):
    print('processing...')
    lookup_table = {}
    data = open(fname).read().splitlines()
    print(data)

    
    elves = set()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '#':
                print((x,y))
                elves.add((x,y))
    prElves(elves)
    input()
    start_len = len(elves)
    directions = [(0,-1), (0,1), (-1,0), (1,0)] # N/S/W/E

    for i in range(10):
        print(i)
        prElves(elves)
        print(directions)
        
        target_dest_counts = defaultdict(lambda: 0)
        intended_dests = {}
        for x,y in elves:
            new_x, new_y = getIntendedMove(x, y, elves, directions)
            intended_dests[(x, y)] = (new_x, new_y)
            target_dest_counts[(new_x, new_y)] += 1

        next_elves = set()
        for x,y in elves:
            intended_x, intended_y = intended_dests[(x,y)]
            if target_dest_counts[(intended_x, intended_y)] == 1:
                next_elves.add((intended_x, intended_y))
            else:
                next_elves.add((x,y))
        
        directions = directions[1:] + [directions[0]]
        elves = next_elves

    prElves(elves)

    xs = [e[0] for e in elves]
    ys = [e[1] for e in elves]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    missing = [(x,y) for x in range(min_x, max_x+1) for y in range(min_y, max_y + 1) if (x,y) not in elves]
    
    print(len(missing))




def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
