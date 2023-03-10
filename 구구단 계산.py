x=int(input("구구단 몇 단을 계산할까요?"))
n=1
if 1<x<10:
    print("구구단",x,"단을 계산합니다")
    for i in range (9):
        print(x,"*",n,"=",x*n)
        n+=1
else :
    print("구구단이 아닙니다")