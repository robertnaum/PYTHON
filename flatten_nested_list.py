from collections.abc import Iterable

def flatten(lst):
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item

def show(lst):
    for item in lst:
        print(item)

nested_list = [1, [2,3, [4,5]],6]
flat_list = list(flatten(nested_list))
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

show(nested_list)