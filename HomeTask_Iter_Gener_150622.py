import itertools
import numpy
from pandas.core.common import flatten
from iteration_utilities import deepflatten

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]]

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, [[None, 3], [4 , 5, [6, 7]]]],
]
# output function
def flatten_output(flatten_list):
    for item_list in flatten_list:
        print(item_list)
    print(flatten_list)

#  list comprehensions function
def listcompr_output(_list):
    return [sub_item for item in _list for sub_item in item]

# variant number 1 - deep flatten
def iterutil_flatten(nested_list=nested_list_2):
    flatten_list = list(deepflatten(nested_list))
    flatten_output(flatten_list)
    return  flatten_list

# variant number 2 - deep flatten
def flatten_pandas(nested_list=nested_list_2):
    flatten_list = list(flatten(nested_list))
    flatten_output(flatten_list)
    return flatten_list

# variant number 3 - 2d-flatten
def flatten_itertools(nested_list=nested_list_1):
    flatten_list = list(itertools.chain(*nested_list_1))
    flatten_output(flatten_list)
    print('List comprehension:', listcompr_output(nested_list))
    return flatten_list

# variant number 4 - 2d-flatten
def flatten_numpy(nested_list=nested_list_1):
    flatten_list = list(numpy.concatenate(nested_list_1).flat)
    flatten_output(flatten_list)
    print('List comprehension:', listcompr_output(nested_list))
    return flatten_list

# variant number 5 - 2d-flatten
def simple_flatten(nested_list=nested_list_1):
    flatten_list = []
    for item_list in nested_list:
        if type(item_list) == list:
            for subitem_list in item_list:
                flatten_list.append(subitem_list)
        else:
            flatten_list.append(item_list)
    flatten_output(flatten_list)
    print('List comprehension:', listcompr_output(nested_list))
    return flatten_list


if __name__ == '__main__':
    iterutil_flatten()
    # flatten_pandas()
    # flatten_itertools()
    # flatten_numpy()
    # simple_flatten()