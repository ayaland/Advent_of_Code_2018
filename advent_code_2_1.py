from collections import Counter


def calcChecksum():
    datafile = open('input-2.txt', 'r').readlines()
    two_count = 0
    three_count = 0

    for box in datafile:
        bocks = Counter(box)
        if 3 in bocks.values():
            three_count += 1
            if 2 in bocks.values():
                two_count += 1
        elif 2 in bocks.values():
            two_count += 1
        else:
            continue
    return two_count * three_count


checksum = calcChecksum()
print(checksum)