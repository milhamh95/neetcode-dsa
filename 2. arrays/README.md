# Arrays

## RAM

- 1 Byte = 8 bits
- Bits -> position to store the digits 0 & 1
- bit -> bits -> byte -> RAM -> data structure
- element in array data type ex -> int 32 bit, int 64 bit, float 32 bit, float64 bit, string, etc.

```
[1,3,5] -> array data type = int 32 bit

1 -> will be represent in bit -> ________ _________ _________ _________1
```

![Array in RAM](https://i.ibb.co/XbcpfZW/array.png)

## Static Arrays

```
index = [1,3,5]
```

- array start from index 0, ex: `index[0]`
- size is fixed. can't be changed
- found in static typed language

### Time Complexity

- Read = `O(1)` -> using index
- Check all element = `O(N)`
- Replace element = `O(1)` -> using index
- Insert & Remove middle element = `O(N)`
- Insert & Remove End = `O(1)`

### Space Complexity

- O(1) -> because array is fixed size

## Dynamic Array

- To solve static arrays
- Example: Java List, Go Slice, Rust vector. Don't need to specify the size

### How Dynamic Arrays works

These are the step to generate dynamic arrays

```
original array = [1,2,3]
to be array = [1,2,3,4,5,6]
```

1. Allocate new slice with the size double (or multiple by growth factor depend on programming language) from original array

Time complexity = `O(n)`

![Allocate Dynamic Arrays](https://i.ibb.co/GHMNnX3/1-allocate.png)

2. Copy element from original array to new array

Time complexity = `O(n)`

![Copy element from original array to new array](https://i.ibb.co/5vGbDWv/2-copyelement.png)

3. Insert new element to new array

Time complexity = `O(1)` -> because the space already available from step 1

![Insert new element to new array](https://i.ibb.co/X4XP5Gg/3-insertelement.png)

### Why don't we allocate new slice with the size triple / 50 / 100?

It will use too much memory and there are a lot of unused space. It will make the program slow

![Allocate too much space](https://i.ibb.co/HrmHpkc/allocate-large-spice.png)

### Why don't we allocate a new single space every element we insert?

The number of allocation is too much. Because we need to repeat

- Allocate new space for new array -> O(n)
- Copy element from original array to new array -> O(n)
- Insert element to new array -> O(1)

equal with number of element that we want to insert.

If there are `n` element we want to insert, time complexity will be:

```
n (O(n) * O(n) * O(1))
```

ex:

```
n = 6

6 (O(6) * O(6) * O(1))
```

Allocate for new space for new array is expensive.

### Time Complexity

- Read / write with index element = `O(1)`
- Insert / remove end = `O(1)`
- Insert middle = `O(n)`
- Remove middle = `O(n)`
