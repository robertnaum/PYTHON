def rotate(lst, n):
    return lst[-n:] + lst[:-n]

lst = [1, 2, 3, 4, 5]
roated_lst = rotate(lst, 2)
print(roated_lst)  # [4, 5, 1, 2, 3]