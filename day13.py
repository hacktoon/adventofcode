#  Advent of code
#  Day 13: Knights of the Dinner relation_table

'''
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular relation_table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the relation_table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
'''

import re
import itertools

relation_table = {}
people = set()
MYSELF_PART_TWO = 'me'

def get_relationship(seating):
    total = 0
    for i, me in enumerate(seating):
        p1 = seating[i-1]
        try:
            p2 = seating[i+1]
        except IndexError:
            p2 = seating[0]
        if me == MYSELF_PART_TWO:
            total += 0
            continue
        total += relation_table[(me, p1)] if p1 != MYSELF_PART_TWO else 0
        total += relation_table[(me, p2)] if p2 != MYSELF_PART_TWO else 0
    return total


def higher_change_happiness(people):
    higher_change = 0
    for seating in itertools.permutations(people):
        change = get_relationship(seating)
        if change >= higher_change:
            higher_change = change
    return higher_change


with open('input/day13.txt') as f:
    entries = f.readlines()

for line in entries:
    info = re.match(r'(.*?) would (.*?) (\d+).*?next to (.*?)\.', line).groups()
    relation_table[(info[0], info[-1])] = int(info[2]) * (-1 if info[1] == 'lose' else 1)
    people.add(info[0])

higher_change = higher_change_happiness(people)
print('Total change in happiness: {}'.format(higher_change))


'''
--- Part Two ---
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
'''

people.add(MYSELF_PART_TWO)
higher_change = higher_change_happiness(people)
print('Total change in happiness (myself included): {}'.format(higher_change))