from module_question_3 import *

if __name__ == '__main__':
  print('Demonstrating merging.')
  dict1 = {'a':1, 'b':2, 'c':3, 'd':4,}
  dict2 = {'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,}
  dict3 = {'apple':45, 'banana':36}

  for i,d in enumerate([dict1, dict2, dict3]):
    print(f'Dictionary {i+1}: {d}')

  print(f'Merged dictionary: {merging_Dict(dict1, dict2, dict3)}')

  print()
  print('Demonstrating finding common keys.')
  dict1 = {'a':1, 'b':2, 'c':3, 'd':4,}
  dict2 = {'e':5, 'a':6, 'g':7, 'c':8, 'i':9, 'j':10,}
  dict3 = {'k':11, 'l':12, 'a':13, 'n':14, 'c':15}

  for i,d in enumerate([dict1, dict2, dict3]):
    print(f'Dictionary {i+1}: {d}')

  print(f'Set of common keys: {common_Keys(dict1, dict2, dict3)}')

  print()
  print('Demonstrating inverting a dictionary.')

  dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'apple':1, 'banana':2, 'orange':49,}

  print(f'Dictionary before inversion: {dict1}')
  print(f'Dictionary after inversion: {invert_Dict(dict1)}')

  print()
  print('Demonstrating finding common key-value pairs in multiple dictionaries.')

  dict1 = {'a':1, 'b':2, 'c':3, 'hundred':100,'d':4,}
  dict2 = {'e':5, 'a':1, 'g':7, 'c':3, 'i':9, 'j':10, 'hundred':100,}
  dict3 = {'hundred':100, 'k':11, 'l':12, 'a':1, 'n':14, 'c':3}

  for i,d in enumerate([dict1, dict2, dict3]):
    print(f'Dictionary {i+1}: {d}')

  print(f'Set of common key-value pairs: {common_Pairs(dict1, dict2, dict3)}')
