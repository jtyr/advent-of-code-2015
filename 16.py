#!/bin/env python2

"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her
a thank you card. However, there's a small problem: she signed it "From,
Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out
which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave
you the gift. You open the present and, as luck would have it, good ol'
Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you
wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a
few specific compounds in a given sample, as well as how many distinct
kinds of those compounds there are. According to the instructions, these
are what the MFCSAM can detect:

- children, by human DNA age analysis.
- cats. It doesn't differentiate individual breeds.
- Several seemingly random breeds of dog: samoyeds, pomeranians, akitas,
  and vizslas.
- goldfish. No other kinds of fish.
- trees, all in one group.
- cars, presumably by exhaust or gasoline or something.
- perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping
from the gift into the MFCSAM. It beeps inquisitively at you a few times
and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue.
Things missing from your list aren't zero - you simply don't remember the
value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's
instructions catches your eye. Apparently, it has an outdated
retroencabulator, and so the output from the machine isn't exact values -
some of them indicate ranges.

In particular, the cats and trees readings indicates that there are
greater than that many (due to the unpredictable nuclear decay of cat
dander and tree pollen), while the pomeranians and goldfish readings
indicate that there are fewer than that many (due to the modial
interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""


def get_matches_count(a, b, n):
    cnt = 0

    for key, val in a.iteritems():
        if b[key] is not None:
            if n == 1 and key in ['cats', 'trees']:
                if b[key] > val:
                    cnt += 1
            elif n == 1 and key in ['pomeranians', 'goldfish']:
                if b[key] < val:
                    cnt += 1
            elif val == b[key]:
                cnt += 1

    return cnt


def main():
    f = open('input/16.txt', 'r')

    sues = {}

    for line in f:
        line = line[0:len(line)-1]

        line = line.replace('Sue ', '')

        (sue, things) = line.split(' ', 1)
        sue = int(sue.replace(':', ''))

        record = {
            'children': None,
            'cats': None,
            'samoyeds': None,
            'pomeranians': None,
            'akitas': None,
            'vizslas': None,
            'goldfish': None,
            'trees': None,
            'cars': None,
            'perfumes': None
        }

        for thing in things.split(', '):
            (key, val) = thing.split(': ')
            record[key] = int(val)

        sues[sue] = record

    my_sue = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    matching_items = [0, 0]
    matched_sue = [0, 0]

    for sue, things in sues.iteritems():
        for n in range(2):
            cnt = get_matches_count(my_sue, things, n)

            if cnt > matching_items[n]:
                matching_items[n] = cnt
                matched_sue[n] = sue

    print "[Star 1] Sue number: %d" % matched_sue[0]
    print "[Star 2] Sue number: %d" % matched_sue[1]


if __name__ == '__main__':
    main()
