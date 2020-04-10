Transmutation (15pts, 18pts, 12pts)
===================================

Round 1B - Google Code Jam 2018

source: <https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675c>


Problem
-------

You are the most skilled alchemist of a country that considers metals such as gold, platinum, and silver to be uninteresting, but highly values lead. There are M metals known in the world; lead is metal number 1 on your periodic table. Your country's leader has asked you to use the metal in the treasury to make as much lead as possible.

For each metal (including lead), you know exactly one formula that lets you create one gram of that metal by destroying one gram each of two ingredient metals. (If you are wondering about the principle of mass conservation, the other gram is lost in useless waste products.) The formulas do not work with partial grams. However, you can use each formula as often as you would like (or not at all), as long as you have the required ingredients each time.

If you make optimal choices, what is the largest total amount of lead you can end up with? Note that it is possible that you may have some metals other than lead left over after you are done.

Input
-----

The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with an integer M: the number of metals known in the world. Then there are M more lines with two integers Ri1 and Ri2 each; the i-th of these lines indicates that you can create one gram of metal i by destroying one gram of metal Ri1 and one gram of metal Ri2. Finally, there is one line with M integers G1, G2, ..., GM; Gi is the number of grams of metal i in the treasury. Lead is metal 1.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the largest amount of lead, in grams, that you can end up with.

Limits
------

1 ≤ T ≤ 100.

1 ≤ Ri1 < Ri2 ≤ M, for all i.

Time limit: 5 seconds per test set.

Memory limit: 1GB.

Test set 1 (Visible)

2 ≤ M ≤ 8.

0 ≤ Gi ≤ 8, for all i.

Test set 2 (Hidden)

2 ≤ M ≤ 100.

0 ≤ Gi ≤ 100, for all i.

Test set 3 (Hidden)

2 ≤ M ≤ 100.

0 ≤ Gi ≤ 109, for all i.

Sample
------

Input

```
3
3
2 3
1 3
1 2
5 2 3
5
3 4
3 4
4 5
3 5
1 3
0 8 6 2 4
4
3 4
2 3
2 3
2 3
0 1 1 0
```

Output

```
Case #1: 7
Case #2: 4
Case #3: 0
```

In Sample Case #1, the optimal strategy is to use 2 grams of metals 2 and 3 to produce 2 more grams of lead, for a total of 7 grams of lead.

In Sample Case #2, the optimal strategy is to first use 2 grams of metal 3 and 2 grams of metal 5 to produce 2 grams of metal 4, and then use 4 grams of metal 3 and 4 grams of metal 4 to produce 4 grams of lead. Note that it is possible for two formulas to have the same two ingredients (you just use different alchemical techniques). Also note that not every metal is necessarily an ingredient in some other formula; in this case, metal 2 is never an ingredient.

In Sample Case #3, note that it is possible for a metal to be used to produce itself. (Sometimes the laws of alchemy may be silly!) Unfortunately, it is not possible to produce any lead in this case. Note that since formulas only work on single-gram quantities, you cannot, for example, use 0.5 grams of each of metals 2 and 3 to create 0.5 grams of metal 4, and then use 0.5 grams of each of metals 3 and 4 to create 0.5 grams of lead.
Syntax pre-check
Show Test Input
