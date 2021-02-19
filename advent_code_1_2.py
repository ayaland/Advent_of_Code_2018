def find_repeat():

    # declare var frequency and an empty set
    datafile = open('input.txt', 'r').readlines()  # this is a list
    frequency = 0
    frequencies = set()

    # loop through input.txt, add to frequency
    # append frequency to list
    # break loop if match
    # otherwise repeat
    while True:
        for item in datafile:
            frequency += int(item)
            if frequency in frequencies:
                return frequency
            else:
                frequencies.add(frequency)


freq = find_repeat()
print(freq)
