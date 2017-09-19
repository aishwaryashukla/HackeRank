print("Hello Aishwarya ")
n = "2 3 6 6 5"
arr = list(set(map(int, n.split())))
arr.sort(reverse=True)
print(arr[1])