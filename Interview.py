def print_pairs(arr, N):
    # hash set
    hash_set = set()

    for i in range(0, len(arr)):
        val = N - arr[i]
        if (val in hash_set):  # check if N-x is there in set, print the pair
            print("Pairs " + str(arr[i]) + ", " + str(val))
        hash_set.add(arr[i])


# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 5
print_pairs(arr, N)


from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
new_dict = Counter(d1) + Counter(d2)
print(new_dict)
