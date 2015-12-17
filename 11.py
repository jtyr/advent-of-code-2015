#!/bin/env python2

"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa
has devised a method of coming up with a password based on the previous
one. Corporate policy dictates that passwords must be exactly eight
lowercase letters (for security reasons), so he finds his new password by
incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and
so on. Increase the rightmost letter one step; if it was z, it wraps
around to a, and repeat with the next letter to the left until one
doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has
imposed some additional password requirements:

- Passwords must include one increasing straight of at least three
  letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip
  letters; abd doesn't count.
- Passwords may not contain the letters i, o, or l, as these letters can
  be mistaken for other characters and are therefore confusing.
- Passwords must contain at least two different, non-overlapping pairs
  of letters, like aa, bb, or zz.

For example:

- hijklmmn meets the first requirement (because it contains the straight
  hij) but fails the second requirement requirement (because it contains
  i and l).
- abbceffg meets the third requirement (because it repeats bb and ff) but
  fails the first requirement.
- abbcegjk fails the third requirement, because it only has one double
  letter (bb).
- The next password after abcdefgh is abcdffaa.
- The next password after ghijklmn is ghjaabcc, because you eventually
  skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next
password be?

--- Part Two ---

Santa's password expired again. What's the next one?
"""


def get_tripples():
    alphabet_s = ""
    alphabet = []

    for n in range(97, 123):
        alphabet_s += chr(n)

    for n in range(3, len(alphabet_s)+1):
        alphabet.append(alphabet_s[n-3:n])

    return alphabet


def replace(s, c, i):
    lst = list(s)
    lst[i] = c

    return ''.join(lst)


def inc(s, i):
    if s[i] == "z":
        s = replace(s, "a", i)
        s = inc(s, i-1)
    else:
        add = 1

        if chr(ord(s[i])+1) in "iol":
            add = 2

        s = replace(s, chr(ord(s[i]) + add), i)

    return s


def find_next(data):
    triples = get_tripples()

    found = False
    np = data

    while not found:
        np = inc(np, len(data)-1)

        found_triple = False

        for t in triples:
            if t in np:
                found_triple = True
                break

        found_twos = False
        prev_c = ""
        prev_prev_c = ""
        prev_key = ""
        pairs = {}

        for c in np:
            key = "%s%s" % (prev_c, c)

            # Take only pairs
            if prev_c != "":
                if c == prev_c and c != prev_prev_c:
                    # Count the pairs
                    if key in pairs:
                        pairs[key] += 1
                    else:
                        pairs[key] = 1
                else:
                    # Delete the pair key if keys overlap
                    pairs.pop(key, None)

            prev_key = key
            prev_prev_c = prev_c
            prev_c = c

        # Any pair key exists at least twice and triple key once
        if len(pairs) > 0 and sum(pairs.values()) > 1:
            found_twos = True

        if np == "abcdffaa":
            print found_triple
            print found_twos
            print pairs

        if found_triple and found_twos:
            found = True

    return np


def main():
    data1 = "cqjxjnds"
    data2 = "cqjxxyzz"

    print "[Star 1] New password: %s" % find_next(data1)
    print "[Star 2] Next password: %s" % find_next(data2)


if __name__ == "__main__":
    main()
