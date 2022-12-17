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


    def canMove(self, direction, nodes):
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

    def tryMove(self, direction, nodes):
        if self.canMove(direction, nodes):
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

    nodes = set()
    count = 0
    tick_num = 0
    while count < 2022:
        newArchetype = rock_archetypes[count % len(rock_archetypes)]
        rock = Rock(newArchetype)
        rock.moveToStart(nodes)
        
        while True:
            #print(count, rock)
            #time.sleep(1)
            winddir = wind[tick_num % len(wind)]
            tick_num += 1
            rock.tryMove(winddir, nodes)
            if rock.canMove(-1, nodes):
                rock.move(-1)
            else:
                #print('stopped! ', rock)
                for part in rock.dumpParts():
                    nodes.add(part)
                count += 1
                break
            

    print(max([0] + [i.real for i in nodes]))


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
