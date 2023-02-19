#Write a function that reads a text file and determines the number of each letter of the alphabet in that text. 
#For example, “I love Python programming” has one “y”, two “m”, two “p”, etc. 
#The function should return the count of only the letters that exist in the function.

s=input("Enter text:")
s1={}
for i in range(0,len(s)):
    if s[i] in s1.keys():
        s1[s[i]]=s1[s[i]]+1
    else:
        s1[s[i]]=1
print(s1)
