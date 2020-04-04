#!/usr/bin/env python3
# coding: utf-8

from parenting import *
import unittest

class SheduleTest(unittest.TestCase):
    def test_assign_tasks(self):
        s = assign_tasks([(360, 480), (420, 540), (600, 660)])
        self.assertEqual(s, "JCC")

        tasks = [(0, 1440), (1, 3), (2, 4)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "IMPOSSIBLE")

        tasks = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "JCCJJ")

        tasks = [(0, 720), (720, 1440)]
        s = assign_tasks(tasks)
        self.assertEqual(s, "JC")

        tasks = [(0, 10), (10, 20), (15, 30), (30, 40), (25, 50)]
        s = assign_tasks(tasks)
        self.assertNotEqual(s, "IMPOSSIBLE")
        self.assertEqual(s, "JCJJC")


    def test_check_solution(self):
        tasks = [(0, 1440), (1, 3), (2, 4)]
        is_solution = check_solution(tasks, "JJ")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "CC")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "JC")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "CJ")
        self.assertEqual(is_solution, False)

        tasks = [(0, 720), (720, 1440)]
        is_solution = check_solution(tasks, "JJ")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "JC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CJ")
        self.assertEqual(is_solution, True)

        tasks = [(99, 150), (1, 100), (100, 301), (2, 5), (150, 250)]
        is_solution = check_solution(tasks, "JCCJJ")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "CJJCC")
        self.assertEqual(is_solution, True)
        is_solution = check_solution(tasks, "JJJ")
        self.assertEqual(is_solution, False)
        is_solution = check_solution(tasks, "JJJCC")
        self.assertEqual(is_solution, False)


        tasks = [(0, 10), (10, 20), (15, 30), (30, 40), (25, 50)]
        is_solution = check_solution(tasks, "JCJJC")
        self.assertEqual(is_solution, True)


if __name__ == '__main__':
    unittest.main()