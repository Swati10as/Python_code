#Write a function that returns the greatest common factor or least common multiple of two numbers. 
#The user can choose whether he wants the greatest common divisor, the least common multiple, or both.

def gcf(a,b):
    m=min(a,b)
    for i in range(1,m+1):
        if a%i==0 and b%i==0:
            res=i
    print (res)

def lcm(a,b):
    m=max(a,b)
    
    for i in range(m,a*b+1,m):

        if i%a == 0 and i%b ==0:
            r=i
            break
    print(r)

if __name__=="__main__":
    f=int(input("For gcf enter 1 or for lcm enter 2 or for both enter 3:"))
    if f==1:
        gcf(4,8)
    elif f==2:
        lcm(4,8)
    else:
        gcf(4,8)
        lcm(4,8)
