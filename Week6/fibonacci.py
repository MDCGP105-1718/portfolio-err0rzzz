## fibonacci ##

def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print (fib(9))
#for n in range (20):
#    print (fib(n))
