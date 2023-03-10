def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(int(input("팩토리얼 할 숫자를 입력 하시오:"))))
