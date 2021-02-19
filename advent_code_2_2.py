def find_matches():
    datafile = open('input-2.txt', 'r').readlines()
    boxes = []

    for line in datafile:
        st = line.strip()
        boxes.append(list(st))
    # now we have a list of 250 items

    for i in range(len(boxes) - 1):
        # compare item to all other items, but only if the index is larger
        for j in range(i + 1, len(boxes)):
            bewl = compare_boxes(boxes[i], boxes[j])
            if bewl:
                return ''.join(bewl)


def compare_boxes(box1, box2):
    count = 0
    answer = []
    # compare boxes[i], boxes[j]
    for l1, l2 in zip(box1, box2):
        if l1 != l2:
            count += 1
        elif count == 2:
            return False
        else:
            answer.append(l1)
    if count == 1:
        return answer


result = find_matches()
print(result)
