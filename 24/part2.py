from collections import defaultdict

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def move(x, y, dx, dy, walls):
    # calculate next position, based on current and direction

    try_x = x + dx
    try_y = y + dy

    if (try_x, try_y) in walls:  # we hit a wall, wrap around
        reverse_x = x - dx
        reverse_y = y - dy
        while ((reverse_x, reverse_y) not in walls):
            reverse_x -= dx
            reverse_y -= dy
        try_x = reverse_x + dx
        try_y = reverse_y + dy

    return try_x, try_y


def getBlizzardsNext(left, right, up, down, walls):
    # get next states for all blizzards going in each direction

    next_left = set()
    for blizz in left:
        next_left.add(move(*blizz, -1, 0, walls))
    next_right = set()
    for blizz in right:
        next_right.add(move(*blizz, 1, 0, walls))
    next_up = set()
    for blizz in up:
        next_up.add(move(*blizz, 0, -1, walls))
    next_down = set()
    for blizz in down:
        next_down.add(move(*blizz, 0, 1, walls))

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
                walls.add((x, y))
            elif space == '<':
                left_blizzards.add((x, y))
            elif space == '>':
                right_blizzards.add((x, y))
            elif space == '^':
                up_blizzards.add((x, y))
            elif space == 'v':
                down_blizzards.add((x, y))

    # convert to frozen sets for easy hashing
    left_blizzards, right_blizzards, up_blizzards, down_blizzards = [frozenset(
        s) for s in [left_blizzards, right_blizzards, up_blizzards, down_blizzards]]

    # because blizzards wrap, they will eventually cycle the state back to initial. Find the cycle pattern
    cycle = []
    while (left_blizzards, right_blizzards, up_blizzards, down_blizzards) not in cycle:
        cycle.append((left_blizzards, right_blizzards,
                     up_blizzards, down_blizzards))
        left_blizzards, right_blizzards, up_blizzards, down_blizzards = getBlizzardsNext(
            left_blizzards, right_blizzards, up_blizzards, down_blizzards, walls)

    # convert cycle pattern into a set of blizzards for each possbile cycle state
    num_steps_in_cycle = len(cycle)
    # list of all sets of all blizzard positions for each cycle state
    cycle = [l.union(r).union(u).union(d) for l, r, u, d in cycle]

    # will be a set of all possible blizzard positions in format (x, y, cycle_state_num)
    blizz_cycle_set = set()
    for cycle_step in range(len(cycle)):
        for blizz_x, blizz_y in cycle[cycle_step]:
            blizz_cycle_set.add((blizz_x, blizz_y, cycle_step))

    # now do pathfinding
    dest_y = len(area_map) - 1
    dest_x = len(area_map[dest_y]) - 2

    # time from start to end
    time_start_to_end_first = getTimeToTravel(
        1, 0, 0, dest_x, dest_y, blizz_cycle_set, num_steps_in_cycle, walls, area_map)

    # time from end to start, starting on the cycle step we hit "end" on
    t2 = time_start_to_end_first % num_steps_in_cycle
    time_end_to_start = getTimeToTravel(
        dest_x, dest_y, t2, 1, 0, blizz_cycle_set, num_steps_in_cycle, walls, area_map)

    # time from end to start, starting on the cycle step we got back to "start"
    t3 = (time_start_to_end_first + time_end_to_start) % num_steps_in_cycle
    time_start_to_end_second = getTimeToTravel(
        1, 0, t3, dest_x, dest_y, blizz_cycle_set, num_steps_in_cycle, walls, area_map)

    print(time_start_to_end_first + time_end_to_start + time_start_to_end_second)


def getTimeToTravel(start_x, start_y, start_t, dest_x, dest_y, blizz_cycle_set, num_steps_in_cycle, walls, area_map):
    # Use BFS to determine distances. Nodes are in format (x, y, cyclestep)

    queue = [(start_x, start_y, start_t)]
    distances = defaultdict(lambda: float('inf'))
    distance = 0

    while len(queue) > 0:
        next_queue = set()

        for x, y, cycle_step in queue:
            next_cycle = (cycle_step+1) % num_steps_in_cycle

            if (x, y, cycle_step) not in distances:
                distances[(x, y, cycle_step)] = distance

                adjacent = [(x+dx, y+dy) for dx in (-1, 0, 1)
                            for dy in (-1, 0, 1) if (abs(dx)+abs(dy)) <= 1]
                for x_adj, y_adj in adjacent:
                    if ( (x_adj, y_adj) not in walls 
                        and (x_adj, y_adj, next_cycle) not in blizz_cycle_set 
                        and 0 <= x_adj < len(area_map[0]) 
                        and 0 <= y_adj < len(area_map) 
                        and (x_adj, y_adj, next_cycle) not in distances):
                        
                            next_queue.add((x_adj, y_adj, next_cycle))

        queue = next_queue
        distance += 1

    return (min([distances[dest_x, dest_y, t] for t in range(num_steps_in_cycle)]))


def main():
    # print('running for example ------')
    process(ex_input_filename)

    # print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
