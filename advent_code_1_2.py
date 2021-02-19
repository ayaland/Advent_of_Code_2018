# declare var frequency and an empty set

# loop through input.txt, add to frequency
# append frequency to list
# break loop if match
# otherwise repeat


def findRepeat():

    datafile = open('input.txt', 'r').readlines()  # this is a list
    frequency = 0
    frequencies = set()

    while True:
        for item in datafile:
            frequency += int(item)
            if frequency in frequencies:
                return frequency
            else:
                frequencies.add(frequency)

    # while x < 10:
    #     print(datafile)
    #     for line in datafile:
    #         if frequency not in frequencies:
    #             frequency += int(line) # adds line to total
    #             frequencies.append(int(frequency)) # adds total to list
    #         else:
    #             print(x)
    #             return frequency
    #     x += 1

#     #     frequency += int(line)
#     #     if frequency in frequencies:
#     #         print("SDLFHASLIFUSHDFLEFUGH")
#     #         flag = true
#     #         break
#     #     else:
#     #         frequencies.append(int(frequency))
#     # return frequency

freq = findRepeat()
print(freq)