from data_loader import load_data
from dataset import DataSet
from normalizer import normalize
from sort_results import sort_values
import numpy as np

values = load_data("data.txt")

normalized_values = normalize(values)
data = DataSet(normalized_values)

sorted_asc = sort_values(normalized_values, ascending=True)
sorted_desc = sort_values(normalized_values, ascending=False)

print("Normalized: ", normalized_values)
print("Mean: ", data.mean())
print("Min: ", data.minimum())
print("Max: ", data.maximum())
print("sorted_asc: ", sorted_asc)
print("sorted_desc: ", sorted_desc)