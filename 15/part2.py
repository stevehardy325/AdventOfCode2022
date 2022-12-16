from string import ascii_letters
from collections import defaultdict
import re

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

re_str = '-{0,1}\d+'


def getCircle(pointx, pointy, dist):
    points = set()
    quadrants = [(1,1),(1,-1),(-1,-1),(-1,1)]

    for xdist in range(dist+1):
        ydist = dist - xdist
        for unitx, unity in quadrants:
            points.add((pointx+xdist*unitx,pointy+ydist*unity))
    
    return points



def getHighLowXsInRangeAtY(point_x, point_y, dist, yval):
    y_dist = max(point_y, yval) - min(point_y, yval)
    x_dist = dist - y_dist
    if x_dist >= 0:
        return range(point_x - x_dist, point_x + x_dist)
    else:
        return None


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

    rownum = 4000000
    #rownum = 20


    check_points = set()
    for sensor in sensors:
        print(sensor)
        just_outside_dist = sensors[sensor] + 1
        sx, sy = sensor
        check_points = check_points.union(getCircle(sx, sy, just_outside_dist))

    check_points = [(x,y) for x, y in check_points if x >= 0 and y >= 0 and x <= rownum and y <= rownum]
    
    for x, y in check_points:
        contact = False
        for sensor in sensors:
            dist = sensors[sensor]
            if manhattan(x, y, *sensor) <= dist:
                contact = True
                break
        if not contact:
            print(x,y)
            input('FOUND IT')

    





def main():
    print('running for example ------')
    #process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
