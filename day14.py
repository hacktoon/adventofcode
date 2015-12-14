#  Advent of code
#  Day 14: Reindeer Olympics

'''
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
'''

import re


TOTAL_SECONDS = 2503


def init_speed_info(line):
    name, kms, tm, rest = re.match('^([^\s]+).*?(\d+).*?(\d+).*?(\d+)', line).groups()
    return {'name': name, 'kms': int(kms), 'time': int(tm), 'rest': int(rest), 'resting': 0, 'distance': 0, 'limit': int(tm), 'points': 0}


def update_speed_info(rd):
    if rd['resting'] > 0:
        rd['resting'] -= 1
        return

    if rd['limit'] > 0:
        rd['limit'] -= 1
        rd['distance'] += rd['kms']
    else:
        rd['resting'] = rd['rest'] - 1
        rd['limit'] = rd['time']


def update_points(reindeers):
    distances = sorted(reindeers, key=lambda x: x['distance'], reverse=True)
    winner = distances[0]
    leading_distance = winner['distance']
    for d in distances:
        if d['distance'] == leading_distance:
            d['points'] += 1


with open('input/day14.txt') as f:
    speeds = f.readlines()

reindeers = []
for i in speeds:
    reindeers.append(init_speed_info(i))

for i in range(TOTAL_SECONDS):
    for reindeer in reindeers:
        update_speed_info(reindeer)
    update_points(reindeers)


winning_distance = sorted(reindeers, key=lambda x: x['distance'], reverse=True)
winner_distance = winning_distance[0]

print('The winning reindeer in first part is {} who traveled {} km'.format(winner_distance['name'], winner_distance['distance']))


'''
--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

'''

winning_points = sorted(reindeers, key=lambda x: x['points'], reverse=True)
winner_points = winning_points[0]
print('The winning reindeer in second part is {} who has {} points'.format(winner_points['name'], winner_points['points']))
