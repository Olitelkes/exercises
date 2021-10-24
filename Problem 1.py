# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def add_list(list,k):
    for x in list[:-1]:
        for element in list:
            y = x + element
            if y == k:
                print (str(x) + ' + ' + str(element) + ' = ' + str(y))


if __name__ == '__main__':
    add_list([10, 13, 15, 7],17)