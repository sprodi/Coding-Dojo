# 1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element). 
def countdown(num):
   for i in range(num, -1, -1):
      print(i)
countdown(5)

# 2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printReturn(arr):
   print(arr[0])
   return arr[1]
printReturn([1,2])

# 3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def firstPlusLength(arr):
   return arr[0] + len(arr)
firstPlusLength([1,2,3,4,5])

# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
def values_greater_than_second(arr):
   newArr = []
   if len(arr) < 3:
      return False
   for i in range(0, len(arr)):
      if arr[i] > arr[1]:
         newArr.append(arr[i])
   print(len(newArr))
   return newArr
values_greater_than_second([9,5,1,2,6,5])
values_greater_than_second([5,2])
values_greater_than_second([5,2,3,2,1,4])

# 5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_and_value(amount, num):
   newArr = []
   for i in range(0, amount):
      newArr.append(num)
   return newArr
length_and_value(4,7)
length_and_value(6,2)
