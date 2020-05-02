

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
n= int(input("Enter the factorial number for :"))
result=fact(n)

print("Factorial is :", result)