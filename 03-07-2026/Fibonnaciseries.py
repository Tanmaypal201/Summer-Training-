x=int(input("Enter the Number of Element Print of series:"))
i=0
j=1
print(i,end=",")
for value in range (0,x-1):
    c=i+j
    j=i
    i=c
    print(c,end=",")