#--------------------------
# Two Pointer Technique 
#---------------------------

# The Two Pointer Technique is an algorithmic approach where you use two indices (pointers) to traverse an array, string, or linked list. It often reduces the time complexity from O(n²) to O(n).


### Why use Two Pointers? ### 
#------------------------------------
# Instead of checking every pair of elements using nested loops:

# Example:
# for i in range(n):
#     for j in range(i+1, n):
#         ...

# which takes O(n²) time,

# you use two pointers:

# Example:
# left = 0
# right = n - 1

# and move them intelligently, often achieving O(n) time.


### Types of Two Pointer Problems: ### 
#------------------------------------

# 1. Opposite Direction Pointers:
# One pointer starts from the beginning and the other from the end.

# left = 0
# right = len(arr) - 1

# Example: Two Sum in Sorted Array
#------------------------------------
# arr = [1, 2, 4, 6, 10]
# target = 8

# left = 0
# right = len(arr) - 1

# while left < right:

#     s = arr[left] + arr[right]

#     if s == target:
#         print(left, right)
#         break

#     elif s < target:
#         left += 1

#     else:
#         right -= 1


# Output:
#--------------------
# [2,6]


# 2. Same Direction Pointers
# Both pointers move from left to right.

# Example: Move All Zeros to End
#------------------------------------

# arr = [1,0,2,0,3,4,0,5]

# j = 0

# for i in range(len(arr)):

#     if arr[i] != 0:

#         arr[j], arr[i] = arr[i], arr[j]

#         j += 1

# print(arr)

# Output:
#--------------------
# [1,2,3,4,5,0,0,0]

# How it works
#---------------------
# i scans every element.
# j points to the next position for a non-zero element.


# 3. Fast and Slow Pointer
# Mostly used in linked lists.

# Example
#--------------------------
# slow = head
# fast = head

# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

# Uses
#---------------------------
# Find middle node
# Detect cycle
# Find loop start


# 4. Sliding Window (Special Two Pointer)
# Used for subarrays and substrings.

# left = 0

# for right in range(n):

#     while condition:
#         left += 1

# Example
#-----------------------------
# Find longest substring without repeating characters.
# Both pointers move in the same direction.



### How to Identify Two Pointer Problems ### 
#-------------------------------------------

# Look for these clues:

# Clue 1: Sorted Array
#-------------------------------------------
# Questions like:
#------------------
# Two Sum II
# Pair with target sum
# Triplet sum

#**Usually use opposite pointers.**


# Clue 2: Pair Search
#-------------------------------------------
# Quetions asking:
#-------------------
# Find pair
# Find triplet
# Closest pair

#**Often use two pointers.**


# Clue 3: Remove or Rearrange Elements
#-------------------------------------------
# Questions like:
#-----------------
# Move zeros
# Remove duplicates
# Sort colors

#** Usually use same-direction pointers.**


# Clue 4: Subarray / Substring
#-------------------------------------------
# Questions asking:
#-----------------
# Longest
# Smallest
# Continuous segment

#** Usually use sliding window.**


# Clue 5: Linked List
#-------------------------------------------
# Questions asking:
#-----------------
# Middle node
# Cycle detection



# Common LeetCode Problems
#-------------------------------------------
# Two Sum II
# Valid Palindrome
# Remove Duplicates from Sorted Array
# Container With Most Water
# Trapping Rain Water
# Move Zeroes
# Sort Colors
# 3Sum
# Middle of Linked List
# Linked List Cycle