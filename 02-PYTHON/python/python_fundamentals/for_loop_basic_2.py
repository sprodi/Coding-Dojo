# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(lst):
   for i in range(0, len(lst)):
      if lst[i] > 0:
         lst[i] = 'big'
   return lst
# biggie_size([-1,3,5,-5])

# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(lst):
   count = 0
   for i in range(0, len(lst)):
      if lst[i] > 0:
         count += 1
   lst[-1] = count
   return lst
# count_positives([-1,1,1,1])
# count_positives([1,6,-4,-2,-7,-2])

# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(lst):
   sumTotal = 0
   for i in range(0, len(lst)):
      sumTotal += lst[i]
   return sumTotal
# sum_total([1,2,3,4])
# sum_total([6,3,-2])

# 4 Average - Create a function that takes a list and returns the average of all the values.
def average(lst):
   sumTotal = 0
   for i in range(0, len(lst)):
      sumTotal += lst[i]
   return sumTotal / len(lst)
# average([1,2,3,4])

# 5 Length - Create a function that takes a list and returns the length of the list.
def length(lst):
  length = 0
  for i in range(0, len(lst)):
    if i < len(lst):
      length += 1
  return length
# length([37,2,1,-9])
# length([])

# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(lst):
   minVal = lst[0]
   if len(lst) == 0:
      return False
   for i in lst:
      if i < minVal:
         minVal = i
   return minVal
# minimum([37,2,1,-9])
# minimum([2,-5,6,2])
# minimum([])

# 7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(lst):
   maxVal = lst[0]
   if len(lst) == 0:
      return False
   for i in lst:
      if i > maxVal:
         maxVal = i
   return maxVal
# maximum([37,2,1,-9])
# maximum([2,-5,6,2])
# maximum([])

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(lst):
   sum = sum_total(lst)
   avg = average(lst)
   min = minimum(lst)
   max = maximum(lst)
   len = length(lst)
   dict = {
      'sumTotal': sum,
      'average': avg,
      'minimum': min,
      'maximum': max,
      'length': len
   }
   print(dict)
# ultimate_analysis([37,2,1,-9])

# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(lst):
   newList = []
   for i in range(1, len(lst)+1):
     newList.append(lst[-i])
   return newList
# reverse_list([37,2,1,-9])