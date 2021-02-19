def parse_data():
    datafile = open('input-3.txt', 'r').readlines()
    patch_list = []  # a list of patch information
    coord = []  # a list of x,y coordinates for the origin of patches
    wh_pairs = []

    for line in datafile:
        sq = line.strip()
        patch = (sq.split(" "))
        patch_list.append(patch)

    for patch in patch_list:
        xy = patch[2].strip(":")
        xy_tuple = tuple(xy.split(","))
        coord.append(xy_tuple)

        wh = patch[3]
        wh_tuple = tuple(wh.split("x"))
        wh_pairs.append(wh_tuple)

    zipd = list(zip(coord, wh_pairs))
    return zipd


def look_for_overlap(zipd):
    patch_block = set()
    doubles = set()
    for patch in zipd:
        x_values, y_values = make_pairs(patch)
        for x_value in x_values:
            for y_value in y_values:
                tup = x_value, y_value
                # we don't want to count a square more than once if it's in more than two patches
                if tup in patch_block:
                    doubles.add(tup)
                else:
                    patch_block.add(tup)
    return len(doubles)


def make_pairs(patch):
    x = int(patch[0][0])
    y = int(patch[0][1])
    w = int(patch[1][0])
    h = int(patch[1][1])
    x_values = []
    y_values = []
    for num in range(w):
        x_values.append(x + num)
    for num in range(h):
        y_values.append(y + num)
    return x_values, y_values


zipd_data = parse_data()
print(look_for_overlap(zipd_data))
