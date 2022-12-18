
ex_input_filename = '04_example.txt'
input_filename = '04_input.txt'

def getElfSections(s: str):
    # s looks like '2-4' meaning 2-through-4, or 2,3,4
    start, end = [int(num_str) for num_str in s.split('-')]
    
    sections = range(start, end + 1)
    sections_set = set(sections)
    return sections_set

def getElfSectionPairs(s: str):
    # s looks like 2-4,6-8 where each comma separates an elf section
    elf1str, elf2str = s.split(',')
    elf1sec = getElfSections(elf1str)
    elf2sec = getElfSections(elf2str)
    return (elf1sec, elf2sec)

def hasOverlap(e1: set, e2: set):
    intersection = e1.intersection(e2)
    if len(intersection) > 0:
        return True
    else:
        return False


def get_input(fname):
    data = []
    with open(fname) as fobj:
        data = [getElfSectionPairs(l.strip()) for l in fobj.readlines()]
    return data

def process(data):
    contains_subset_list = [hasOverlap(*d) for d in data ]
    trues = [v for v in contains_subset_list if v is True]
    
    return len(trues)


def main():
    print('running for example ------')
    ex_data = get_input(ex_input_filename)
    ex_result = process(ex_data)
    print('example result:')
    print(ex_result)
    assert ex_result == 4

    print('running for real input ------')
    input_data = get_input(input_filename)
    real_result = process(input_data)
    print('real result:')
    print(real_result)


if __name__ == '__main__':
    main()

    