import itertools
import numpy
from pandas.core.common import flatten
from iteration_utilities import deepflatten
from HomeTask_Decorators_200622 import file_path_maker

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
@file_path_maker('\log')
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

class MyFlattenIterator:
    def __init__(self, _list):
        self._list = _list

    def __iter__(self):
        self.marker = -1
        self.nested_list = []
        self.list_iter = iter(self._list)
        return self

    def __next__(self):
        self.marker += 1
        if len(self.nested_list) == self.marker:
            self.nested_list = []
            self.marker = 0
            while not self.nested_list:
                self.nested_list = next(self.list_iter)
        return self.nested_list[self.marker]

class MyGenerator:
    def __init__(self, _list):
        self._list = _list

    def flat_generator(self, _list):
        for item_list in _list:
            for sub_itemlist in item_list:
                yield sub_itemlist


if __name__ == '__main__':
    iterutil_flatten()

    # print('Iterator:')
    # for list_item in MyFlattenIterator(nested_list_1):
    #     print(list_item)
    #
    # print('Generator:')
    # for list_item in MyGenerator.flat_generator(MyGenerator, nested_list_1):
    #     print(list_item)
    #
    # print('List comprehensions:')
    # print([list_item for list_item in MyFlattenIterator(nested_list_1)])
    #
    # print('Iterator with deep flatten:')
    # iterutil_flatten()