x=input("Enter the String for Check pallindrome :")
size=len(x)
neg=-1
ispal=1
for i in range(0,size//2):
    if(x[i]!=x[neg]):
        ispal=0
    neg=neg-1
    break
if(ispal==0):
    print("Not Palindrome")
elif(ispal==1):
    print("Palindrome")
