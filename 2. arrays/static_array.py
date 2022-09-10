def printArr(arr, capacity):
    # for i in range(capacity):
    #     print(arr[i])

    print("capacity = ", capacity)

    for idx, ele in enumerate(arr):
        print(f"index = {idx}, element = {ele}")

# Insert n into arr at the next open position
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array)
# similar to append
def insertEnd(arr, n , length, capacity):
    if length < capacity:
        arr[length - 1] = n

# Remove from the last position in the array if the array
# is not empty
def removeEnd(arr, length):
    if length > 0:

        # overwrite last element with some default value
        # we would also decreased the length array by 1
        arr[length - 1] = 0

# Insert n into index i after shifting elements to the right
# i is valid
# arr = [1,2,3,4,5,0]
# arr = [1,2,100,3,4,5]
def insertMiddle(arr, i, n, length):
    for idx in range(length - 1, i , - 1):
        arr[idx + 1] = arr[idx]

    arr[i] = n

# Remove value at index i before shifting elements to the left
# i is valid
# arr = [1,2,100,3,4,5]
# arr = [1,2,3,4,5,0]
def removeMiddle(arr, i, length):
    for idx in range(i, length - 1, 1):
        arr[idx] = arr[idx + 1]

    arr[length - 1] = 0

printArr([1,2,3], 3)
