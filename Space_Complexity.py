#---------------------
# Space Complexity
#----------------------

# What is Space Complexity?
#--------------------------------
# Space Complexity is the amount of memory an algorithm uses as the input size (n) grows.


# It includes:
#---------------------------------------------------
# Input Space → Memory needed to store the input.
# Auxiliary Space → Extra memory used by the algorithm.

# In interviews, when people ask for Space Complexity, they usually mean Auxiliary Space.


# Rules for Space Complexity:
#-------------------------------------

# Rule 1: No Extra Variables → O(1)
#-------------------------------------
# a = 10
# b = 20
# c = a + b

# Only a fixed number of variables.

# Space Complexity:
# O(1)


# Rule 2: One Array of Size n → O(n)
#-------------------------------------
# temp = [0] * n
# If n = 5

# [0,0,0,0,0]

# If n = 1000
# 1000 elements

# Memory grows with n.

# Space Complexity:
# O(n)


# Rule 3: Two Arrays of Size n → O(n)
#-------------------------------------
# a = [0] * n
# b = [0] * n

# Memory:
# n + n = 2n
# Drop constants:
# O(n)


# Rule 4: 2D Matrix → O(n²)
#-------------------------------------
# matrix = [[0]*n for _ in range(n)]

# Example:
# n x n
# Total cells:
# n²

# Space Complexity:
# O(n²)


# Rule 5: Dictionary / Hash Map
#-------------------------------------
# seen = {}

# Example:

# for num in nums:
#     seen[num] = 1

# Worst case stores all n elements.

# O(n)

# This is why your Two Sum hash map solution has:
# Space Complexity = O(n)


# Rule 6: Set
#-------------------------------------
# s = set()

# Example:

# for num in nums:
#     s.add(num)

# Stores up to n values.
# O(n)


# Rule 7: Recursion
#-------------------------------------
# Every recursive call is stored in the call stack.

# Example:

# def fun(n):
#     if n == 0:
#         return
#     fun(n-1)

# Call stack:

# fun(5)
# fun(4)
# fun(3)
# fun(2)
# fun(1)
# fun(0)

# Total:
# n calls

# Space Complexity:
# O(n)


# Rule 8: Binary Search (Iterative)
#-------------------------------------
# while low <= high:

# Uses only:

# low
# high
# mid

# Fixed variables.

# Space Complexity:
# O(1)


# Rule 9: Binary Search (Recursive)
#-------------------------------------
# def bs(low, high):

# Call stack grows:

# log n

# Space Complexity:
# O(log n)


# Common Examples
#-------------------------------------
# Algorithm	Space Complexity
# Linear Search	O(1)
# Binary Search (Iterative)	O(1)
# Binary Search (Recursive)	O(log n)
# Bubble Sort	O(1)
# Selection Sort	O(1)
# Insertion Sort	O(1)
# Merge Sort	O(n)
# Quick Sort (average)	O(log n)
# Hash Map Two Sum	O(n)
# BFS	O(n)
# DFS Recursive	O(n)


# How to Find Space Complexity Quickly
#-------------------------------------

# Question 1
#-------------------------------------
# Did you create a new array/list/set/dictionary?

# temp = []
# seen = {}

# If yes:
# Usually O(n)

# Question 2
#-------------------------------------
# Are you only using a few variables?

# i = 0
# j = 0
# sum = 0

# Then:
# O(1)


# Question 3
#-------------------------------------
# Are you using recursion?

# Count the maximum depth of recursive calls.

# Depth n  -> O(n)
# Depth log n -> O(log n)
# Example: Your Two Sum Hash Map
# seen = {}

# for i in range(len(nums)):
#     ...
#     seen[nums[i]] = i

# Stores up to all elements.

# Space Complexity = O(n)

# Example: Two Pointer Solution
# i = 0
# j = len(nums)-1

# while i < j:

# Only uses:

# i
# j
# sum

# No extra data structure.

# Space Complexity = O(1)


# Easy Interview Formula
#-------------------------------------
# Extra array/list/set/dictionary of size n → O(n)
# Only variables (i, j, temp) → O(1)
# Recursive depth n → O(n)
# Recursive depth log n → O(log n)
# n × n matrix → O(n²)

