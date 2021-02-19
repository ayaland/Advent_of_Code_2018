from advent_code_3_1 import parse_data, make_pairs
# parse_data returns list of (x, y) and (w, h) tuples as each item
# note this data is in str form
# [
#   ((x1, y1), (w1, h1)),
#   ((x2, y2), (w2, h2))
# ]
import itertools


def look_for_overlap():
    zipd_data = parse_data()
    patches = compare_patch(zipd_data)
    overlap_patches = []

    for patch1, patch2 in itertools.combinations(patches, 2):
        # every combination of two patches
        overlap = patch1.intersection(patch2)
        if len(overlap) != 0:
            if patch1 not in overlap_patches:
                overlap_patches.append(patch1)
            if patch2 not in overlap_patches:
                overlap_patches.append(patch2)

    patch = [x for x in patches if x not in overlap_patches]
    get_id(patch, zipd_data)


def compare_patch(zipd):
    # makes list of all (x, y) coordinates for patch item in patches set
    # returns a list of sets of all coords for each patch
    patches = []
    for patch in zipd:
        coords = set()
        x_values, y_values = make_pairs(patch)
        for x in x_values:
            for y in y_values:
                tup = x, y
                coords.add(tup)
        if coords not in patches:
            patches.append(coords)
    return patches


def get_id(patch, zipd_data):
    unpack = []
    for thingset in patch:
        for thingtuple in thingset:
            unpack.append(thingtuple)
    print(sorted(unpack))
    # str_origin = tuple(str(val) for val in origin)
    # for thing in zipd_data:
    #     if thing[0] == str_origin:
    #         return zipd_data.index(thing) + 1


answer = look_for_overlap()
print(answer)
