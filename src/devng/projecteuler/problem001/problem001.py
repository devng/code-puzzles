#!/usr/bin/env python
# coding: utf-8

def sum_n(n):
    """sum_n returns the sum of the first n numbers"""
    return (n * n + n) / 2

def sum_3_5(limit):
    """sum_3_5 finds the sum of all the multiples of 3 or 5 below the given limit."""
    limit = limit - 1
    sum3 = sum_n(limit / 3) * 3
    sum5 = sum_n(limit / 5) * 5
    sum15 = sum_n(limit / 15) * 15
    result = sum3 + sum5 - sum15
    return result

def main():
    result = sum_3_5(1000)
    print(result)

if __name__ == '__main__':
    main()
