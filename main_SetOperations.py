from module_SetOperations import *
import random

if __name__ == "__main__":
  a = { i  for i in range(6) }
  print('Demonstrating add and remove')
  print(f'Set a = {a}')
  add_to_set(25, a)
  print(f'Added 25, new set a = {a}')
  add_to_set(3, a)
  remove_from_set(5, a)
  print(f'Removed 3, new set a = {a}')
  remove_from_set(27, a)

  print()

  a = set()
  add_to_set('apple', a)
  add_to_set('banana', a)
  add_to_set('orange', a)
  add_to_set('pear', a)
  add_to_set('apricot', a)

  b = set()
  add_to_set('papaya', b)
  add_to_set('watermelon', b)
  add_to_set('pear', b)
  add_to_set('grape', b)
  add_to_set('apricot', b)
  add_to_set('pineapple', b)

  print('Demonstrating union, intersection, difference,  symmetric difference, and set length')

  print(f'Set a = {a}')
  print(f'Length of set a = {set_length(a)}')
  
  print(f'Set b = {b}')
  print(f'Length of set b = {set_length(b)}')
  
  a_union_b, a_inter_b = union_and_intersection(a, b)
  print(f'Union of a and b = {a_union_b} and length is {set_length(a_union_b)}')
  print(f'Intersection of a and b = {a_inter_b} and length is {set_length(a_inter_b)}')
  
  a_diff_b = set_difference(a, b)
  print(f'Difference of a and b = {a_diff_b} and length of difference is {set_length(a_diff_b)}')
  
  a_symdiff_b = set_symmetric_difference(a, b)
  print(f'Symmetric difference of a and b = {a_symdiff_b} and length is {set_length(a_symdiff_b)}')

  print()

  print('Demonstrating checking subset')
  a = set([1])
  b = set([i for i in range(1, 11, 2)])
  c = set([1, 3, 5])

  if check_subset(a, b):
    print(f'Set a = {a} is a subset of set b = {b}')
  else:
    print(f'Set a = {a} is not a subset of set b = {b}')
  
  if check_subset(c, b):
    print(f'Set c = {c} is a subset of set b = {b}')
  else:
    print(f'Set c = {c} is not a subset of set b = {b}')

  if check_subset(set(), b):
    print(f'Empty set is a subset of set b = {b}')
  else:
    print(f'Empty set is not a subset of set b = {b}')

  if check_subset(c, set()):
    print(f'Set c = {c} is a subset of the empty set')
  else:
    print(f'Set c = {c} is not a subset of the empty set')

  print()
  print('Demonstrating power set and list of unique sets')

  a = set([1,2,3,4,5])

  print(f'Set a = {a}')
  print(f'Length of set a = {set_length(a)}')

  power_a = get_power_set(a)
  print(f'Power set of a = {power_a}')
  print(f'Length of power set of a = {set_length(power_a)}')

  print()
  unique_a = get_unique_subsets(a)
  print(f'Unique subsets of a = {power_a}')
  print(f'Length of list of unique subsets of a = {set_length(power_a)}')