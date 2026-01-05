import numpy as np

def normalize(values: np.ndarray):
    if values.size == 0:
        return values
    
    min_val = np.min(values)
    max_val = np.max(values)

    if min_val == max_val:
        return np.zeros_like(values)
    return (values - min_val) / (max_val - min_val)