class person:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id

class student(person):

    def __init__(self,name,id,classes,gpa):
        super().__init__(name,id)
        self.classes=classes
        self.gpa=gpa
        return 

    def avg(self):
        if self.gpa<self.classes['python']:
            print(self.name)

# 등록
import pickle

f=open("학생들의 데이터","wb")
p=0
y=[]           

kor=[]
math=[]
python=[]

names=["갑","을","병","정","무"]

for i in range(len(names)):

    name=names[i]
    print(names[i])

    kor.append(int(input("국어")))
    math.append(int(input('수학')))
    python.append(int(input('파이썬')))

    if len(python)==5:
        p=int(sum(python)/len(python))


for i in range(len(names)):

    d={'이름':names[i],'kor':kor[i],'math':math[i],'python':python[i],"gap":p}
    y.append(d)

pickle.dump(y,f)
f.close()


#출력
import pickle

f=open("학생들의 데이터","rb")
o=pickle.load(f)

f.close()
print("파이썬 점수가 평균 이상인 학생은")

for i in range(len(o)):

    p=o.pop(0)
    a=student(p['이름'],None,p,p['gap'])
    a.avg()
    
