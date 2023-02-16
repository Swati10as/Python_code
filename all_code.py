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

def third():
    #Write a function that gets the time as three integer arguments (for hours, minutes, and seconds) 
    #and returns the number of seconds since the last time the clock “reached 12.” 
    #Use this function to calculate the amount of time in seconds between two hours, when both are within a 12-hour cycle.    
    
    
    def calcSecondsFromTvelwe( hh, mm, ss):
	    return (hh % 12 * 3600 + mm * 60 + ss)   # take hh modulo 12 to maintain 24h mode

    def gydfvgiouygfg():

    	hours = int(input("Enter a number: "))
        minutes = int(input("Enter a number: "))
        seconds = int(input("Enter a number: "))
	    time1 = calcSecondsFromTvelwe(hours, minutes, seconds)
	    print("Enter second time (hours, minutes and seconds): ",hours,minutes,seconds)
	    time2 = calcSecondsFromTvelwe(hours, minutes, seconds)
	    print("Amount of time in seconds between two times is: ",abs(time1 - time2))
