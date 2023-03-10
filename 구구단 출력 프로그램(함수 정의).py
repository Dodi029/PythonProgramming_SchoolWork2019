def multiplicationTable(dan):
    n=1
    i=0

    if dan>20 or dan <1:

        print("구구단이 아닙니다.")

    else:
        print("구구단",dan,"단을 계산합니다.")

        while i<20:
            i=i+1
            print(dan,"x",i,"=",dan*i)

        print("계산 완료.")

multiplicationTable(int(input("구구단 몇 단을 계산할까요?:")))
