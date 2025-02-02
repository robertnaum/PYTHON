from collections import Counter

lst=[1,2,2,3,4,4,4,5]
duplicates = [item for item, count in Counter(lst).items() if count > 1]
print (duplicates)

x = [item for item, count in Counter(lst).items()]  #distinct
print(x)

y = [item for item in lst]
print(y)

print(Counter(lst))
print(Counter(lst).items())
print(Counter(lst).values())
print(Counter(lst).keys())
print(Counter(lst).most_common(2))
print(Counter[3])