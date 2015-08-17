#!/usr/bin/env python
# coding: utf-8

import datetime

def count_sundays(from_year, to_year):
    """Counts how many Sundays fell on the first of the month during a given period."""
    sundays = 0
    for year in range(from_year, to_year):
        for month in range(1, 13):
            d = datetime.date(year, month, 1)
            if d.weekday() == 6:
                sundays += 1
    return sundays

def main():
    sundays = count_sundays(1901, 2001)
    print(sundays)

if __name__ == '__main__':
    main()
