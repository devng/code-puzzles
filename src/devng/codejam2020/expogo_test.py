#!/usr/bin/env python3

import sys
script_dir = sys.path[0]
sys.path.insert(0, script_dir + '/..')
from codejam_local_testing import local_shell_test


test_input = ["""
4
2 3
-2 -3
3 0
-1 1
"""]

expected_output = [
"""
Case #1: SEN
Case #2: NWS
Case #3: EE
Case #4: IMPOSSIBLE
"""
]

cmd = "python3 {}/expogo.py".format(script_dir)
local_shell_test(cmd, test_input, expected_output, False)
