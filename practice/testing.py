print('hello world')

import matplotlib.pyplot as plt
import numpy as np

x = list(range(5))
y = [3*i for i in range(5)]

# plt.plot(x, y)
# plt.show()

array = np.array([[2, 4, 1], [6, 13, 3], [7, 8, 3]])
print(np.mean(array, axis=0))
print(np.delete(array, 0))
print(array[1:])

print('=======')

array = array[1:]
print(array)