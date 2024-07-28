def maximum_value(arr):
  return max(arr)

def minimum_value(arr):
  return min(arr)

def list_sum(arr):
  return sum(arr)

def list_average(arr):
  return sum(arr)/len(arr)

def list_median(arr):
  arr.sort()
  if len(arr) % 2 != 0:
    middle = len(arr) // 2
    return arr[middle]
  else:
    middle = len(arr) // 2
    return (arr[middle-1] + arr[middle]) / 2