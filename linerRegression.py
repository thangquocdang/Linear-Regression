import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data set
A = [2,5,7,9,11,16,19,23,22,29,29,35,37,40,46]
b = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

plt.plot(A,b, 'ro') 
# Convert row vector to column vector
A = np.array([A]).T
b = np.array([b]).T
 
# Create ones vector
ones = np.ones((A.shape[0],1),dtype=np.uint8)

# Concatenate ones to A
A = np.concatenate((A,ones), axis =1 )

# Apply linear regression formula
x = np.linalg.inv(A.transpose().dot(A)).dot(A.transpose()).dot(b)

# Visualize result
x0 = np.array([1,50]).T
y0 = x[0][0]*x0+ x[1][0]
plt.plot(x0,y0)


plt.show()