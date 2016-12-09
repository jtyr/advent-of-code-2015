#!/bin/env python2

"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter:
now, at most ten thousand lights are allowed. You arrange them in a
100x100 grid.

Never one to let you down, Santa again mails you instructions on the
ideal lighting configuration. With so few lights, he says, you'll have to
resort to animation.

Start by setting your lights to the included initial configuration (your
puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next
configuration based on the current one. Each light's next state (either
on or off) depends on its current state and the current states of the
eight lights adjacent to it (including diagonals). Lights on the edge of
the grid might have fewer than eight neighbors; the missing ones always
count as "off".

For example, in a simplified 6x6 grid, the light marked A has the
neighbors numbered 1 through 8, and the light marked B, which is on an
edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or
off) plus the number of neighbors that are on:

- A light which is on stays on when 2 or 3 neighbors are on, and turns off
  otherwise.
- A light which is off turns on if exactly 3 neighbors are on, and stays
  off otherwise.

All of the lights update simultaneously; they all consider the same
current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how
many lights are on after 100 steps?

--- Part Two ---

You flip the instructions over; Santa goes on to point out that this is
all just an implementation of Conway's Game of Life. At least, it was,
until you notice that something's wrong with the grid of lights you
bought: four lights, one in each corner, are stuck on and can't be turned
off. The example above will actually run like this:

Initial state:
##.#.#
...##.
#....#
..#...
#.#..#
####.#

After 1 step:
#.##.#
####.#
...##.
......
#...#.
#.####

After 2 steps:
#..#.#
#....#
.#.##.
...##.
.#..##
##.###

After 3 steps:
#...##
####.#
..##.#
......
##....
####.#

After 4 steps:
#.####
#....#
...#..
.##...
#.....
#.#..#

After 5 steps:
##.###
.##..#
.##...
.##...
#.#...
##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but
with the four corners always in the on state, how many lights are on
after 100 steps?
"""


def init(size):
    matrix = []

    for n in range(size):
        matrix.append([0] * size)

    return matrix


def process(matrix, size, skip_corners=False):
    new_matrix = init(size)

    for x in range(size):
        for y in range(size):
            cnt_on = 0

            if (
                    skip_corners and (
                        x == 0 and y == 0 or
                        x == 0 and y == size-1 or
                        x == size-1 and y == 0 or
                        x == size-1 and y == size-1)):
                new_matrix[x][y] = matrix[x][y]
                next

            if x-1 >= 0 and matrix[x-1][y] == 1:
                cnt_on += 1

            if y-1 >= 0 and matrix[x][y-1] == 1:
                cnt_on += 1

            if x+1 < size and matrix[x+1][y] == 1:
                cnt_on += 1

            if y+1 < size and matrix[x][y+1] == 1:
                cnt_on += 1

            if x-1 >= 0 and y-1 >= 0 and matrix[x-1][y-1] == 1:
                cnt_on += 1

            if x+1 < size and y-1 >= 0 and matrix[x+1][y-1] == 1:
                cnt_on += 1

            if x-1 >= 0 and y+1 < size and matrix[x-1][y+1] == 1:
                cnt_on += 1

            if x+1 < size and y+1 < size and matrix[x+1][y+1] == 1:
                cnt_on += 1

            if matrix[x][y] == 1 and cnt_on in (2, 3):
                new_matrix[x][y] = 1

            if matrix[x][y] == 0 and cnt_on == 3:
                new_matrix[x][y] = 1

    return new_matrix


def main():
    cnt1 = 0
    cnt2 = 0
    size = 100
    steps = 100

    matrix = init(size)

    f = open('input/18.txt', 'r')

    l = 0
    for line in f:
        line = line[0:len(line)-1]

        for i, c in enumerate(line):
            if c == '#':
                matrix[l][i] = 1
            else:
                matrix[l][i] = 0

        l += 1

    matrix1 = list(matrix)
    matrix2 = list(matrix)

    for s in range(steps):
        matrix1 = process(matrix1, size)

    for x in range(size):
        for y in range(size):
            if matrix1[x][y] == 1:
                cnt1 += 1

    # Light on corners
    matrix2[0][0] = 1
    matrix2[0][size-1] = 1
    matrix2[size-1][0] = 1
    matrix2[size-1][size-1] = 1

    for s in range(steps):
        matrix2 = process(matrix2, size, True)

    for x in range(size):
        for y in range(size):
            if matrix2[x][y] == 1:
                cnt2 += 1

    print "[Star 1] Number of lights on: %d" % cnt1
    print "[Star 2] Number of lights on: %d" % cnt2


if __name__ == '__main__':
    main()
