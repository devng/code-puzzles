#!/usr/bin/env python3
# coding: utf-8

from typing import List
StrList = List[str]

import subprocess
import sys
import time


class bc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def local_shell_test(my_script: str, test_input: StrList, expected_output: StrList, exit_on_failure: bool = True) -> None:
    assert len(expected_output) == len(test_input)

    start_time = time.process_time()
    for i in range(len(test_input)):
        ti = test_input[i].strip()
        ex = expected_output[i].strip()
        cmd = 'echo "{}" | {}'.format(ti, my_script)

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.communicate()[0].decode("utf-8").strip()

        if ex != out:
            print(f"{bc.BOLD}TEST {i}{bc.ENDC}: {bc.FAIL}Failed{bc.ENDC}\n{bc.UNDERLINE}\nOutput:{bc.ENDC}\n{bc.WARNING}{out}{bc.ENDC}\n\n{bc.UNDERLINE}Expected:{bc.ENDC}\n{bc.OKBLUE}{ex}{bc.ENDC}\n")
            if exit_on_failure:
                sys.exit(1)
        else:
            print(f"{bc.BOLD}TEST {i}{bc.ENDC}: {bc.OKGREEN}OK{bc.ENDC}")

    elapsed_time = time.process_time() - start_time
    print("\nElapsed time: {:.4f}s".format(elapsed_time))
