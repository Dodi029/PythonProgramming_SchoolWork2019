appleQuality=input("사과의 상태를 입력하시오.")
applePrice=int(input("사과 1개의 가격을 입력하시오."))
if appleQuality=="신선":
               if applePrice<1000:
                   print("10개를 산다.")
               else:
                   print("5개를 산다.")
else:
        print("사과를 사지 않는다.")
