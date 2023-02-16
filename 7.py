#Write a function that takes an integer value and 
#returns the number with its digits reversed. For example, given the number 7631, 
#the function should return 1367


num = int(input("enter number:"))
rev=0
while num>0:
    rem=num%10
    rev=rev*10 + rem
    num=num//10
print(rev)


