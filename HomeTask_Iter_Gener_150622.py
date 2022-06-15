import itertools
import numpy
from pandas.core.common import flatten

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]]

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, [[None, 3], [4 , 5, [6, 7]]]],
]

def flatten_pandas():
    flatten_list = list(flatten(nested_list_2))
    print(flatten_list)
    return flatten_list

def flatten_itertools():
    flatten_list = list(itertools.chain(*nested_list_1))
    for item_list in flatten_list:
        print(item_list)
    print(flatten_list)
    print([sub_item for item in nested_list_1 for sub_item in item])
    return flatten_list

def flatten_numpy():
    flatten_list = list(numpy.concatenate(nested_list_1).flat)
    print(flatten_list)
    return flatten_list



if __name__ == '__main__':
    flatten_pandas()
    # flatten_itertools()
    # flatten_numpy()
