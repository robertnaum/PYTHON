num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

for num in range(start, end + 1):
    if num > 1 and all(num % i != 0 for i in range(2, num)):
        print(num)    