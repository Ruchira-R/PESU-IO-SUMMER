c=input("Enter a list of numbers seperated by commas : ").split(",")
l = list(map(int,c))
m=int(input("Enter the element to be searched : "))
low=0
z=0
high=len(l)-1
while(low<=high):
    mid=int((low+high)/2)
    if(l[mid]==m):
        print("Element ", m, " is present at (index) : ", mid)
        z=1
        break
    elif(l[mid]<m):
        low=mid+1
    elif(l[mid]>m):
        high=mid-1
if(z==0):
    print("Element is not present in the list")

