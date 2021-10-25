# Given an array of integers, return a new array such that each element at index i of the
# new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def add_list(mylist):
    reslist = []
    for x in mylist:
        res = 1
        i = 0
        for y in mylist:
            if mylist.index(x) != i:
                res = y * res
            i = i + 1
        reslist.append(res)
    print(reslist)


if __name__ == '__main__':
    add_list([1, 2, 3, 4, 5])
    add_list([3, 2, 1])
    
# Output : [120, 60, 40, 30, 24]
           [2, 3, 6]
