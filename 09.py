#!/bin/env python2

"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single
night.

This year, however, he has some new locations to visit; his elves have
provided him the distances between every pair of locations. He can start
and end at any two (different) locations he wants, but he must visit each
location exactly once. What is the shortest distance he can travel to
achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the
answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the
longest distance instead.

He can still start and end at any two (different) locations he wants, and
he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982
via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""


# https://github.com/dmishin/tsp-solver
from tsp_solver.greedy import solve_tsp


def main():
    D = [
        [0,    65, 129, 144,  71, 137,   3, 149],
        [65,    0,  63,   4, 105, 125,  55,  14],
        [129,  63,   0,  68,  52,  65,  22, 143],
        [144,   4,  68,   0,   8,  23, 136, 115],
        [71,  105,  52,   8,   0, 101,  84,  96],
        [137, 125,  65,  23, 101,   0, 107,  14],
        [3,    55,  22, 136,  84, 107,   0,  46],
        [149,  14, 143, 115,  96,  14,  46,   0]
    ]

    path = solve_tsp(D)

    cnt = 0
    prev = -1

    for n in path:
        if prev > -1:
            cnt += D[prev][n]

        prev = n

    print "[Star 1] min length: %d" % cnt

# Patch for Star 2
'''
diff --git a/tsp_solver/greedy.py b/tsp_solver/greedy.py
index c2ec9bc..db2fb83 100644
--- a/tsp_solver/greedy.py
+++ b/tsp_solver/greedy.py
@@ -25,7 +25,7 @@ def optimize_solution( distances, connections ):
         b = a+1
         for c in xrange( b+2, N-1):
             d = c+1
-            delta_d = ds(a,b)+ds(c,d) -( ds(a,c)+ds(b,d))
+            delta_d = - ds(a,b) - ds(c,d) + ds(a,c) + ds(b,d)
             if delta_d > 0:
                 d_total += delta_d
                 optimizations += 1
@@ -74,7 +74,7 @@ def pairs_by_dist(N, distances):
             idx += 1
             
     indices.sort(key = lambda ij: distances[ij[0]][ij[1]])
-    return indices
+    return reversed(indices)
     
 def solve_tsp( distances, optim_steps=3, pairs_by_dist=pairs_by_dist ):
     """Given a distance matrix, finds a solution for the TSP problem.
'''


if __name__ == "__main__":
    main()
