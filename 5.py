#Write a function that determines if a number is prime.

num = int(input("Enter the number:"))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
if flag==0:
    print("prime")
else:
    print("not prime")