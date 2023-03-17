# class point:
#     '''构造函数，构造函数是一个在创建时被调用的函数'''
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")



'''point1调用类point'''
# point1 =point()
# '''调用point中的函数'''
# '''设置point中的x为10'''
# point1.x=10
# point1.y=20
# print(point1.x)
# point1.draw()
'''构建了一个名为pointa的对象，对象中的x，y赋值为10，20'''
# pointa=point(10,20)
# pointa.x=11
# print(pointa.x)


class Person:
    '''使用person类定义对象时自动定义name属性'''
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")
'''建立名为john的对象，使用person'''
john = Person('johnsmith')
print(john.name)
'''调用john对象中的talk函数'''
john.talk()