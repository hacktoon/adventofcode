#  Advent of code
#  Day 11: Corporate Policy

'''
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?
'''

import re

password = 'vzbxkghb'


def has_allowed_letters(pwd):
    if set('iol').intersection(set(pwd)):
        return False
    return True


def has_pairs(pwd):
    if re.search(r'([a-z])\1.*([a-z])\2', pwd):
        return True
    return False


def has_increasing_straight(pwd):
    for i, s in enumerate(pwd[:-2]):
        sec = ord(pwd[i+1])
        trd = ord(pwd[i+2])
        if ord(pwd[i]) + 1 == sec and sec + 1 == trd:
            return True
    return False


def is_valid(pwd):
    return has_increasing_straight(pwd) and \
        has_pairs(pwd) and \
        has_allowed_letters(pwd)


def increment(pwd):
    ordinals = [ord(s) for s in pwd]
    carry = False
    idx = -1
    while True:
        try:
            n = ordinals[idx]
        except IndexError:
            break
        if n == ord('z'):
            ordinals[idx] = ord('a')
            carry = True
        else:
            ordinals[idx] += 1
            break
        idx -= 1
    return ''.join([chr(s) for s in ordinals])

while not is_valid(password):
    password = increment(password)

print('The next valid password is {!r}'.format(password))

'''
--- Part Two ---
Santa's password expired again. What's the next one?

'''
password = increment(password)
while not is_valid(password):
    password = increment(password)

print('The next one is {!r}'.format(password))