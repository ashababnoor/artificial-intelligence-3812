# -*- coding: utf-8 -*-
"""KNN_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CqAhILc0iSH1elif35uCKYLv_wZbBJDQ
"""

from numpy import genfromtxt
data_path = 'knn/datasets/diabetes.csv'
my_data = genfromtxt(data_path, delimiter=',')

# print(my_data.shape)
# print(type(my_data))

my_list = my_data.tolist()

import random

shuffled_list = my_list.copy()
random.shuffle(shuffled_list)

train_set = []
val_set = []
test_set = []

# Splitting dataset into train, validation and test set

# checking if list is shuffled or not
# for i in range(5):
#   print(shuffled_list[i])
#   print(my_list[i])
#   print('-' * 30)

for s in shuffled_list:
  num = random.random()
  if num >= 0 and num <= 0.7:
    train_set.append(s)
  elif num > 0.7 and num <= 0.85:
    val_set.append(s)
  else:
    test_set.append(s)

print('train set length:', len(train_set))
print('val set length:', len(val_set))
print('test set length:', len(test_set))

#Implementing KNN Regression algorithm

import numpy as np

def get_average(arr):
  output_list = []
  for element in arr:
    output_list.append(element[0][-1])
    # only taking the regression value/output
  
  # print('output list:', output_list)
  return sum(output_list) / len(output_list)

K = 20

# running algorithm on validation set

error = 0

for V in val_set:
  L = [] # list for storing distance
  v_point = np.array(V[:-1])
  # print('V as point:', v_point, 'V: ', V)
  
  for T in train_set:
    t_point = np.array(T[:-1])
    # print('T as point:', t_point)
    distance = (np.sum(np.square(v_point - t_point)))**0.5
    L.append([T, distance])

  L = sorted(L, key = lambda x:x[1])
  first_K = L[:K]
  # first_K = np.array(first_K)
  # print(first_K)
  # print('-' * 30)
  predicted_output = get_average(first_K)
  # print('predicted output: ', predicted_output, 'actual output:', V[-1])
  error += ((V[-1] - predicted_output)**2)

print()
mean_squared_error = (error) / len(val_set)
print('Error on validation set: ', str(round(mean_squared_error, 3)))

# running algorithm on test set

error = 0

for V in test_set:
  L = [] # list for storing distance
  v_point = np.array(V[:-1])
  # print('V as point:', v_point, 'V: ', V)
  
  for T in train_set:
    t_point = np.array(T[:-1])
    # print('T as point:', t_point)
    distance = (np.sum(np.square(v_point - t_point)))**0.5
    L.append([T, distance])

  L = sorted(L, key = lambda x:x[1])
  first_K = L[:K]
  # first_K = np.array(first_K)
  # print(first_K)
  # print('-' * 30)
  predicted_output = get_average(first_K)
  # print('predicted output: ', predicted_output, 'actual output:', V[-1])
  error += ((V[-1] - predicted_output)**2)

print()
mean_squared_error = (error) / len(test_set)
print('Error on test set: ', str(round(mean_squared_error, 3)))