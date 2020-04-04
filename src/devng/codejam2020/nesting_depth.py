#!/usr/bin/env python3
# coding: utf-8

def insert_parentheses(numbers):
    cur_open = 0
    result = ""

    for num in numbers:
        if cur_open == num:
            result += str(num)
        elif cur_open < num:
            result += "(" * (num - cur_open)
            result += str(num)
        elif cur_open > num:
            result += ")" * (cur_open - num)
            result += str(num)
        cur_open = num
    if cur_open > 0:
        result += ")" * cur_open
    
    return result

if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    num_cases = int(input()) # read a line with a single integer
    for i in range(1, num_cases + 1):
        line = input()
        numbers = [int(ch) for ch in line]
        result = insert_parentheses(numbers)
        print("Case #{}: {}".format(i, result))