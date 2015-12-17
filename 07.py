#!/bin/env python2

"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise
logic gates! Unfortunately, little Bobby is a little under the
recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a
16-bit signal (a number from 0 to 65535). A signal is provided to each
wire by a gate, another wire, or some specific value. Each wire can only
get a signal from one source, but can provide its signal to multiple
destinations. A gate provides no signal until all of its inputs have a
signal.

The included instructions booklet describes how to connect the parts
together: x AND y -> z means to connect wires x and y to an AND gate, and
then connect its output to wire z.

For example:

- 123 -> x means that the signal 123 is provided to wire x.
- x AND y -> z means that the bitwise AND of wire x and wire y is
  provided to wire z.
- p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2
  and then provided to wire q.
- NOT e -> f means that the bitwise complement of the value from wire e
  is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).
If, for some reason, you'd like to emulate the circuit instead, almost
all programming languages (for example, C, JavaScript, or Python) provide
operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle
input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal,
and reset the other wires (including wire a). What new signal is
ultimately provided to wire a?
"""

import re
import numpy as np


def process(d, k):
    ret = ""

    if d[k]["value"] is not None:
        ret = d[k]["value"]
    else:
        if d[k]["source"].startswith("NOT"):
            (n, x) = d[k]["source"].split(" ")

            if re.match("^\d+$", x):
                ret = ~ np.array([int(x)], dtype="uint16")
            else:
                ret = ~ process(d, x)
        elif re.match("^[a-z]+$", d[k]["source"]):
            ret = process(d, d[k]["source"])
        else:
            (x, op, y) = d[k]["source"].split(" ")

            if re.match("^\d+$", x):
                x = np.array([int(x)], dtype="uint16")
            else:
                x = process(d, x)

            if re.match("^\d+$", y):
                y = np.array([int(y)], dtype="uint16")
            else:
                y = process(d, y)

            if op == "AND":
                ret = x & y
            elif op == "OR":
                ret = x | y
            elif op == "LSHIFT":
                ret = x << y
            elif op == "RSHIFT":
                ret = x >> y
            else:
                print "Unknown operation: %s" % op

        d[k]["value"] = ret

    return ret


def init(key=None, val=None):
    data = {}
    f = open("input/07.txt", "r")

    for line in f:
        line = line[0:len(line)-1]

        (source, wire) = line.split(" -> ")

        record = {}
        if key is not None and wire == key:
            record = {
                "value": np.array([int(val)], dtype="uint16")
            }
        elif re.match("^\d+$", source):
            record = {
                "value": np.array([int(source)], dtype="uint16")
            }
        else:
            record = {
                "source": source,
                "value": None
            }

        data[wire] = record

    return data


def main():
    data = init()
    a = process(data, "a")
    print "[Star 1] Signal on wire a: %d" % a

    data = init("b", 16076)
    a = process(data, "a")
    print "[Star 2] Signal on wire a: %d" % a


if __name__ == "__main__":
    main()
