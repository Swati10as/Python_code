#Write a function that returns the smallest of three numbers.
 
a, b, c = input("Enter three number: ").split()
x,y,z=int(a),int(b),int(c)
if x>y & x>z:
    print(x)
elif y>x & y>z:
    print(y)
else:
    print(z)


