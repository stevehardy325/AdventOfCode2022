import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


facings = [(1, 0), (0,1), (-1,0), (0,-1)]
facings_chars = '>V<^'



def process(fname):
    print('processing...')
    lookup_table = {}
    data = [re.findall('\d+', l) for l in open(fname).read().splitlines()]
    area_map_str, directions = [part for part in open(fname).read().split('\n\n')]
    area_map_str = area_map_str.splitlines()
    height = len(area_map_str)
    width = max([len(r) for r in area_map_str])
    print(height, width)

    area_map = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(' ')
        area_map.append(row)
    print(area_map)
    
    for y in range(len(area_map_str)):
        for x in range(len(area_map_str[y])):
            area_map[y][x] = area_map_str[y][x]
    
    x = area_map[0].index('.')
    y = 0
    facing = 0
    area_map[y][x] = facings_chars[facing]

    nums = re.findall('\d+', directions)
    rotations = re.findall('[RL]', directions)

    while len(nums) > 0 or len(rotations) > 0:
        #print('\n'.join([''.join(l) for l in area_map]))
        #print()
        if len(nums) > 0:
            steps = int(nums.pop(0))
            print(facing)
            dx, dy = facings[facing]
            for i in range(steps):
                newx = (x + dx) % (len(area_map[0]))
                newy = (y + dy) % (len(area_map))
                while area_map[newy][newx] == ' ':
                    newx = (newx + dx) % (len(area_map[0]))
                    newy = (newy + dy) % (len(area_map))
                if area_map[newy][newx] == '#':
                    newx = x
                    newy = y
                x = newx
                y = newy
                area_map[y][x] = facings_chars[facing]
        if len(rotations) > 0:
            rotate_dir = rotations.pop(0)
            print(rotate_dir)
            if rotate_dir == 'L':
                facing = (facing - 1) % (len(facings))
            else:
                facing = (facing + 1) % (len(facings))
    print(x+1, y+1, facing)
    print(1000*(y+1) + 4*(x+1) + facing)




def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
