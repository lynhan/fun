"""
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
Given
    an initial state of all bulbs
Return
    the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.
Approach
    the total number of times each bulb will be flipped is the same no matter the order
        since two different bulbs next to each other means we must flip once
    so we can count the number of 0 and 1 segments starting from the first 0 and that will be the number of switches we have to press to turn on all bulbs
"""

def numpress(bulbs):
    if not bulbs:
        return 0
    count = 0
    prev = None
    for b in bulbs:
        if b != prev:
            count += 1
            prev = b
    if bulbs[0] == 1:
        count -= 1
    return count
