#!/bin/env python2

"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty
or nice.

A nice string is one with all of the following properties:

- It contains at least three vowels (aeiou only), like aei, xazegov, or
  aeiouaeiouaeiou.
- It contains at least one letter that appears twice in a row, like xx,
  abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
- It does not contain the strings ab, cd, pq, or xy, even if they are part
  of one of the other requirements.

For example:

- ugknbfddgicrmopn is nice because it has at least three vowels
  (u...i...o...), a double letter (...dd...), and none of the disallowed
  substrings.
- aaa is nice because it has at least three vowels and a double letter,
  even though the letters used by different rules overlap.
- jchzalrnumimnmhp is naughty because it has no double letter.
- haegwjzuvuyypxyu is naughty because it contains the string xy.
- dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of
determining whether a string is naughty or nice. None of the old rules
apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

- It contains a pair of any two letters that appears at least twice in the
  string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not
  like aaa (aa, but it overlaps).
- It contains at least one letter which repeats with exactly one letter
  between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

- qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
  and a letter that repeats with exactly one letter between them (zxz).
- xxyxx is nice because it has a pair that appears twice and a letter
  that repeats with one between, even though the letters used by each rule
  overlap.
- uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat
  with a single letter between them.
- ieodomkazucvgmuy is naughty because it has a repeating letter with one
  between (odo), but no pair that appears twice.

How many strings are nice under these new rules?
"""


def main():
    f = open("input/05.txt", "r")

    nice1 = 0
    nice2 = 0

    for full_line in f:
        line = full_line[0:len(full_line)-1]

        # # # Star 1
        vowels = 0

        # Count vowels
        for c in line:
            for v in "aeiou":
                if v == c:
                    vowels += 1

                    # Quit the loop if happy
                    if vowels > 2:
                        break

            # Quit the loop if happy
            if vowels > 2:
                break

        prev_c = ""
        multi = False

        # Check for series of the same chars
        for c in line:
            if c == prev_c:
                multi = True
                break

            prev_c = c

        if (
                vowels > 2 and
                multi and
                "ab" not in line and
                "cd" not in line and
                "pq" not in line and
                "xy" not in line
                ):
            nice1 += 1

        # # # Star 2
        prev_c = ""
        prev_prev_c = ""
        prev_key = ""
        prev_prev_key = ""
        pairs = {}
        triples = {}

        for c in line:
            key = "%s%s" % (prev_c, c)

            # Take only pairs
            if prev_c != "":
                if prev_key != key:
                    # Count the pairs
                    if key in pairs:
                        pairs[key] += 1
                    else:
                        pairs[key] = 1
                elif prev_prev_key == prev_key:
                    pairs[key] = 2
                else:
                    # Delete the pair key if keys overlap
                    pairs.pop(key, None)

            prev_prev_key = prev_key
            prev_key = key

            # <prev_c><whatever><c>
            if c == prev_prev_c:
                key = "%s%s" % (prev_prev_c, key)

                # Count the triple keys
                if key in triples:
                    triples[key] += 1
                else:
                    triples[key] = 1

            prev_prev_c = prev_c
            prev_c = c

        # Any pair key exists at least twice and triple key once
        if len(pairs) and sorted(pairs.values())[-1] > 1 and len(triples) > 0:
            nice2 += 1

    print "[Star 1] Number of nice words: %d" % nice1
    print "[Star 2] Number of nice words: %d" % nice2


if __name__ == "__main__":
    main()
