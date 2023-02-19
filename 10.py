#Write a program that determines if a word is a palindrome.

s=input("Enter:")

y=s[::-1]

if s==y:
    print("PALINFROME")
else:
    print("NPT PALINDROME")