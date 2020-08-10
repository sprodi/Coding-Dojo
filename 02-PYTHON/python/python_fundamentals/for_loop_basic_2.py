# 1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(list):
   for i in range(0, len(list)):
      if list[i] > 0:
         list[i] = 'big'
   return list
# print(biggie_size([-1,3,5,-5]))

# 2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def count_positives(list):
   count = 0
   for i in range(0, len(list)):
      if list[i] > 0:
         count += 1
   list[-1] = count
   return list
# print(count_positives([-1,1,1,1]))
# print(count_positives([1,6,-4,-2,-7,-2]))

# 3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(list):
   sumTotal = 0
   for i in range(0, len(list)):
      sumTotal += list[i]
   return sumTotal
# print(sum_total([1,2,3,4]))
# print(sum_total([6,3,-2]))

# 4 Average - Create a function that takes a list and returns the average of all the values.
def average(list):
   sumTotal = 0
   for i in range(0, len(list)):
      sumTotal += list[i]
   return sumTotal / len(list)
# print(average([1,2,3,4]))

# 5 Length - Create a function that takes a list and returns the length of the list.
def length(list):
  return len(list)
# print(length([37,2,1,-9]))
# print(length([]))

# 6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
   if len(list) == 0:
      return False
   else:
      minVal = list[0]
      for i in range(len(list)):
         if list[i] < minVal:
            minVal = list[i]
      return minVal
# print(minimum([37,2,1,-9]))
# print(minimum([2,-5,6,2]))
# print(minimum([]))

# 7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(list):
   if len(list) == 0:
      return False
   else:
      maxVal = list[0]
      for i in list:
         if i > maxVal:
            maxVal = i
      return maxVal
# print(maximum([37,2,1,-9]))
# print(maximum([2,-5,6,2]))
# print(maximum([]))

# 8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analysis(list):
   sum = sum_total(list)
   avg = average(list)
   min = minimum(list)
   max = maximum(list)
   len = length(list)
   dict = {
      'sumTotal': sum,
      'average': avg,
      'minimum': min,
      'maximum': max,
      'length': len
   }
   return dict
print(ultimate_analysis([37,2,1,-9]))

# 9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse_list(list):
   newList = []
   for i in range(1, len(list)+1):
     newList.append(list[-i])
   return newList
# print(reverse_list([37,2,1,-9]))