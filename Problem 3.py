# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_missing_int_pos(mylist):
    mylist.sort()
    newlist = []
    for x in mylist:
        if x > 0:
            newlist.append(x)
        newlist = list(dict.fromkeys(newlist))

    y = 1
    count = 0
    for z in newlist:
        count = count + 1
        if y == z:
            y = y + 1
        else:
            break
    print(y)


if __name__ == '__main__':
    find_missing_int_pos([3, 4, -1, 1])
    find_missing_int_pos([1, 2, 0])
