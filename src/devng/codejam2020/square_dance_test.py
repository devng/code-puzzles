#!/usr/bin/env python3
# coding: utf-8

import sys
script_dir = sys.path[0]
sys.path.insert(0, script_dir + '/..')
from codejam_local_testing import local_shell_test


test_input = ["""
5
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
3 3
1 3 1
3 1 2
1 2 1
"""
]

expected_output = [
"""
Case #1: 15
Case #2: 16
Case #3: 14
Case #4: 14
Case #5: 31
"""
]

cmd = "python3 {}/square_dance.py".format(script_dir)
local_shell_test(cmd, test_input, expected_output, False)
