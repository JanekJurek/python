import numpy as np
x1 = np.random.random([8,8])
x2 = np.random.random([8,8])


y = np.zeros([x1.shape[0],x2.shape[1]])

for i in range(x1.shape[0]):
    for j in range(x2.shape[1]):
        for k in range(x2.shape[0]):
            y[i][j] += x1[i][k] + x2[k][j]

print(y)
