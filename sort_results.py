import numpy as np

def sort_values(values: np.ndarray, ascending=True):
    return np.sort(values) if ascending else np.sort(values) [::-1]
