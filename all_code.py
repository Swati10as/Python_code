def fibonacci():
    # Program to display the Fibonacci sequence up to n-th term

    n_number = int(input("How many terms? "))

    n1, n2 = 0, 1
    count = 0

    if n_number <= 0:
        print("Please enter a positive integer")
    elif n_number == 1:
        print(n1)
    else:
        while count < n_number:
                print(n1)
                n = n1 + n2
                # update values
                n1 = n2
                n2 = n
                count += 1
def factorial():
    num = int(input("Enter a number: "))

    fact = 1

    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("1")
    else:
        for i in range(1,num + 1):
            fact = fact*i
        print("The factorial of",num,"is",fact)


    