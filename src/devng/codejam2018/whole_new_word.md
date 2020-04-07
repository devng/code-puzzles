A Whole New Word (11pts, 17pts)
===============================

Round 1C - Google Code Jam 2018

source: <https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e064>

Problem
-------

 Vincent and Desta are childhood friends. Today, Vincent is showing N distinct L-letter words to Desta by using some letter tiles. Each tile contains one uppercase English alphabet letter, and one number between 1 and L. A word consists of the letters spelled out by L tiles with numbers from 1 through L, in order. (Vincent's words are not necessarily real English words.)

For example, if Vincent has `N = 3` words with `L = 4`, and the words are `{CAKE, TORN, SHOW}`, then Vincent must show the following to Desta:

```
C1 A2 K3 E4
T1 O2 R3 N4
S1 H2 O3 W4
```

Desta feels that creating words must be easy, and he wants to create a new word that obeys the rules above and is not one of Vincent's existing words. However, Desta does not have any tiles of his own, so he must use some of Vincent's tiles.

For instance, if Vincent has the words from the previous example, then Desta can make a new word such as CORN or SAKE or CHRE (Desta's words are also not necessarily real English words). Each of the example is illustrated in the following image:

```
C1 O2 R3 N4
S1 A2 K3 E4
C1 H2 R3 E4
```

Note that the three rows in the image above are independent. Desta only needs to make one new word.

However, in the above example, Desta cannot make WAKE, for example, because there is no W tile with a number 1. Nor can he make COO, since it is not the right length.

Notice that it may be impossible for Desta to make a new word. For example, if Vincent has only one word, then Desta cannot make anything new. Or, if Vincent has the words {AA, AB, BA, BB}, then any word that Desta can form is already present.

Help Desta to choose a word that he can show to Vincent using only the tiles used by Vincent, or indicate that it is impossible to do so.

Input
-----

The first line of the input gives the number of test cases, T. T test cases follow. Each begins with one line with two integers N and L: the number of Vincent's words, and the length of each word. Then, N more lines follow. The i-th of these lines contains a string of L uppercase English letters representing the i-th of Vincent's words.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a valid word to be chosen by Desta, or - (a single dash character of ASCII value 45) if there is no valid word to be chosen by Desta. If there is more than one valid word that Desta can make, you can output any of them.

Limits
------

1 ≤ T ≤ 100.
Time limit: 15 seconds per test set.
Memory limit: 1GB.
No two of Vincent's words are the same.
Test set 1 (Visible)

1 ≤ N ≤ 262.
1 ≤ L ≤ 2.
Test set 2 (Hidden)

1 ≤ N ≤ 2000.
1 ≤ L ≤ 10.
Sample

Input

```
5
4 1
A
B
C
D
4 2
WW
AA
SS
DD
4 2
AA
AB
BA
BB
3 4
CAKE
TORN
SHOW
5 7
HELPIAM
TRAPPED
INSIDEA
CODEJAM
FACTORY
```

Output

```
Case #1: -
Case #2: WA
Case #3: -
Case #4: CORN
Case #5: HOLIDAY
```

Note that the last two sample cases would not appear in test set 1.

In Sample Case #1, the only words that can be construted using the tiles used by Vincent are A, B, C, D. However, all of those words already appear in Vincent's list of words, so Desta is not allowed to choose them.

In Sample Case #2, there are 12 possible new words that Desta can make, one of which is WA.

Sample Case #3 was explained in the problem description above; there is no new word that Desta can make.

Sample Case #4 was explained in the problem description above; other answers such as SAKE are possible.

In Sample Case #5, other answers such as TRAPJAM are possible.
Show Test Input


Analysis
========

Test set 1
----------

Since L ≤ 2, this test set can be solved using a complete search. First, we collect the letters that appear among the first characters of the input words in a set C1 and the letters that appear among the second characters of the input words in a set C2. Any candidate new word has the form c1c2, where c1 is in C1 and c2 is in C2. For each candidate new word, we check whether this word is in the input. We can output any candidate new word which does not appear in the input as our answer. If every candidate new word already appears in the input, the case is impossible.

Since there are only at most 262 different candidate words that we need to try, this solution will run very quickly.

Test set 2
----------

In early rounds of Code Jam, a complete search will often work for the first test set, but will generally not work for subsequent test sets. This problem is an exception! Our approach above will work just fine for test set 2.

We can create sets C1, C2, ..., CL as in the solution above, and then use them to generate candidate words as before, one at a time. If we encounter a word that is not in the input, we can return it as our answer. If it turns out that there are exactly N candidate words (which implies that every word that could be generated is already in the input), the case is impossible. Otherwise, we can be sure that we will have found an answer by the time we generate and check the (N + 1)th candidate word, since there are only N words in the input list.
Show Test Input
