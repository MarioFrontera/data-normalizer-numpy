import numpy as np

class DataSet():
    def __init__(self, values: np.ndarray):
        self.values = values

    def mean(self):
        return np.mean(self.values) if self.values.size > 0 else None
    
    def minimum(self):
        return np.min(self.values) if self.values.size > 0 else None
    
    def maximum(self):
        return np.max(self.values if self.values.size > 0 else None)
    
    