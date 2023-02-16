#Write a function that displays all prime numbers between 1 and 1000

def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==0:
        return num
    else:
        return 0

def prime_list():
    res=[]
    for i in range(1,1000):
        res.append(prime(i))
    new=list(filter(lambda num: num != 0, res))
    print(new)

prime_list()

