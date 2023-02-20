#Write a function that indicates the number of one-letter words, two-letter words, three-letter words, etc. 
# For example, “I love Python programming” has zero one-letter words, two two-letter words, 
# one three-letter word, zero four- and five-letter words, one six-letter word, and one word with more than six letters.
from num2words import num2words
s=input("Enter sentence:  ").split(' ')
d={1:0,2:0,3:0,4:0,5:0,6:0,7:0}
for i in s:
    if len(i) in d and len(i)<7:

        d[len(i)]=d[len(i)]+1
    if len(i)>6:
        d[7]=d[7]+1
for i in d.keys():
    if i!=7:
        print(num2words(d[i])," ",num2words(i),"letter word ,",end="")
    else:
        print(num2words(d[i])," word with more than six letter word")
    