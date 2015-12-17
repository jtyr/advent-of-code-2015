#!/bin/env python2

"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it
all into your refrigerator, you'll need to move it into smaller
containers. You take an inventory of the capacities of the available
containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5
liters. If you need to store 25 liters, there are four ways to do it:

- 15 and 10
- 20 and 5 (the first 5)
- 20 and 5 (the second 5)
- 15, 5, and 5

Filling all containers entirely, how many different combinations of
containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of
eggnog arrives! The shipping and receiving department is requesting as
many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters
of eggnog. How many different ways can you fill that number of containers
and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There
were three ways to use that many containers, and so the answer there
would be 3.
"""

import itertools


def main():
    cnt = 0
    total_volume = 150
    containers = []
    num_containers = 0

    f = open('input/17.txt', 'r')

    for line in f:
        line = line[0:len(line)-1]
        containers.append(int(line))

    # Determine the maximum number of combinations
    num_comb = 0
    sum_volumes = 0
    for c in sorted(containers):
        sum_volumes += c

        if sum_volumes <= total_volume:
            num_comb += 1
        else:
            break

    for n in range(1, num_comb+1):
        for c in itertools.combinations(containers, n):
            if sum(c) == total_volume:
                cnt += 1

                if num_containers == 0:
                    num_containers = n

    print "[Star 1] Number of combinations: %d" % cnt
    print "[Star 2] Min number of containers: %d" % num_containers


if __name__ == '__main__':
    main()
