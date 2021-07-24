

class Protected:
    def __init__(self):
        self._protectedVar = 15
        self.__privateVar = 5
        
    def getPrivate(self):
        print(self.__privateVar)


obj = Protected()
obj.getPrivate()
print(obj._protectedVar)

