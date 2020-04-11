#!/usr/bin/env python3
# coding: utf-8

import subprocess
import sys
import time


def local_shell_test(py_script: str, test_input: list, expected_output: list) -> None:
    assert len(expected_output) == len(test_input)
    start_time = time.process_time()

    for i in range(len(test_input)):
        ti = test_input[i].strip()
        ex = expected_output[i].strip()
        cmd = 'echo "{}" | python3 {}'.format(ti, py_script)

        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out = p.communicate()[0].decode("utf-8").strip()

        if ex != out:
            print("TEST {} Failed , output is:\n\n".format(i), out, file=sys.stderr, sep="")
            sys.exit(1)
        else:
            print("TEST {} Ok".format(i))

    elapsed_time = time.process_time() - start_time
    print("\nElapsed time: {:.4f}".format(elapsed_time))
