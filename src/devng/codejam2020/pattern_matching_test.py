#!/usr/bin/env python3
# coding: utf-8

import sys
sys.path.insert(0,'..')
from codejam_local_testing import local_shell_test


test_input = ["""
2
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ
""",
"""
6
4
H*O
HELLO*
*HELLO
HE*
2
CO*DE
J*AM
2
CODE*
*JAM
2
A*C*E
*B*D
2
A*C*E
*B*D*
2
**Q**
*A*
"""]

expected_output = [
"""
Case #1: COCONUTS
Case #2: *
""",
"""
Case #1: HELLOHELLO
Case #2: *
Case #3: CODEJAM
Case #4: *
Case #5: ACBDE
Case #6: QA
"""
]

local_shell_test("python3 pattern_matching.py", test_input, expected_output, False)
