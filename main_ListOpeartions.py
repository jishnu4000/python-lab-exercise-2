from module_ListFunction import *
import random

if __name__ == "__main__":
  # List of numbers from 1 to 10
  list_1_to_10 = [i for i in range(1, 11)]

  print('Numbers 1 to 10')

  print(f'Max Value: {maximum_value(list_1_to_10)}')
  print(f'Min Value: {minimum_value(list_1_to_10)}')
  print(f'Sum of List: {list_sum(list_1_to_10)}')
  print(f'Average of List: {list_average(list_1_to_10)}')
  print(f'Median of List: {list_median(list_1_to_10)}')

  print('----------------------------------------------------')

  # List of odd numbers from 1 to 100
  list_odd = [i for i in range(1, 100, 2)]

  print('Odd numbers from 1 to 100')

  print(f'Max Value: {maximum_value(list_odd)}')
  print(f'Min Value: {minimum_value(list_odd)}')
  print(f'Sum of List: {list_sum(list_odd)}')
  print(f'Average of List: {list_average(list_odd)}')
  print(f'Median of List: {list_median(list_odd)}')

  print('----------------------------------------------------')

  # List of squares from 1 to 100
  list_squares = [i**2 for i in range(1, 101)]

  print('Squares of numbers from 1 to 100')

  print(f'Max Value: {maximum_value(list_squares)}')
  print(f'Min Value: {minimum_value(list_squares)}')
  print(f'Sum of List: {list_sum(list_squares)}')
  print(f'Average of List: {list_average(list_squares)}')
  print(f'Median of List: {list_median(list_squares)}')

  print('----------------------------------------------------')

  # list of random integers between 1 and 1000
  list_rand_1_1000= [random.randint(1, 1000) for i in range(1, 101)]

  print('100 random numbers in the range 1 to 1000')

  print(f'Max Value: {maximum_value(list_rand_1_1000)}')
  print(f'Min Value: {minimum_value(list_rand_1_1000)}')
  print(f'Sum of List: {list_sum(list_rand_1_1000)}')
  print(f'Average of List: {list_average(list_rand_1_1000)}')
  print(f'Median of List: {list_median(list_rand_1_1000)}')

  print('----------------------------------------------------')