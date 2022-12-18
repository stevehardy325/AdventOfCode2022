
ex_input_filename = 'example.txt'
input_filename = 'input.txt'

def getCrateLayout(s: str):
    lines = s.split('\n')
    lines.reverse()
    lines.pop(0)
    column_count = (len(lines[0]) + 1) // 4
    crate_columns = {}
    for i in range(1, column_count + 1):
        crate_columns[i] = []

    for l in lines:
        print(l)
        text_col = 1
        while text_col <= column_count:
            char_num = (text_col - 1) * 4 + 1
            print(char_num)
            char = l[char_num]
            if char is not ' ':
                crate_columns[text_col] += [l[char_num]]
            text_col += 1
    
    return crate_columns

def getMove(s: str):
    # get one move from one line
    parts = s.split(' ')
    num_moved = int(parts[1])
    source = int(parts[3])
    dest = int(parts[5])
    return (num_moved, source, dest)

def getMoves(s: str):
    # get all moves from all move lines
    moves_split = s.split('\n')
    moves = [getMove(l) for l in moves_split]
    return moves

def get_input(fname):
    data = []
    with open(fname) as fobj:
        top_raw_str, bottom_raw_str = fobj.read().split('\n\n')
        crates = getCrateLayout(top_raw_str)
        print(crates)
        moves = getMoves(bottom_raw_str)
        print(moves)
    return (crates, moves)

def moveCrates(crates, moves):
    for m in moves:
        num_moved, source, dest = m
        crates_lifted = []
        for i in range(num_moved):
            crates_lifted += crates[source].pop()
        crates_lifted.reverse()
        for c in crates_lifted:
            crates[dest].append(c)
    return crates

def getAnswer(crates):
    outstr = ''.join([crates[pile].pop() for pile in crates])
    return outstr



def process(crates, moves):
    print('processing...')
    # print(data)
    crates = moveCrates(crates, moves)
    return getAnswer(crates)
    


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(*ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 'MCD'

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(*input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    