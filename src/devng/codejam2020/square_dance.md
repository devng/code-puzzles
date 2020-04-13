Square Dance (9pts, 28pts)
==========================

Round 1A - Google Code Jam 2020

source: <https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355>

Problem
-------

You are organizing an international dancing competition. You have already obtained all of the following:

* A dance floor with R rows and C columns, consisting of unit square cells;
* R × C competitors;
* A cutting-edge automated judge for the competition.

But you are still missing an audience! You are worried that the competition might not be interesting enough, so you have come up with a way to calculate the interest level for the competition.

Each competitor occupies one square unit cell of the floor and stays there until they are eliminated. A _compass neighbor_ of a competitor x is another competitor y chosen such that y shares a row or column with x, and there are no competitors still standing in cells in between x and y. Each competitor may have between 0 and 4 compass neighbors, inclusive, and the number may decrease if all the other competitors in one orthogonal direction are eliminated.

The competition runs one round at a time. In between rounds i and i+1, if a competitor d had at least one compass neighbor during round i, and d's skill level is strictly less than the average skill level of all of d's compass neighbors, d is eliminated and is not part of the competition for rounds i+1, i+2, i+3, etc. Notice that d still counts as a neighbor of their other compass neighbors for the purpose of other eliminations that may also happen between rounds i and i+1. Competitors that do not have any compass neighbors are never eliminated. If after a round no competitor is eliminated, then the competition ends.

The _interest level of a round_ is the sum of skill levels of the competitors dancing in that round (even any competitors that are to be eliminated between that round and the next). The _interest level of the competition_ is the sum of the interest levels of all of the rounds.

Given the skill levels of the dancers that are on the floor for the first round, what is the interest level of the competition?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing two integers R and C. Then, there are R more lines containing C integers each. The j-th value on the i-th of these lines, Si, j, represents the skill level of the dancer in the cell in the i-th row and j-th column of the floor.
Output

For each test case, output one line containing `Case #x: y`, where `x` is the test case number (starting from 1) and `y` is the interest level of the competition.

Limits
------

Time limit: 40 seconds per test set.

Memory limit: 1GB.

1 ≤ Si,j ≤ 10^6, for all i and j.

Test set 1 (Visible Verdict)

1 ≤ T ≤ 100.

1 ≤ R × C ≤ 100.

Test set 2 (Hidden Verdict)

10 ≤ T ≤ 100.

1000 < R × C ≤ 105, in exactly 10 cases.

1 ≤ R × C ≤ 1000, in exactly T - 10 cases.

Sample
------

Input

```
4
1 1
15
3 3
1 1 1
1 2 1
1 1 1
1 3
3 1 2
1 3
1 2 3
```

Output

```
Case #1: 15
Case #2: 16
Case #3: 14
Case #4: 14
```

In Sample Case #1, only one competitor is on the floor. Since the competitor does not have any compass neighbors, they dance in one round, and then the competition is over. Thus the answer is equal to the dancer's skill level, 15.

In Sample Case #2, the interest level of the first round is 1+1+1+1+2+1+1+1+1=10.

The competitors that are not in the center nor in a corner have a skill level of 1, but the average of their compass neighbors is 4 / 3, which is greater than 1, so they are eliminated. The floor during the second round looks like this:

```
1 . 1
. 2 .
1 . 1
```

This round is the last one. The competitors in the corner have two compass neighbors each, but the average of their skill level is equal to their own. The competitor in the center has no compass neighbor. The interest level of the round is 1+1+2+1+1=6. This means the interest level of the competition is 10+6=16.

In Sample Case #3, the competitor with skill level 1 is eliminated after the first round, while the other two remain. In the second round, the two other competitors become compass neighbors, and this causes the competitor with skill level 2 to be eliminated. There is a single competitor in the third round, which makes it the last one. The interest levels of the rounds are 6, 5 and 3, making the interest level of the competition 14.
