# Problem #1
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24], if our input was [3, 2, 1], the expected output would be [2, 3, 6]
# Follow-up what if we can’t use division

# Solution 1 - brute force - complexity n^2
print("Solution 1 - brute force")
arr = [1, 2, 3, 4, 5]
new_arr = []
for i in range(len(arr)):
    new_arr.append(1)
    for j in range(len(arr)):
        if i != j:
            new_arr[i] = new_arr[i] * arr[j]
print("\t" + str(new_arr))

# Solution 2 - mile and step - complexity n
print("Solution 2 - mile and step")
arr = [1, 2, 3, 4, 5]
product = 1
for item in arr:
    product *= item
new_arr = []
for item in arr:
    new_arr.append(int(product / item))
print("\t" + str(new_arr))

# Solution 3 - meta programming - complexity n
print("Solution 3 - meta programming")
arr = [1, 2, 3, 4, 5]
ltr = []
product = 1
for item in arr:
    product = product * item
    ltr.append(product)

rtl = []
product = 1
for item in reversed(arr):
    product = product * item
    rtl.append(product)
rtl.reverse()

new_arr = []
for i in range(len(arr)):
    if i == 0:
        new_arr.append(rtl[1])
        continue
    if i == len(arr) - 1:
        new_arr.append(ltr[len(arr) - 2])
        continue
    new_arr.append(ltr[i-1] * rtl[i+1])
print("\t" + str(new_arr))
