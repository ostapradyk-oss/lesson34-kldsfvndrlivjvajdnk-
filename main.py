class Student:
    def __init__(self,name,age,height, number):
        self.height=height
        self.name=name
        self.age=age
        self.number=number

    def grow(self, height=1):
        self.height+=height


anton=Student('Anton', 14,171,871231243783246894321)
print('Name - '+ anton.name)
print('Age - ', anton.age)
print('Name - '+anton.name)
print('Height - ', anton.height)
print('Number - ', anton.number)

anton.grow(height=1)
print(anton.height)




