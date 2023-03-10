import random
class dice:
    def __init__(self,random):
        self.random=random
    def roll(self):
        return self.random
a=random.randint(1,6)
b=dice(a)
print('주사위를 굴려 나온 눈은', str(b.roll()),'입니다')