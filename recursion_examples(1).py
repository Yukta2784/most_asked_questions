''' this file contains 2 programs'''
#code to find sum of natural numbers using recursion
def sum(n):
    if(n==0):
        return 0;
    else:
        return(n+sum(n-1))
p=sum(5)
print(p)
#code to find a^b using recursion
def pow(a,b):
    if(b==0):
        return 1;
    else:
        return(a*pow(a,b-1))
p=pow(3,4)
print(p)
