'''函数传入参数'''
# def greet_user(name):
#     print(f"hi {name}")
#
# print("start")
# greet_user("john")
# print("end")
'''传入多个参数'''
# def greet_user(first_name,last_name):
#     print(f"hi {first_name} {last_name}")
#     print("welcome")
# print("start")
# greet_user("john","smish")
'''关键参数,指定传入的参数为某个参数
传入参数时可以第一个为位置参数第二个为关键参数
greet_user("ri",first_name="liu")'''
# def greet_user(first_name,last_name):
#     print(f"Hi {first_name} {last_name}")
# print("start")
# greet_user(last_name="ri",first_name="liu")
'''函数返回值'''
# def square(number):
#     return number*number
# result = square(3)
# print(result)

# def emoji_converter(message):
#     words=message.split(" ")
#     emoji={
#         ":)":"😀",
#         ":(":"🙃"
#     }
#     output=""
#     for word in words:
#         output += emoji.get(word, word)+" "
#     return output
#
# message=input(">")
# result=emoji_converter(message)
# print(result)

'''错误，当输入不是你太类型时输出except'''
try:
    age= int(input("age: "))
    incom=2000
    risk=incom/age
    print(risk)
except ZeroDivisionError:
    '''除数为0'''
    print("Age cannot be 0")
except ValueError:
    '''值错误'''
    print("invalid value")
