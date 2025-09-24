#reverse order
str1=input("Enter a string:")
print('The',str1,"in reverse orderis:")
length=len(str1)
for a in range(-1,-length-1,-1):
    print(str1[a])

#reverse order and normal
str1=input("Enter a string:")
length=len(str1)
i=0
for a in range(-1,-length-1,-1):
    print(str1[i],"\t",str1[a])
    i+=1
    
#contain 0 or not
n=int(input("Enter a number:"))
s=str(n)
if '0' in s:
    print("There is a 0 in",n)
else:
    print("There is no 0 in",n)
    
#username and passcode
uname=input("Enter your username:")
code=input("Enter your passcode:")
if uname in code:
    print("NOt valid")
else:
    print("Thank you")
#pattern without loop
str1='#'
pattern=''
for a in range(5):
    pattern+=str1
    print(pattern)
#
string = input("Enter a string:")
a=0
length = len(string)
end = length
string2=" "      #empty string
while a < length:
    if a==0:
        string2 += string[0].upper()
        a+= 1
    elif (string[a] ==" and string[a+1] !="):
          string2 += string[a]
          string2 += string[a+1].upper()
          a += 2
    else:
        string2 += string[a]
        a += 1
        print ("Original String:", string)
        print ("Capitalized words String", string2)
#
string = input("Enter a string:")
length = len(string)
mid = length/2
rev=-1
for a in range(mid):
    if string[a] == string[rev]:
        a += 1
        rev -= 1
    else:
        print (string, "is not a palindrome")
        break
else: print (string, "is a palindrome")
#
string= input("Enter a string:")
length=len(string)
maxlength=0
maxsub=' '
sub=' '
lensub=0
for a in range(length):
    if string[a] in 'aeiou' or string[a] in "AEIOU":
        if lensub > maxlength:
            maxsub=sub
            maxlength =lensub
            Sub=' '
            lensub=0
        else:
            sub += string[a]
            lensub= len(sub)
            a+=1


print ("Maximum length consonant substring is:", maxsub,end=' ')
print ("with", maxlength, "characters")
#
string=input("Enter a string")
length=len(string)
print ("Original string :", string)
string2=" "
for a in range(9, length, 2):
    string2 += string[a]
    if a< (length-1):
        string2 += string[a+1].upper()
print ("Alternatively capitalized string:", string2)
