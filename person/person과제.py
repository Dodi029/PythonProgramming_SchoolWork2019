import person as p
if __name__=="__main__":
    peoples=[]
    names=["을지문덕", "계백", "김유신", "강감찬", "이순신"]

    for i in range(5):  #질문
        name=names[i]   #이름
        age=int(input(names[i]+' 나이 ')) #나이
        weight=int(input('몸무게')) #몸무게
        height=int(input('키')) #키
        heroes=p.person(name,i,age,weight,height) #총정리
        peoples.append(heroes) #함수지정

    heroes = sorted(peoples,    key=lambda person: person.age)  #나이
    print("나이순서")

    for i in range(len(heroes)):
        print(heroes[i])

    heroes = sorted(peoples,    key=lambda person: person.height) #키
    print("키순서")

    for i in range(len(heroes)):
        print(heroes[i])

    heroes = sorted(peoples,    key=lambda person: person.weight) #몸무게
    print("몸무게순서")

    for i in range(len(heroes)):
        print(heroes[i])

