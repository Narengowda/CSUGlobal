import numpy as np
import pandas as pd

temperatures = np.array([1,2,3])
temperatures = np.append(temperatures, 25.5)
temperatures = np.append(temperatures, 28.0)
temperatures = np.append(temperatures, 26.2)

print("Max temperature = ", temperatures.max())
print("Min temperature = ", temperatures.min())
print("Average temperature = ", temperatures.mean())
print("Standard deviation temperature = ", np.std(temperatures))
print("numpy array = ", temperatures)

# Create multi dimensional arrays
arr = np.array([
    [np.array([1, 2]), np.array([3, 4])],
    [np.array([5, 6]), np.array([7, 8])]
])

print("Multi dimentional numpy array = ", arr)

# Creating a Pandas array from a list
int_array = pd.array([1, 2, 3, 4, 5])
print("Pandas arrays = ", int_array)
