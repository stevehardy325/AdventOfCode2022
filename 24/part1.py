from collections import defaultdict
import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

    
def move(x, y, dx, dy, walls):
    #print(walls)
    try_x = x + dx
    try_y = y + dy

    if (try_x, try_y) in walls:
        #print(try_x, try_y)
        reverse_x = x - dx
        reverse_y = y - dy
        while((reverse_x, reverse_y) not in walls):
            #print(reverse_x, reverse_y)
            reverse_x -= dx
            reverse_y -= dy
        try_x = reverse_x + dx
        try_y = reverse_y + dy
    
    #print(x, y, dx, dy, try_x, try_y)
    return try_x, try_y


def getBlizzardsNext(left, right, up, down, walls):
    next_left = set()
    for blizz in left:
        next_left.add(move(*blizz, -1, 0, walls))
    next_right = set()
    for blizz in right:
        next_right.add(move(*blizz, 1, 0, walls))
    next_up = set()
    for blizz in up:
        next_up.add(move(*blizz, 0,-1, walls))
    next_down = set()
    for blizz in down:
        next_down.add(move(*blizz, 0,1, walls))

    return frozenset(next_left), frozenset(next_right), frozenset(next_up), frozenset(next_down)



def process(fname):
    area_map = [list(l) for l in open(fname).read().splitlines()]

    walls = set()
    
    left_blizzards = set()
    right_blizzards = set()
    up_blizzards = set()
    down_blizzards = set()

    for y in range(len(area_map)):
        for x in range(len(area_map[y])):
            space = area_map[y][x]
            if space == '#':
                walls.add((x,y))
            elif space == '<':
                left_blizzards.add((x,y))
            elif space == '>':
                right_blizzards.add((x,y))
            elif space == '^':
                up_blizzards.add((x,y))
            elif space == 'v':
                down_blizzards.add((x,y))

    left_blizzards, right_blizzards, up_blizzards, down_blizzards = [frozenset(s) for s in [left_blizzards, right_blizzards, up_blizzards, down_blizzards]]

    cycle = []
    while (left_blizzards, right_blizzards, up_blizzards, down_blizzards) not in cycle:
        cycle.append((left_blizzards, right_blizzards, up_blizzards, down_blizzards))
        left_blizzards, right_blizzards, up_blizzards, down_blizzards = getBlizzardsNext(left_blizzards, right_blizzards, up_blizzards, down_blizzards, walls)
    #print(cycle)
    num_steps_in_cycle = len(cycle)
    cycle = [l.union(r).union(u).union(d) for l, r, u, d in cycle]
    blizz_cycle_set = set()
    for cycle_step in range(len(cycle)):
        for blizz_x, blizz_y in cycle[cycle_step]:
            blizz_cycle_set.add((blizz_x, blizz_y, cycle_step))



    #pathfinding:
    dest_y = len(area_map) - 1
    dest_x = len(area_map[dest_y]) - 2

    queue = [(1,0,0)]
    distances = defaultdict(lambda: float('inf'))
    distance = 0

    while len(queue) > 0:
        next_queue = set()

        for x, y, cycle_step in queue:
            next_cycle = (cycle_step+1) % num_steps_in_cycle

            if (x, y, cycle_step) not in distances:
                #print(x, y, cycle_step, 'is {} steps away======='.format(distance))
                distances[(x, y, cycle_step)] = distance

                adjacent = [(x+dx, y+dy) for dx in (-1,0,1) for dy in (-1,0,1) if (abs(dx)+abs(dy)) <=1]
                for x_adj, y_adj in adjacent:
                    #print('can step {} -> {}'.format((x, y, cycle_step), (x_adj, y_adj, next_cycle)))
                    if (x_adj, y_adj) in walls:
                        #print('    {} collides with a wall'.format((x_adj, y_adj, next_cycle)))
                        pass
                    elif (x_adj, y_adj, next_cycle) in blizz_cycle_set:
                        #print('    {} collides with a blizzard'.format((x_adj, y_adj, next_cycle)))
                        pass
                    elif x_adj < 0 or y_adj < 0 or y_adj >= len(area_map) or x_adj >= len(area_map[0]):
                        #print('    {} is out of bounds'.format((x_adj, y_adj, next_cycle)))
                        pass
                    elif (x_adj, y_adj, next_cycle) in distances:
                        #print('    {} already visited'.format((x_adj, y_adj, next_cycle)))
                        pass
                    else:
                        #print('    {} valid, adding to queue'.format((x_adj, y_adj, next_cycle)))
                        next_queue.add((x_adj, y_adj, next_cycle))
            
        queue = list(next_queue)
        distance += 1


    #print(distances)
    
    print(min([distances[dest_x, dest_y, t] for t in range(num_steps_in_cycle)]))




def main():
    #print('running for example ------')
    process(ex_input_filename)

    #print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
