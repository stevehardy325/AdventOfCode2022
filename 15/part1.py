from string import ascii_letters
from collections import defaultdict
import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

re_str = '-{0,1}\d+'


def getXsInRangeAtY(point_x, point_y, dist, yval):
    y_dist = max(point_y, yval) - min(point_y, yval)
    x_dist = dist - y_dist
    xs = set([(x, yval) for x in range(point_x - x_dist, point_x + x_dist + 1)])
    return xs


def manhattan(ax, ay, bx, by):
    dx = max(ax, bx) - min(ax, bx)
    dy = max(ay, by) - min(ay, by)
    return dx + dy

def process(fname):
    print('processing...')
    data = [re.findall(re_str, l.strip()) for l in open(fname).read().split('\n')]
    beacons = set()
    sensors = set()
    all_x = set()
    all_y = set()

    not_possible = set()

    sensors = {}

    for sx, sy, bx, by in data:
        print(sx, sy, bx, by)
        sx = int(sx)
        sy = int(sy)
        bx = int(bx)
        by = int(by)
        #sensors.add((sx, sy))
        beacons.add((bx,by))
        dist = manhattan(sx, sy, bx, by)
        sensors[(sx, sy)] = dist
        for s in ((sx - dist, sy - dist), (sx + dist, sy + dist)):
            not_possible.add(s)

    all_x = [i[0] for i in not_possible]
    all_y = [i[1] for i in not_possible]

    min_x = min(all_x)
    max_x = max(all_x)
    min_y = min(all_y)
    max_y = max(all_y)

    print(min_x, min_y, max_x, max_y)

    rownum = 2000000
    #rownum = 10
    cant_be = set()
    for sensor in sensors:
        print(sensor)
        xs = getXsInRangeAtY(*sensor, sensors[sensor], rownum)
        xs = xs.difference(beacons)
        xs = xs.difference(sensors)
        cant_be = cant_be.union(xs)
    
                


    #print(cant_be)
    print(len(cant_be))


def main():
    print('running for example ------')
    process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
