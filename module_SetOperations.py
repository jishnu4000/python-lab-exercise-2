# Question 2

# a 
def add_to_set(elem, setObj):
  if elem not in setObj:
    setObj.add(elem)
  else:
    print(f'{elem} is already present in the set {setObj}.')

# b
def remove_from_set(elem, setObj):
  if elem in setObj:
    setObj.remove(elem)
  else:
    print(f'{elem} is not present in the set {setObj}.')

# c
def union_and_intersection(set1, set2):
  if set1 == set():
    return set2, set()
  elif set2 == set():
    return set1, set()
  else:
    return set1.union(set2), set1.intersection(set2)

# d
def set_difference(set1, set2):
  if set1 == set():
    return set()
  elif set2 == set():
    return set1
  else:
    return set1.difference(set2)
  
# e
def check_subset(set1, set2):
  if set1 == set():
    return True
  elif set2 == set():
    return False
  else:
    return set1.issubset(set2)

# f
def set_length(setObj):
  set_length = 0
  for i in setObj:
    set_length += 1
  return set_length

# g
def set_symmetric_difference(set1, set2):
  return set1.symmetric_difference(set2)

# h
def get_power_set(setObj):
  setObj_list = list(setObj)
  power_set_length = len(setObj)
  power_set_output = []
  
  # loop for 2^n subsets
  for i in range(2 ** power_set_length):
    set_subset = set()
    for j in range(power_set_length):
      if i & (1 << j):
        set_subset.add(setObj_list[j])
  
    power_set_output.append(set_subset)
  
  return power_set_output

# i
def get_unique_subsets(setObj):
  def backtrack(start, current_subset):
    # Add the current subset to the result
    result.append(set(current_subset))

    for i in range(start, len(set_items)):
      # Include set_items[i] in the current subset
      current_subset.append(set_items[i])

      # Recursion with the next start index
      backtrack(i + 1, current_subset)
      
      # Exclude set_items[i] from the current subset (backtrack)
      current_subset.pop()
  
  set_items = list(setObj)
  result = []
  backtrack(0, [])
  return result