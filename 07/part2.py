
from enum import Enum


ex_input_filename = 'example.txt'
input_filename = 'input.txt'

filetree = {'/': []}

class NodeType(Enum):
    FILE = 0
    DIR = 1

class Node:
    def __init__(self, name, parent, ntype, size=0):
        self.name = name
        self.ntype = ntype
        self.children = {}
        self.size = size
        self.parent = parent

    def getSize(self):
        return self.size + sum([self.children[c].getSize() for c in self.children])
    
    def __repr__(self):
        return '{} {} {}'.format(self.name, self.size, self.ntype)


def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [cmd.strip() for cmd in fobj.read().split('$')]
    return data

def getNode(l, parentnode) -> Node:
    size, name = l.split(' ')
    if size == 'dir':
        size = 0
        ntype = NodeType.DIR
    else:
        size = int(size)
        ntype = NodeType.FILE
    return Node(name, parentnode, ntype, size)


def process(data):
    print('processing...')
    print(data)
    
    rootNode = Node('/', None, NodeType.DIR)
    curNode = rootNode
    allNodes = [rootNode]

    for cmd_res in data:
        print(cmd_res)
        lines = [c.strip() for c in cmd_res.split('\n')]
        if lines[0] == 'ls':
            for l in lines[1:]:
                child = getNode(l, curNode)
                curNode.children[child.name] = child
                allNodes.append(child)
        elif 'cd' in lines[0]:
            dest_dir = lines[0].split(' ')[1]
            if dest_dir == '/':
                curNode = rootNode
            elif dest_dir == '..':
                curNode = curNode.parent
            else:
                curNode = curNode.children[dest_dir]

    total = 70000000
    totalNeeded = 30000000
    totalUsed = rootNode.getSize()
    totalMinToDel = totalUsed - (total - totalNeeded)

    return min([n.getSize() for n in allNodes if n.ntype == NodeType.DIR and n.getSize() >= totalMinToDel])
    
    print(allNodes)
    return sum([n.getSize() for n in allNodes if n.ntype == NodeType.DIR and n.getSize() <= 100000])

def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 24933642

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    