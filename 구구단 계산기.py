x = int(input("구구단 몇 단이 궁금하닝? \n>>"))

n = 1
i = 0

if x > 9:
    
    print("그건 구구단이 아니자낭!")

else:

    print("구구단",x,"단을 계산하장")

    while i < 9:
        i = i+1
        print(x,"×",i,"=",x*i)
        
    print("계산 끗!")
