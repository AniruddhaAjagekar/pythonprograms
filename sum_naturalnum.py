print("Enter the Value of n: ", end="")
n = int(input())
if n<0:
    print("\nInvalid Input!")
else:
    sum = 0
    for i in range(1, n+1):
        sum = sum+i
    print("\nSum of ",n," natural numbers is: ", sum)
