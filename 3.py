
#Write a function that gets the time as three integer arguments (for hours, minutes, and seconds) 
#and returns the number of seconds since the last time the clock “reached 12.” 
#Use this function to calculate the amount of time in seconds between two hours, when both are within a 12-hour cycle.    
    
    
def calcSecondsFrom12( hh, mm, ss):
	    return (hh % 12 * 3600 + mm * 60 + ss)   # take hh modulo 12 to maintain 24h mode

def final():
    hours, minutes, seconds = input("Enter three values:hours,minutes,seconds ").split()
    time1 = calcSecondsFrom12(int(hours), int(minutes), int(seconds))
    hours, minutes, seconds = input("Enter three values:hours,minutes,seconds ").split()
    time2 = calcSecondsFrom12(int(hours), int(minutes), int(seconds))
    print("Amount of time in seconds between two times is: ",abs(time1 - time2))

final()

