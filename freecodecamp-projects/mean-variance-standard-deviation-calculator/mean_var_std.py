import numpy as np

def calculate(list):
    arr = np.array(list).reshape(3, 3)
    mean = [[np.mean(arr[:, 0]), np.mean(arr[:, 1]), np.mean(arr[:, 2])], [np.mean(arr[0]), np.mean(arr[1]), np.mean(arr[2])], np.mean(arr)]
    var = [[np.var(arr[:, 0]), np.var(arr[:, 1]), np.var(arr[:, 2])], [np.var(arr[0]), np.var(arr[1]), np.var(arr[2])], np.var(arr)]
    std = [[np.std(arr[:, 0]), np.std(arr[:, 1]), np.std(arr[:, 2])], [np.std(arr[0]), np.std(arr[1]), np.std(arr[2])], np.std(arr)]
    max = [[np.max(arr[:, 0]), np.max(arr[:, 1]), np.max(arr[:, 2])], [np.max(arr[0]), np.max(arr[1]), np.max(arr[2])], np.max(arr)]
    min = [[np.min(arr[:, 0]), np.min(arr[:, 1]), np.min(arr[:, 2])], [np.min(arr[0]), np.min(arr[1]), np.min(arr[2])], np.min(arr)]
    sum = [[np.sum(arr[:, 0]), np.sum(arr[:, 1]), np.sum(arr[:, 2])], [np.sum(arr[0]), np.sum(arr[1]), np.sum(arr[2])], np.sum(arr)]
    calculations = {
      'mean': mean,
      'variance': var,
      'standard deviation': std,
      'max': max,
      'min': min,
      'sum': sum
    }
    return calculations
