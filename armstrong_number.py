def armstrong(number):
    num_str = str(number)
    return number == sum([int(i) ** len(num_str) for i in num_str])

num = int(input("Enter a number: "))

if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")