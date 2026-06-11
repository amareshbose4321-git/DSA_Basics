
#------------------
# Sliding Window
#------------------

# The Sliding Window technique is one of the most important patterns for coding interviews and DSA. It is mainly used for problems involving subarrays or substrings.

# What is Sliding Window?
# Instead of checking every possible subarray (which is usually O(n²)), we maintain a window and move it through the array/string.

# Think of it like a window that slides from left to right.
# Example:

# arr = [1, 2, 3, 4, 5]
# k = 3

# Window 1: [1, 2, 3]
# Window 2: [2, 3, 4]
# Window 3: [3, 4, 5]

# Types of Sliding Window
#-----------------------------

# 1. Fixed Size Window

# The window size is given.

# Example:

# Maximum sum of subarray of size k
# Average of every subarray of size k
# Brute Force
# arr = [1,2,3,4,5]
# k = 3

# max_sum = 0

# for i in range(len(arr)-k+1):
#     current = sum(arr[i:i+k])
#     max_sum = max(max_sum, current)

# print(max_sum)

# Time Complexity = O(n*k)


# Optimized Sliding Window
# arr = [1,2,3,4,5]
# k = 3

# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k, len(arr)):
#     window_sum += arr[i]
#     window_sum -= arr[i-k]

#     max_sum = max(max_sum, window_sum)

# print(max_sum)

# Time Complexity = O(n)


# 2. Variable Size Window

# Window size changes according to condition.

# Example:

# Longest substring without repeating characters
# Smallest subarray with sum ≥ target

# Pattern:

# left = 0

# for right in range(len(arr)):

#     # Expand window
#     ...

#     while condition:
#         # Shrink window
#         left += 1
# Fixed Window Template
# window = 0
# k = ...

# for i in range(k):
#     window += arr[i]

# for right in range(k, len(arr)):
#     window += arr[right]
#     window -= arr[right-k]
# Variable Window Template
# left = 0

# for right in range(len(arr)):

#     # include current element

#     while invalid_condition:
#         # remove left element
#         left += 1

#     # update answer


# How to Identify Sliding Window?

# Use Sliding Window when you see:

# Arrays
# Subarray
# Continuous elements
# Contiguous segment

# Example:

# ❌ Any 3 numbers

# ✅ 3 consecutive numbers

# Strings
# Substring
# Consecutive characters

# Example:

# ✅ Longest substring
# ✅ Minimum window substring

# Common LeetCode Problems
# Easy
# Move Zeroes
# Maximum Average Subarray I
# Contains Duplicate II
# Medium
# Longest Substring Without Repeating Characters
# Permutation in String
# Fruit Into Baskets
# Longest Repeating Character Replacement
# Hard
# Minimum Window Substring
# Sliding Window Maximum
# Difference Between Two Pointers and Sliding Window
# Two Pointers

# Pointers move independently.

# Example:

# left = 0
# right = len(arr)-1

# while left < right:
#     ...

# Used in:

# Two Sum II
# Container With Most Water
# 3Sum
# Sliding Window

# Pointers represent a window.

# left = 0

# for right in range(len(arr)):
#     ...

#     while condition:
#         left += 1

# Used in:

# Longest substring
# Maximum subarray
# Minimum window