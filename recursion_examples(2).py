#code to find factorial using recursion
def factorial(n):
    if(n==0):
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(5))


#code to find fibonacci sum using recursion


def fibonacci(n):
    if(n<=1):
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(9))
    
