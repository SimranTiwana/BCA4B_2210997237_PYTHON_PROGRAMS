# Write a program to display the Fibonacci sequences up to nth term where n is provided by the user.


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter the value of n: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence up to", n, "terms:")
    for i in range(n):
        print(fib(i))


