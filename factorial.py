def factorial(n):
    fact = 1
    for i in range(n):
        fact *= (i+1) # recall range is 0 .. n-1, we need 1 to n
    return fact

for i in range(1, 11):
    print(f"{i}! = {factorial(i)}")
