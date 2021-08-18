print('hello world')

import matplotlib.pyplot as plt 

x = list(range(5))
y = [3*i for i in range(5)]

plt.plot(x, y)
plt.show()