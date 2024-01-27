num = int(input('which number factorial do you want..? '))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial)
