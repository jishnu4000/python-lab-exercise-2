# Question 1

# a) i
def maximum_value(arr):
  return max(arr)

# a) ii
def minimum_value(arr):
  return min(arr)

# a) iii
def list_sum(arr):
  return sum(arr)

# a) iv
def list_average(arr):
  return sum(arr)/len(arr)

# a) v
def list_median(arr):
  arr.sort()
  if len(arr) % 2 != 0:
    middle = len(arr) // 2
    return arr[middle]
  else:
    middle = len(arr) // 2
    return (arr[middle-1] + arr[middle]) / 2