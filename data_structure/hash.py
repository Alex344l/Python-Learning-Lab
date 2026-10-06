
def isSubset(a, b):

    hash_set = set(a)

    for num in b:
        if num not in hash_set:
            return False

    return True


if __name__ == "__main__":

    a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    b = [1, 2, 3, 4, 5, 6, 7]

    if isSubset(a, b):
        print("TRUE")
    else:
        print("FALSE")

