import datetime
import functools
import json
from string import ascii_letters
from collections import defaultdict
import re
import sys
import time
sys.setrecursionlimit(100000)

ex_input_filename = 'example.txt'
input_filename = 'input.txt'

re_str = '-{0,1}\d+'

paths = {}
flows = {}

def getTimeToOpen(valve_name, nearby_valves):
    distance = {}
    cur_valves = [valve_name]
    
    dist = 0
    while len(cur_valves) > 0:
        next_round = set()

        for valve in cur_valves:
            if valve not in distance:
                distance[valve] = dist + 1
                for touching in nearby_valves[valve]:
                    next_round.add(touching)
        cur_valves = next_round
        dist += 1

    return distance

def getOptimalFlow(start_valve, closed_valves, all_valves, time_left=30):
    current_flow_rate = sum([flows[valve] for valve in all_valves.difference(closed_valves)])
    if time_left == 0:
        return 0
    elif len(closed_valves) < 1:
        return current_flow_rate * time_left
    else:
        options = {}
        for valve in sorted(closed_valves):
            time_to_reach = distances[start_valve][valve]
            if time_to_reach < time_left:
                flow_after_opened = getOptimalFlow(valve, closed_valves.difference(set([start_valve,valve])), all_valves, time_left=time_left - time_to_reach)
                flow_until_opened = current_flow_rate * time_to_reach
                options[valve] = flow_after_opened + flow_until_opened
            else:
                options[valve] = current_flow_rate * time_left
        path_flow_rates = sorted([options[key] for key in options], reverse=True)
        return path_flow_rates[0]
            
        



def process(fname):
    global distances
    global flows
    # "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    print('processing...')
    data = [l.strip().split(' ') for l in open(fname).read().split('\n')]

    valve_map = {}
    flows = {}
    distances = {}

    for line in data:
        valve_name = line[1]
        valve_rate = int(line[4].split('=')[1].replace(';',''))
        valve_map[valve_name] = [l.replace(',', '') for l in line[9:]]
        flows[valve_name] = valve_rate

    for valve in valve_map:
        distances[valve] = getTimeToOpen(valve, valve_map)

    closed_valves = set(valve for valve in valve_map if flows[valve] > 0)
    print(getOptimalFlow('AA', closed_valves, set(distances)))
    


def main():
    print('running for example ------')
    #process(ex_input_filename)

    print('running for real input ------')
    process(input_filename)


if __name__ == '__main__':
    main()
