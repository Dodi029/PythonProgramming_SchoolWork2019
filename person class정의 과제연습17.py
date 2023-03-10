class person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return "이름 %s  나이 %d  키 %d  몸무게 %d" %(self.name, self.age, self.height, self.weight)

peoples = []

names = ["을지문덕", "계백", "김유신", "강감찬", "이순신"]

for i in range(len(names)):
    name = names[i]
    print(names[i])

    age = int(input("나이를 입력하세요"))
    height = int(input("키를 입력하세요"))
    weight = int(input("몸무게를 입력하세요"))
    a = person(name, age, height, weight)

    peoples.append(a)

a = sorted(peoples, key=lambda person: person.age)
print("나이순서입니다")

for i in range(len(a)):
    print(a[i])

a = sorted(peoples, key=lambda person: person.weight)
print("키순서입니다")

for i in range(len(a)):
    print(a[i])
    
a = sorted(peoples, key=lambda person: person.weight)
print("몸무게순서입니다")

for i in range(len(a)):
    print(a[i])
