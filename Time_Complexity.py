
# Time & Space Complexity - DSA Series by Shradha Ma'am (YouTube - Apna College)
# https://youtu.be/PwKv8fOcriM?si=dq9t8-I-VfCrSsGu

# DSA Patterns Episode 6 - What If You Could Master Time Complexity in Just 30 Minutes? (YouTube: Padho with Pratyush)
# https://youtu.be/oFwHwCkSoGw?si=kdlWvnPoYSZ6_5d7


#---------------------
# Time Complexity :
#----------------------

# Time Complexity measures how the running time of an algorithm grows as the input size (n) increases.

# It does not measure actual time in seconds. Instead, it measures the number of operations performed.


### Why Time Complexity is Important ###
#-----------------------------------
# Suppose you have two programs:

# Program A
#-------------
# for i in range(n):
#     print(i)

# Operations ≈ n


# Program B
#-------------
# for i in range(n):
#     for j in range(n):
#         print(i, j)

# Operations ≈ n × n = n²

# If n = 10
# Program A → 10 operations
# Program B → 100 operations

# If n = 1000
# Program A → 1000 operations
# Program B → 1,000,000 operations

# As input grows, Program B becomes much slower.


### Big O Notation ###
#-----------------------------------
# We represent complexity using Big O notation.

# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n²)
# O(n³)
# O(2ⁿ)
# O(n!)


# 1. O(1) — Constant Time
#----------------------------------
# Execution time remains the same regardless of input size.

# Example
# arr = [10,20,30,40]
# print(arr[2])

# Only one operation.

# Complexity
# O(1)


# 2. O(log n) — Logarithmic Time
#------------------------------------
# Input size keeps reducing by half.

# Example: Binary Search
# arr = [10,20,30,40,50,60,70]
# target = 50
# low = 0
# high= len(arr)-1

# while low <= high:
#     mid = (low + high)//2

#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         low = mid + 1
#     else:
#         high = mid - 1

# Each step removes half the elements.

# Example
# For 16 elements:
# 16 → 8 → 4 → 2 → 1
# Only 4 steps.

# Complexity
# O(log n)


# 3. O(n) — Linear Time
#-------------------------------------
# Loop runs proportional to input size.

# Example
# for i in range(n):
#     print(i)
# Dry Run

# If
# n = 5
# Loop executes:
# 0
# 1
# 2
# 3
# 4

# 5 times.

# Complexity
# O(n)
# 4. O(n log n)

# Common in efficient sorting algorithms.

# Examples
# Merge Sort
# Heap Sort
# Quick Sort (average case)
# Complexity
# O(n log n)


# 5. O(n²) — Quadratic Time
#--------------------------------

# Nested loops.
# Example
# for i in range(n):
#     for j in range(n):
#         print(i,j)


# Dry Run
# For
# n = 3

# Operations:
# (0,0)
# (0,1)
# (0,2)

# (1,0)
# (1,1)
# (1,2)

# (2,0)
# (2,1)
# (2,2)

# Total:
# 3 × 3 = 9


# Complexity
# O(n²)


# 6. O(n³)
#------------------------
# Three nested loops.

# Example
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             print(i,j,k)

# Complexity
# O(n³)


# 7. O(2ⁿ) — Exponential Time
#---------------------------------
# Every element has two choices.

# Example
# Recursive Fibonacci

# def fib(n):
#     if n <= 1:
#         return n

#     return fib(n-1) + fib(n-2)
# Complexity
# O(2ⁿ)

# Very slow.


# 8. O(n!)
#-------------------------
# Worst complexity.

# Example
# Generating all permutations.
# from itertools import permutations
# permutations(arr)

# Complexity
# O(n!)


# Complexity Order (Best → Worst)
#-----------------------------------
# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n²)
# O(n³)
# O(2ⁿ)
# O(n!)


# Time Complexity of Common Python Operations
#---------------------------------------------
# | Operation           | Complexity   |
# | ------------------- | ------------ |
# | Access list element | O(1)         |
# | Append list         | O(1)         |
# | Insert at beginning | O(n)         |
# | Delete from middle  | O(n)         |
# | Search in list      | O(n)         |
# | Dictionary lookup   | O(1) Average |
# | Set lookup          | O(1) Average |
# | Sorting             | O(n log n)   |

