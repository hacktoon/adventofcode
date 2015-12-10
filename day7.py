#  Advent of code
#  Day 7: Some Assembly Required

'''
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
'''

import operator

MAX = 65535

wires = {}
commands = {
    'AND': operator.and_,
    'OR': operator.or_,
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift
}


def normalize_value(val):
    return val


def process_param(param):
    if param.isdigit():
        param = int(param)
    else:
        return int(wires.get(param, 0))
    return param


def parse(line):
    tokens = line.strip().split(' ')
    first_token = tokens[0]
    if first_token == 'NOT':
        val = MAX - process_param(tokens[1])
    elif first_token.isalpha():
        param1 = process_param(first_token)
        if tokens[1] in commands.keys():  # xy AND 7...
            param2 = process_param(tokens[2])
            val = commands[tokens[1]](param1, param2)
        else:  # x -> f
            val = param1
    elif first_token.isdigit():
        param1 = int(first_token)
        if tokens[1] in commands.keys():  # 55 AND 44...
            param2 = process_param(tokens[2])
            val = commands[tokens[1]](param1, param2)
        else:  # 55 ->...
            val = param1

    wires[tokens[-1]] = normalize_value(val)


with open('input/day7.txt') as f:
    instructions = f.readlines()

for i in instructions:
    parse(i)
print(wires)

print('Value of wire a: {}'.format(wires.get('a')))


'''
--- Part Two ---


'''