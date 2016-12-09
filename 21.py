#!/bin/env python2

"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas. It's an RPG, and
he's stuck on a boss. He needs to know what equipment to buy at the shop.
He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns
attacking. The player always goes first. Each attack reduces the
opponent's hit points by at least 1. The first character at or below 0
hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage
score minus the defender's armor score. An attacker always does at least
1 damage. So, if the attacker has a damage score of 8, and the defender
has an armor score of 3, the defender loses 5 hit points. If the defender
had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be
increased by buying items in exchange for gold. You start with no items
and have as much gold as you need. Your total damage or armor is equal to
the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but
you can't use more than one. You can buy 0-2 rings (at most one for each
hand). You must use any items you buy. The shop only has one of each
item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and
that the boss has 12 hit points, 7 damage, and 2 armor:

- The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
- The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
- The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
- The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
- The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
- The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
- The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle
input. What is the least amount of gold you can spend and still win the
fight?

--- Part Two ---

Turns out the shopkeeper is working with the boss, and can persuade you
to buy whatever items he wants. The other rules still apply, and he still
only has one of each item.

What is the most amount of gold you can spend and still lose the fight?
"""

import itertools


def strike(a, b):
    down = a['d'] - b['a']

    if down < 1:
        down = 1

    b['h'] -= down

    return b['h']


def fight(me, boss):
    winner = 'me'

    while True:
        # Me striking
        if strike(me, boss) < 1:
            break

        # Boss striking
        if strike(boss, me) < 1:
            break

    if boss['h'] > 0:
        winner = 'boss'

    return winner


def main():
    items = {
        'weapons': {
            'Dagger': {
                'c': 8,
                'd': 4,
                'a': 0
            },
            'Shortsword': {
                'c': 10,
                'd': 5,
                'a': 0
            },
            'Warhammer': {
                'c': 25,
                'd': 6,
                'a': 0
            },
            'Longsword': {
                'c': 40,
                'd': 7,
                'a': 0
            },
            'Greataxe': {
                'c': 74,
                'd': 8,
                'a': 0
            },
        },
        'armor': {
            'None': {
                'c': 0,
                'd': 0,
                'a': 0
            },
            'Leather': {
                'c': 13,
                'd': 0,
                'a': 1
            },
            'Chainmail': {
                'c': 31,
                'd': 0,
                'a': 2
            },
            'Splintmail': {
                'c': 53,
                'd': 0,
                'a': 3
            },
            'Bandedmail': {
                'c': 75,
                'd': 0,
                'a': 4
            },
            'Platemail': {
                'c': 102,
                'd': 0,
                'a': 5
            }
        },
        'rings': {
            'None1': {
                'c': 0,
                'd': 0,
                'a': 0
            },
            'None2': {
                'c': 0,
                'd': 0,
                'a': 0
            },
            'Damage +1': {
                'c': 25,
                'd': 1,
                'a': 0
            },
            'Damage +2': {
                'c': 50,
                'd': 2,
                'a': 0
            },
            'Damage +3': {
                'c': 100,
                'd': 3,
                'a': 0
            },
            'Defense +1': {
                'c': 20,
                'd': 0,
                'a': 1
            },
            'Defense +2': {
                'c': 40,
                'd': 0,
                'a': 2
            },
            'Defense +3': {
                'c': 80,
                'd': 0,
                'a': 3
            }
        }
    }

    boss_stats = {
        'h': 109,
        'd': 8,
        'a': 2
    }

    my_stats = {
        'c': 0,
        'h': 100,
        'd': 0,
        'a': 0
    }

    min_gold_win = 1000
    max_gold_lose = 0

    for w_name, w_props in items['weapons'].iteritems():
        for a_name, a_props in items['armor'].iteritems():
            for pairs in itertools.combinations(items['rings'], 2):
                me = my_stats.copy()
                boss = boss_stats.copy()

                for prop in ('a', 'd', 'c'):
                    me[prop] += w_props[prop]
                    me[prop] += a_props[prop]

                    for r in pairs:
                        me[prop] += items['rings'][r][prop]

                winner = fight(me, boss)

                if winner == 'me' and me['c'] < min_gold_win:
                    min_gold_win = me['c']

                if winner == 'boss' and me['c'] > max_gold_lose:
                    max_gold_lose = me['c']

    print "[Star 1] The least amount of gold spent to win: %s" % min_gold_win
    print "[Star 2] The max amount of gold spent to lose: %s" % max_gold_lose


if __name__ == '__main__':
    main()
