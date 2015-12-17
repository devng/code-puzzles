#!/usr/bin/env python3

import functools


data = {}


@functools.lru_cache()
def get_value(var_name):
    if var_name.isdigit():
        return int(var_name)

    ops = data[var_name]
    if len(ops) == 1:
        # we have just and assignment
        return get_value(ops[0])
    else:
        op = ops[-2]
        if op == 'AND':
          return get_value(ops[0]) & get_value(ops[2])
        elif op == 'OR':
          return get_value(ops[0]) | get_value(ops[2])
        elif op == 'NOT':
          return ~get_value(ops[1]) & 0xffff
        elif op == 'RSHIFT':
          return get_value(ops[0]) >> get_value(ops[2])
        elif op == 'LSHIFT':
          return get_value(ops[0]) << get_value(ops[2])
        else:
            raise ValueError("Unknown operation: %s" % op)


def process_file(filename, search_var_name='a', extra_vars=None):
    with open(filename, "r") as fin:
        for line in fin:
            (ops, var_name) = line.split("->")
            var_name = var_name.strip() # the result var name
            ops = ops.strip().split(" ") # the splitted operation
            data[var_name] = ops

    # needed for part two
    if extra_vars:
        data.update(extra_vars)
    return get_value(search_var_name)


def main():
    get_value.cache_clear()
    a = process_file("input.txt")
    print("Part one: a = %d" % a)

    get_value.cache_clear()
    a2 = process_file("input.txt", extra_vars={'b': [str(a)]})
    print("Part two: a = %d" % a2)


if __name__ == "__main__":
    main()
