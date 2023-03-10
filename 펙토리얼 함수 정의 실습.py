#Prog: factorial

def factorial(x):

    f=1
    i=0

    while i <x:
        i=i+1
        f*=i

    return f

print(factorial(int(input("임의의 숫자를 입력하시오."))))
