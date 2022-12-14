from string import ascii_letters
from collections import defaultdict

from animation import ImageHandler


ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def getAllRocks(a, b):
    ax, ay = [int(n) for n in a.split(',')]
    bx, by = [int(n) for n in b.split(',')]
    startx = min(ax, bx)
    starty = min(ay, by)
    endx = max(ax, bx)
    endy = max(ay, by)

    rock_locations = [(x, y) for x in range(startx, endx + 1) for y in range(starty, endy+1)]
    return rock_locations



def process(fname):
    print('processing...')
    ih = ImageHandler(fname+".gif")
    data = [l.split(' -> ') for l in open(fname).read().split('\n')]
    print(data)

    rocks = set()
    for rock_wall_list in data:
        for idx in range(1, len(rock_wall_list)):
            new_rocks = getAllRocks(rock_wall_list[idx-1], rock_wall_list[idx])
            for rock in new_rocks:
                rocks.add(rock)

    #print(sorted(rocks))

    run = True
    sand_rest_count = 0
    lowest_rock = max([rock[1] for rock in rocks]) + 2
    
    blocks = set(rocks)

    while (500, 0) not in blocks:
        sand = (500, 0)
        while True:
            #print(sand)
            sandx, sandy = sand
            new_sand = sand
            targets = [(sandx, sandy+1),(sandx-1, sandy+1),(sandx+1, sandy+1)]

            for t in targets:
                if t not in blocks and t[1] != lowest_rock:
                    new_sand = t
                    break
            if sand == new_sand:
                blocks.add(sand)
                sand_rest_count += 1
                break
            else:
                sand = new_sand
        ih.createSnapshot(blocks, rocks, sand)

    ih.outputgif()
    print(sand_rest_count)

        


            
            

        


    





def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
