# Find the guard that has the most minutes asleep.
# What minute does that guard spend asleep the most?

from re import search
from datetime import datetime


def minutes_asleep():
    datafile = open('input-4.txt', 'r').readlines()
    guard_minutes = dict()

    # sort chronologically
    sorted_data = sorted(datafile)

    # iterate sorted_data array, pick out all guards #nnn
    guard_numbers = []
    # datafile = open('input-4.txt', 'r').read()
    for entry in sorted_data:
        guard_number = search(r"(#\d+)", entry)
        if guard_number:
            guard_numbers.append(guard_number.group(0))
    return guard_numbers

    # datafile.close()
    # return guard_numbers

    # print(len(datafile))
    # return type(datafile)


print(minutes_asleep())
