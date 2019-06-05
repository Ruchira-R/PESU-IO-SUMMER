m=int(input("Enter an integer : "))
sum=0
if(m<0):
    print("Sum of the digits of the number cant be found")
while m:
    l=m%10
    sum=sum+l
    m=m//10
print("Sum : ",sum)