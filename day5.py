#  Advent of code
#  Day 5: Doesn't He Have Intern-Elves For This?

'''
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
'''

import re

with open('day5.txt') as f:
    words = f.readlines()


def vowelRule(word):
    if len(re.findall(r'[aeiou]', word)) >= 3:
        return True


def repeatedLetterRule(word):
    if re.search(r'([a-zA-Z])\1', word):
        return True


def sequencesRules(word):
    if not re.search(r'ab|cd|pq|xy', word):
        return True


nice_words = 0
for word in words:
    if vowelRule(word) and repeatedLetterRule(word) and sequencesRules(word):
        nice_words += 1

print('Nice words: {}'.format(nice_words))

'''
--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
'''


def nonOverlapSequenceRule(word):
    if re.search(r'([a-zA-Z]{2}).*?\1', word):
        return True


def sequenceLetterBetween(word):
    if re.search(r'([a-zA-Z]).\1', word):
        return True


nice_words = 0
for word in words:
    if nonOverlapSequenceRule(word) and sequenceLetterBetween(word):
        nice_words += 1

print('New nice words: {}'.format(nice_words))
