#!/usr/bin/env python3
# coding: utf-8

from parenting import *
import unittest

class SheduleTest(unittest.TestCase):
    def test_assign_tasks(self):
        s = assign_tasks([(360, 480, 0), (420, 540, 1), (600, 660, 2)])
        self.assertEqual(s, "JCJ")

        tasks = [(0, 1440, 0), (1, 3, 1), (2, 4, 2)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "IMPOSSIBLE")

        tasks = [(99, 150, 0), (1, 100, 1), (100, 301, 2), (2, 5, 3), (150, 250, 4)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "CJJCC")

        tasks = [(0, 720, 0), (720, 1440, 1)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "JJ")

        tasks = [(0, 10, 0), (10, 20, 1), (15, 30, 2), (30, 40, 3), (25, 50, 4)]
        s = assign_tasks(tasks)
        self.assertNotEqual(s, "IMPOSSIBLE")
        self.assertEqual(s, "JJCCJ")


    def test_check_solution(self):
        tasks = [(0, 1440, 0), (1, 3, 1), (2, 4, 2)]
        is_solution = check_solution(tasks, "JJ")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "CC")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "JC")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "CJ")
        self.assertEqual(is_solution, False)

        tasks = [(0, 720, 0), (720, 1440, 1)]
        is_solution = check_solution(tasks, "JJ")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "JC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CJ")
        self.assertEqual(is_solution, True)

        tasks = [(99, 150, 0), (1, 100, 1), (100, 301, 2), (2, 5, 3), (150, 250, 4)]
        is_solution = check_solution(tasks, "JCCJJ")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CJJCC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "JJJ")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "JJJCC")
        self.assertEqual(is_solution, False)


        tasks = [(0, 10, 0), (10, 20, 1), (15, 30, 2), (30, 40, 3), (25, 50, 4)]
        is_solution = check_solution(tasks, "JCJJC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "JJCCJ")
        self.assertEqual(is_solution, True)


if __name__ == '__main__':
    unittest.main()
