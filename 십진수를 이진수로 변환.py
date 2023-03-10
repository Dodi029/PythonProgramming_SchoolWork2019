decimal = int(input("원하는 숫자를 입력하세요"))
result = ''
while (decimal>0):
    remainder = decimal %2
    decimal = decimal //2
    result = str(remainder)+result
print(result)
