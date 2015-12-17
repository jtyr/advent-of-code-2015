#!/bin/env python2

"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but
must rest occasionally to recover their energy. Santa would like to know
which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting
(not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

- Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
- Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km.
After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
On the eleventh second, Comet begins resting (staying at 140 km), and
Dancer continues on for a total distance of 176 km. On the 12th second,
both reindeer are resting. They continue to rest until the 138th second,
when Comet flies for another ten seconds. On the 174th second, Dancer
flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and
Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by
that point). So, in this situation, Comet would win (if the race ended at
1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after
exactly 2503 seconds, what distance has the winning reindeer traveled?

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with
the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer
currently in the lead. (If there are multiple reindeer tied for the lead,
they each get one point.) He keeps the traditional 2503 second time
limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is
in the lead and gets one point. He stays in the lead until several
seconds into Comet's second burst: after the 140th second, Comet pulls
into the lead and gets his first point. Of course, since Dancer had been
in the lead for the 139 seconds before that, he has accumulated 139
points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor
Comet, our old champion, only has 312. So, with the new scoring system,
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input),
after exactly 2503 seconds, how many points does the winning reindeer
have?
"""


def distance(params, progress):
    if progress['rest'] == 0:
        # Running
        progress['d'] += params['speed']

        if progress['run']+1 == params['t_run']:
            progress['run'] = 0
            progress['rest'] = params['t_rest']
        else:
            progress['run'] += 1
    else:
        # Resting
        progress['rest'] -= 1


def distance2(time, speed, t_run, t_rest):
    d = 0
    run = 0
    rest = 0

    for n in range(time):
        if rest == 0:
            # Running
            d += speed

            if run+1 == t_run:
                run = 0
                rest = t_rest
            else:
                run += 1
        else:
            # Resting
            rest -= 1

    return d


def main():
    time = 2503
    f = open("input/14.txt", "r")

    data = {}

    for line in f:
        line = line[0:len(line)-1]

        line = line.replace("can fly ", "")
        line = line.replace("km/s for ", "")
        line = line.replace("seconds, but then must rest for ", "")
        line = line.replace(" seconds.", "")

        (name, speed, t_run, t_rest) = line.split(" ")

        data[name] = {
            'params': {
                'speed': int(speed),
                't_run': int(t_run),
                't_rest': int(t_rest)
            },
            'progress': {
                'd': 0,
                'run': 0,
                'rest': 0,
                'points': 0
            }
        }

    for n in range(time):
        for name, val in data.iteritems():
            distance(val['params'], val['progress'])

        max_distance = 0
        for name, val in data.iteritems():
            if val['progress']['d'] > max_distance:
                max_distance = val['progress']['d']

        for name, val in data.iteritems():
            if val['progress']['d'] == max_distance:
                val['progress']['points'] += 1

    winner1_name = ''
    winner1_d = 0
    winner2_name = ''
    winner2_points = 0

    for name, val in data.iteritems():
        if val['progress']['d'] > winner1_d:
            winner1_d = val['progress']['d']
            winner1_name = name

        if val['progress']['points'] > winner2_points:
            winner2_points = val['progress']['points']
            winner2_name = name

    print(
        "[Star 1] Fastest Reindeer %s traveled distance of %d km" % (
            winner1_name, winner1_d))
    print(
        "[Star 2] Reindeer %s collected %d points" % (
            winner2_name, winner2_points))


if __name__ == "__main__":
    main()
