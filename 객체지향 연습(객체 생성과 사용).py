class Box:
    def __init__(self, width=0, length=0, height=0):
        self.__width = width
        self.__length = length
        self.__height = height
    def setWidth(self, width):
        self.__width = width;
    def setLength(self, length):
        self.__length = length;
    def setHeight(self, height):
        self.__height = height;
    def getVolume(self):
        return self.__width*self.__length*self.__height
    def __str__(self):
        return '(%d, %d, %d)' % (self.__width, self.__length, self.__height)

box = Box(100, 100, 100)

print(box)
print('상자의 부피는 ', box.getVolume())
