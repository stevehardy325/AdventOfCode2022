from string import ascii_lowercase
from collections import defaultdict

ex_input_filename = 'example.txt'
input_filename = 'input.txt'


def process(fname):
    print('processing...')
    data = [list(l) for l in open(fname).read().split('\n')]
        

    starts = []
    end = [99,99]
    nodes = []
    for linenum in range(len(data)):
        line = data[linenum]
        for charnum in range(len(line)):
            character = line[charnum]
            if character == 'S' or character == 'a':
                data[linenum][charnum] = 'a'
                starts += [(charnum,linenum)]
            elif character == 'E':
                data[linenum][charnum] = 'z'
                end = (charnum,linenum)

    dists = [getDistStartToEnd(s, end, data) for s in starts]
    print(min(dists))
    

def getDistStartToEnd(start, end, data):
    heightFunc = lambda c: ascii_lowercase.index(c)
    reachable = lambda start, fin: heightFunc(fin) <= heightFunc(start) + 1

    checknodes = [start]
    visited = defaultdict(lambda: float('inf') )
    steps = 0
    while len(checknodes) > 0:
        visitable = set()
        while len(checknodes) > 0:
            node = checknodes.pop()
            visited[node] = steps
            x, y = node
            touching_nodes = [n for n in [(x, y+1),(x, y-1),(x+1, y),(x-1, y)] if n[0] >= 0 and n[1] >= 0 and n[0] < len(data[0]) and n[1] < len(data)]
            
            for target_node in touching_nodes:
                if target_node not in visited:
                    target_x, target_y = target_node
                    if reachable(data[y][x], data[target_y][target_x]):
                        visitable.add(target_node)
        checknodes = list(visitable)
        steps += 1

    return visited[end]

def main():
    print('running for example ------')
    process(ex_input_filename)
    
    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()

    
