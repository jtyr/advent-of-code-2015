#!/bin/env python2

"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie
recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You
make a list of the remaining ingredients you could use to finish the
recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately,
and you have to be accurate so you can reproduce your results in the
future. The total score of a cookie can be found by adding up each of the
properties (negative totals become 0) and then multiplying together
everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of
cinnamon (because the amounts of each ingredient must add up to 100)
would result in a cookie with the following properties:

- A capacity of 44*-1 + 56*2 = 68
- A durability of 44*-2 + 56*3 = 80
- A flavor of 44*6 + 56*-2 = 152
- A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for
now) results in a total score of 62842880, which happens to be the best
score possible given these ingredients. If any properties had produced a
negative total, it would have instead become zero, causing the whole
score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the
total score of the highest-scoring cookie you can make?

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make
another recipe that has exactly 500 calories per cookie (so they can use
it as a meal replacement). Keep the rest of your award-winning process
the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40
teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds
to 100), the total calorie count would be 40*8 + 60*3 = 500. The total
score would go down, though: only 57600000, the best you can do in such
trying circumstances.

Given the ingredients in your kitchen and their properties, what is the
total score of the highest-scoring cookie you can make with a calorie
total of 500?
"""

import itertools


def get_score(spoons, props):
    scores = {}

    for prop, val in props.iteritems():
        scores[prop] = val * spoons

    return scores


def main():
    f = open('input/15.txt', 'r')

    total_spoons = 100
    ingredients = {}

    # Parse data
    for line in f:
        line = line[0:len(line)-1]

        (name, properties) = line.split(': ')

        props = {}

        for p in properties.split(', '):
            (p_name, p_val) = p.split(' ')
            props[p_name] = int(p_val)

        ingredients[name] = props

    # To keep track of the best score
    best_score1 = 0
    best_score2 = 0

    # All variations of teaspoons
    variations = itertools.product(
        range(1, total_spoons+1), repeat=len(ingredients))

    for spoons in variations:
        if (sum(spoons) == total_spoons):
            scores = []
            n = 0
            for name, props in ingredients.iteritems():
                scores.append(get_score(spoons[n], props))
                n += 1

            sums = {}
            for s in scores:
                for prop, val in s.iteritems():
                    if prop in sums:
                        sums[prop] += val
                    else:
                        sums[prop] = val

            score = 1
            for prop, val in sums.iteritems():
                if prop != 'calories':
                    if val < 0:
                        val = 0

                    score *= val

            if score > best_score1:
                best_score1 = score

            if sums['calories'] == 500 and score > best_score2:
                best_score2 = score

    print "[Star 1] Best score: %d" % best_score1
    print "[Star 2] Best score: %d" % best_score2


if __name__ == '__main__':
    main()
