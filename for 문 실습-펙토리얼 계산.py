x=int(input("숫자를 입력하세요"))
f=1
for i in range(x,0,-1):
    f*=i
print("입력하신 숫자의 펙토리얼은",f,"입니다")
