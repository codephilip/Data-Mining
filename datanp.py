import numpy as np

arr = np.loadtxt("./data/heart.csv", delimiter=",")
print(arr[:])
arr_del = np.delete(arr, 0, 1)
print("deleted\n")
print(arr_del[:])