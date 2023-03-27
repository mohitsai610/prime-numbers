t=1
n=int(input("enter a number:"))
for num in range(t,n+1):
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
               print(num)
