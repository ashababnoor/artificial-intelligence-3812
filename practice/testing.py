print('hello world')

import matplotlib.pyplot as plt
import numpy as np

x = list(range(5))
y = [3*i for i in range(5)]

# plt.plot(x, y)
# plt.show()

array = np.array([[2, 4, 1], [6, 13, 3], [7.89854, 8, 3]])
print(np.mean(array, axis=0))
print(np.delete(array, 0))
print(array[1:])

print('=======')

array = array[1:]
print(array)

sub = [5, 0, 9]

print(np.append(array, [sub], axis=0))

x = None
x = 5

print(None == x)

test = []
test.append(array[1][0])
print(test)

a = np.array([[5, 6], [4, 9]])
print(np.square(a[1] - a[0]))

