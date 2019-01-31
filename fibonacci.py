Numero=int(input())

for i in range(Numero):  
     if i == 0:
             a=[1]
             print(a[i])
         
     elif i == 1:
         a=[1,1]
         print(a[i])
         
     else:
         b=a[i-1]+a[i-2]
         a=a+[b]
         print(a[i]) 
