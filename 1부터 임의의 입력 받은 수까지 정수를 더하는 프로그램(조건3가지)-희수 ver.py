x = int(input("정수를 입력하세요. \n>>"))

i = 1
s = 0

while x > 0 :

    sv=i*17
    i = i+1

    if abs(x - sv) < 8.5 :
        break

for x in range(1, sv+1):
    if x % 3 == 0: continue
    s+=x
    

print("입력하신 수에 가장 가까운 17의 배수는",sv,"입니다.")
print("또한 1에서",sv,"까지의 정수 중 3의 배수를 제외한 정수의 합은",s,"입니다.")
