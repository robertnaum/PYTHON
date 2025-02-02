lst = [10,20,10,30,10,40]
indices  = [i+2 for i, x in enumerate(lst) if x == 10]
print(indices)  #[2,4,6]
