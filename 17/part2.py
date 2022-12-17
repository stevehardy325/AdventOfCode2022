from string import ascii_letters
from collections import defaultdict
import time

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


class Rock:
    def __init__(self, pattern_str):
        lines = pattern_str.split('\n')
        self.height = len(lines)
        self.width = len(lines[0])
        self.parts = []
        for i in range(self.height):
            for j in range(self.width):
                if lines[i][j] == '#':
                    self.parts.append(complex(0-i, j))
        self.position = complex(0,0)


    def canMove(self, direction, nodes, max_i):
        bottom = self.position.real - self.height + 1
        left = self.position.imag
        right = self.position.imag + self.width - 1

        if bottom > max_i + 2 and left > 1 and right < 7:
            return True
        
        for part in self.parts:
            part_abs_pos = part + self.position + direction
            if part_abs_pos in nodes:
                return False
            if part_abs_pos.imag > 7 or part_abs_pos.imag < 1:
                return False
            if part_abs_pos.real < 1:
                return False
        return True

    def dumpParts(self):
        abs_parts = [p + self.position for p in self.parts]
        return abs_parts
            

    def move(self, direction):
        self.position += direction

    def tryMove(self, direction, nodes, max_i):
        if self.canMove(direction, nodes, max_i):
            self.move(direction)

    def moveToStart(self, nodes):
        yval = max([0] + [i.real for i in nodes])
        yval += 3
        yval += self.height
        self.position = complex(yval, 3)

    def __repr__(self):
        return '{} height {} width {} @{}'.format(self.parts,self.height, self.width, self.position)



pat1 = '''####'''
pat2 = '''.#.
###
.#.'''
pat3 = '''..#
..#
###'''
pat4 ='''#
#
#
#'''
pat5='''##
##'''

rock_archetypes = [pat1, pat2, pat3, pat4, pat5]

def process(fname):
    print('processing...')
    wind = [complex(0, -1) if l == '<' else complex(0,1) for l in open(fname).read()]

    seen = {}
    seen_second = {}

    nodes = set()
    max_i = -1
    count = 0
    tick_num = 0
    check_rocks = []
    height_before_cycles = 0
    height_of_cycle = 0
    cycle_start = False
    cycle_end = False
    target = 1000000000000
    #target = 2022
    while count < target:
        try:
            archetype_index = count % len(rock_archetypes)
            newArchetype = rock_archetypes[archetype_index]
            init_wind_index = tick_num % len(wind)
            rock = Rock(newArchetype)
            rock.moveToStart(nodes)

            max_i = int(max([0] + [i.real for i in nodes]))
            top_nodes = frozenset([complex(i - max_i, j) for i in range(max_i - 40, max_i + 1) for j in range(1, 8) if complex(i,j) in nodes])
            state = (top_nodes, archetype_index, init_wind_index)
            if state in seen:
                if state in seen_second:
                    first_count, first_height = seen[state]
                    second_count,second_height = seen_second[state]
                    count_diff = second_count - first_count
                    height_diff = second_height-first_height
                    new_height = max_i
                    if count_diff + count < target:
                        while count_diff + count < target:
                            new_height += height_diff
                            count += count_diff
                        nodes_at_top = [n + new_height for n in top_nodes]
                        for n in nodes_at_top:
                            nodes.add(n)
                        continue

                else:
                    seen_second[state] = (count, max_i)
                    print('CYCLE')
            else:
                seen[state] = (count, max_i)

            
            
            while True:
                #print(count, rock)
                #time.sleep(1)
                winddir = wind[tick_num % len(wind)]
                tick_num += 1
                rock.tryMove(winddir, nodes, max_i)
                if rock.canMove(-1, nodes, max_i):
                    rock.move(-1)
                else:
                    #print('stopped! ', rock)
                    for part in rock.dumpParts():
                        nodes.add(part)
                    count += 1
                    break
        except KeyboardInterrupt as e:
            print(count)
            exit(1)
            

    print(int(max([0] + [i.real for i in nodes])))


def main():
    print('running for example ------')
    process(ex_input_filename)
    time.sleep(10)
    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
