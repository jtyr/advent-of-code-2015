#!/bin/env python2

"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating
contest year after year, you've decided to deploy one million lights in a
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has
mailed you instructions on how to display the ideal lighting
configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the
lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
instructions include whether to turn on, turn off, or toggle various
inclusive ranges given as coordinate pairs. Each coordinate pair
represents opposite corners of a rectangle, inclusive; a coordinate pair
like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The
lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your
lights by doing the instructions Santa sent you in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.
- toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
  turning off the ones that were on, and turning on the ones that were off.
- turn off 499,499 through 500,500 would turn off (or leave off) the
  middle four lights.

After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize
you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls;
each light can have a brightness of zero or more. The lights all start at
zero.

The phrase turn on actually means that you should increase the brightness
of those lights by 1.

The phrase turn off actually means that you should decrease the
brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness
of those lights by 2.

What is the total brightness of all lights combined after following
Santa's instructions?

For example:

- turn on 0,0 through 0,0 would increase the total brightness by 1.
- toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""


def switch1(m, c, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if c == "turn_on":
                m[x][y] = 1
            elif c == "turn_off":
                m[x][y] = 0
            elif c == "toggle":
                m[x][y] = not m[x][y]


def switch2(m, c, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if c == "turn_on":
                m[x][y] += 1
            elif c == "turn_off":
                if m[x][y] > 1:
                    m[x][y] -= 1
                else:
                    m[x][y] = 0
            elif c == "toggle":
                m[x][y] += 2


def main():
    f = open("input/06.txt", "r")

    lit = 0
    brightness = 0
    size = 1000
    matrix1 = []
    matrix2 = []

    for n in range(size):
        matrix1.append([0] * size)
        matrix2.append([0] * size)

    for line in f:
        line = line.replace(" o", "_o")

        (command, start, through, end) = line.split(" ")
        (start_x, start_y) = map(int, start.split(","))
        (end_x, end_y) = map(int, end.split(","))

        switch1(matrix1, command, start_x, start_y, end_x, end_y)
        switch2(matrix2, command, start_x, start_y, end_x, end_y)

    for column in matrix1:
        for cell in column:
            if cell != 0:
                lit += 1

    for column in matrix2:
        for cell in column:
            if cell != 0:
                brightness += cell

    print "[Star 1] Number of lit lights: %d" % lit
    print "[Star 2] Total brightness of all lit lights: %d" % brightness


if __name__ == "__main__":
    main()
