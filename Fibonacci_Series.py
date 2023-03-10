"""write a python program to print fibonacci series"""
num=10
n1=1
n2=3
print(n1,n2,end=" ")
for i in range(2,num):
         nth=n1+n2
         n1 = n2
         n2 = nth
         print(nth, end=" ")






