#!/bin/env python2

"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from
some unknown benefactor. It comes with instructions and an example
program, but the computer itself seems to be malfunctioning. She's
curious what the program does, and would like you to help her run it.

The manual explains that the computer supports two registers and six
instructions (truly, it goes on to remind the reader, a state-of-the-art
technology). The registers are named a and b, can hold any non-negative
integer, and begin with a value of 0. The instructions are as follows:

- hlf r sets register r to half its current value, then continues with
  the next instruction.
- tpl r sets register r to triple its current value, then continues with
  the next instruction.
- inc r increments register r, adding 1 to it, then continues with the
  next instruction.
- jmp offset is a jump; it continues with the instruction offset away
  relative to itself.
- jie r, offset is like jmp, but only jumps if register r is even ("jump
  if even").
- jio r, offset is like jmp, but only jumps if register r is 1 ("jump if
  one", not odd).

All three jump instructions work with an offset relative to that
instruction. The offset is always written with a prefix + or - to
indicate the direction of the jump (forward or backward, respectively).
For example, jmp +1 would simply continue with the next instruction,
while jmp +0 would continuously jump back to itself forever.

The program exits when it tries to run an instruction beyond the ones
defined.

For example, this program sets a to 2, because the jio instruction causes
it to skip the tpl instruction:

inc a
jio a, +2
tpl a
inc a

What is the value in register b when the program in your puzzle input is
finished executing?

--- Part Two ---

The unknown benefactor is very thankful for releasi-- er, helping little
Jane Marie with her computer. Definitely not to distract you, what is the
value in register b after the program is finished executing if register a
starts as 1 instead?
"""


def run(prog, reg):
    run = 0
    prog_len = len(prog)
    cnt = 0

    while True:
        if prog[run]['cmd'] == 'hlf':
            if reg[prog[run]['arg1']] > 0:
                reg[prog[run]['arg1']] = int(reg[prog[run]['arg1']]/2)

            run += 1
        elif prog[run]['cmd'] == 'tpl':
            reg[prog[run]['arg1']] *= 3
            run += 1
        elif prog[run]['cmd'] == 'inc':
            reg[prog[run]['arg1']] += 1
            run += 1
        elif prog[run]['cmd'] == 'jmp':
            run += prog[run]['arg1']
        elif prog[run]['cmd'] == 'jie':
            if reg[prog[run]['arg1']] % 2 == 0:
                run += prog[run]['arg2']
            else:
                run += 1
        elif prog[run]['cmd'] == 'jio':
            if reg[prog[run]['arg1']] == 1:
                run += prog[run]['arg2']
            else:
                run += 1
        else:
            print "ERROR: Unknown command"
            break

        if run >= prog_len:
            break
        elif cnt > 10000:
            print "ERROR: Too many iterations"
            break

        cnt += 1


def main():
    f = open('input/23.txt', 'r')

    prog = []

    for line in f:
        line = line[0:len(line)-1]
        line = line.replace(',', '')

        instr = line.split(' ')

        record = {
            'cmd': instr[0],
            'arg1': instr[1]
        }

        if record['cmd'] == 'jmp':
            record['arg1'] = int(record['arg1'])

        if len(instr) > 2:
            record['arg2'] = int(instr[2])

        prog.append(record)

    reg = {'a': 0, 'b': 0}
    run(prog, reg)

    print "[Star 1] Reg b: %d" % reg['b']

    reg = {'a': 1, 'b': 0}
    run(prog, reg)

    print "[Star 2] Reg b: %d" % reg['b']


if __name__ == '__main__':
    main()
