
# Creating class "Protected"
class Protected:
    def __init__(self):
        # Defining private and protected variables
        self._protectedVar = 15
        self.__privateVar = 5

    # Creating a method to print the private variable
    def getPrivate(self):
        print(self.__privateVar)


# Object created to print both variables
obj = Protected()
obj.getPrivate()
print(obj._protectedVar)

