#!/usr/bin/env python3

import sys
script_dir = sys.path[0]
sys.path.insert(0, script_dir + '/..')
from codejam_local_testing import local_shell_test


test_input = ["""
1
1
""",
"""
1
4
""",
"""
1
19
"""]

expected_output = [
"""
Case #1:
1 1
""",
"""
Case #1:
1 1
2 2
3 2
""",
"""
Case #1:
1 1
2 2
3 2
4 2
5 2
6 2
6 1
7 1
8 1
"""
]

cmd = "python3 {}/pascal_walk.py".format(script_dir)
local_shell_test(cmd, test_input, expected_output)
