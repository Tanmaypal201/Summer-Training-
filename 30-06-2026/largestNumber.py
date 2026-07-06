a = [20,21,70,80,64,36]
a.sort()
print("Maximum Number is",a[-1])
sum=0
for i in a:
    sum+=i 
print("Sum of these number is : ",sum)
print("Average of these number is : ",sum/(len(a)))