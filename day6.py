#  Advent of code
#  Day 6: Probably a Fire Hazard

'''
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
'''

import re

with open('day6.txt') as f:
    instructions = f.readlines()


grid = []
size = 1000

TURN_ON = 'turn on'
TURN_OFF = 'turn off'
TOGGLE = 'toggle'


def turn_on(x, y):
    grid[x][y] = 1


def turn_off(x, y):
    grid[x][y] = 0


def toggle(x, y):
    grid[x][y] = int(not grid[x][y])


def update(comm, from_range, to_range):
    for row in range(from_range[0], to_range[0] + 1):
        for col in range(from_range[1], to_range[1] + 1):
            comm(row, col)


def parse(line):
    coords = re.findall(r'(\d+,\d+)', line)
    from_range = [int(x) for x in coords[0].split(',')]
    to_range = [int(x) for x in coords[1].split(',')]
    if line.startswith(TURN_ON):
        comm = turn_on
    if line.startswith(TURN_OFF):
        comm = turn_off
    if line.startswith(TOGGLE):
        comm = toggle
    return (comm, from_range, to_range)


def init_grid():
    for row in range(size):
        grid.append([])
        for col in range(size):
            grid[row].append(0)

init_grid()

for i in instructions:
    command, from_range, to_range = parse(i)
    update(command, from_range, to_range)

total_lights = 0
for row in range(size):
    for col in range(size):
        if grid[row][col] == 1:
            total_lights += 1

print('Total lights: {}'.format(total_lights))

'''
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

'''

grid = []
init_grid()


def turn_on(x, y):
    grid[x][y] += 1


def turn_off(x, y):
    grid[x][y] -= 1
    if grid[x][y] < 0:
        grid[x][y] = 0


def toggle(x, y):
    grid[x][y] += 2


for i in instructions:
    command, from_range, to_range = parse(i)
    update(command, from_range, to_range)

total_brightness = 0
for row in range(size):
    for col in range(size):
        total_brightness += grid[row][col]

print('Total brightness: {}'.format(total_brightness))
