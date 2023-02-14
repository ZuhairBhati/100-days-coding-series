# Mahesh got a beautiful array named A as a birthday gift from his beautiful girlfriend Namratha. There are N positive integers in that array. Mahesh loved the array so much that he started to spend a lot of time on it everyday. One day, he wrote down all possible subsets of the array. Then for each subset, he calculated the sum of elements in that subset and wrote it down on a paper. Unfortunately, Mahesh lost the beautiful array :(. He still has the paper on which he wrote all subset sums. Your task is to rebuild beautiful array A and help the couple stay happy :)

# Input

# The first line of the input contains an integer T denoting the number of test cases. First line of each test case contains one integer N, the number of elements in A. Second line of each test case contains 2^N integers, the values written on paper

# Output

# For each test case, output one line with N space separated integers in non-decreasing order.

# Sample Input

# 2

# 1

# 0 10

# 2

# 0 1 1 2

# Sample Output

# 10

# 1 1


def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, mid+1, r, x)
        else:
            return binarySearch(arr, l, mid-1, x)
    else:
        return -1
for _ in range(int(input().strip())):
    n = int(input().strip())
    sub_sums_list = list(map(int, input().strip().split()))
    sub_sums = sorted(sub_sums_list, reverse = True)
    sub_sums.pop()
    original_set = []
    to_be_removed = []

    while len(original_set) < n:
        element = sub_sums.pop()
        original_set.append(element)
        will_be_removed = [element]
        for rem_val in to_be_removed:
            new_rem_val = rem_val + element
            will_be_removed.append(new_rem_val)
            idx = binarySearch(sub_sums, 0, len(sub_sums) - 1, new_rem_val)
            sub_sums.pop(idx)
        to_be_removed += will_be_removed

    print(*sorted(original_set),sep = " ")

