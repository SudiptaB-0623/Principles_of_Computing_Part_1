"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    -parameter line: array with elements
    -return: new array of elements after the merge operation
    """

    newline = shift(list(line))

    for index in range(len(newline)):
        if index + 1 < len(newline):
            if newline[index] != 0 \
                    and newline[index] == newline[index + 1] != 0:
                newline[index] *= 2
                newline[index + 1] = 0
                newline = shift(newline)

    return newline


def shift(array):
    """
    Function that removes the zeroes from array after it append them at the end
    -parameter array: elements list
    -return: new array of elements after the shift
    """

    total_zeros_counter = 0

    while True:
        zeros_counter = 0
        for index in range(len(array)):
            if array[index] == 0:
                del array[index]
                zeros_counter += 1
                break
        total_zeros_counter += zeros_counter

        if zeros_counter == 0:
            break

    for index in range(total_zeros_counter):
        array.append(0)

    return array
