fist='john'
last='smith'
message=f'{fist}[{last}] is a coder'
print(message)
# print(len(message))长度
# print(message.upper())大写
# print(message.lower())
# print(message.find('o'))查找
# print(message.replace('mi','liu'))替换某个字符
# print('john'in message)判断某些字符是否存在于字符串中

# print(10//3)取整
# print(10**3)立方
# x=2.9
# print(round(x))向上取整
# print(abs(-x))变为正数

import math
# 数学公式
# print(math.ceil(2.9))向上取整
# print(math.floor(2.9向下取整))


# if  else
# is_hot=False
# if is_hot:
#     print("it is a hot day")
# else:
#     print("enjoy you day")

# price=1000000
# has_good_credit=True
# if has_good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f"down payment:${down_payment}")
# has_high_income=True
# has_high_credit=False
# has_criminal_record=True
# if has_high_income or has_high_credit:或
# if has_high_income and has_high_credit:与
# if has_high_income and not has_criminal_record:与非

    # print("Eligible for loan")
#
# temperature=30
# if temperature==30:
#     print("is a hot day")
# else:
#     print("is not a hot day")

# weight=input("weight:")
# unit=input('(L)bs or (Kg)').upper()
# if unit=="L":
#     weight=int(weight)*0.45
# elif unit=="K":
#     weight=int (weight)/0.45
# print(f"you are {weight}")


# 循环
# secret_number=9
# guess_count=0
# guess_limit=3
# i=0
# while guess_count<guess_limit:
#     guess=int(input('guess'))
#     guess_count+=1
#     if guess==secret_number:
#         print("you win")
#         break
# else:
#     print("sorry you failed")
# command=""
# while True:
#     command=input(">").lower()
#     if command=="start":
#         print("car started...")
#     elif command=="stop":
#         print("car stopped.")
#     elif command=="quit":
#         break
#     elif command=="help":
#         print("""s-go
#                 st-end
#                 h=help""")
#     else:print("i can`t understand")

# command=""
# started=False
# while True:
#     command=input(">").lower()
#     if command=="start":
#         if started:
#             print("the car is go")
#         else:
#             started=True
#             print("the car is started")
#     elif command=="stop":
#         if not started:
#             print("car is already")
#         else:
#             started=False
#             print("the car is stopped")

# for循环
# for item in range(2,10,3):
    # range(起始，结尾，步长）
    # print(item)
# prices=[10,20,30]
# for price in prices:
#     num_price=price+price
# print(f"total:{num_price}")


# 嵌套循环
# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")
# number=[5,2,5,2,2]
# for num in number:
#     output=''
#     for i in range(num):
#         output += 'x'
#     print(output)

# list列表
# name=['john','bob','mosh','sarah']
# print(name[1:3])一到三之间的元素
# number=[3,6,2,8,4,10]
# max = number[0]
# for i in number:
#     if i >max:
#         max=i
# print(max)
# # 2维列表
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# matrix[0][1]=20
# print(matrix[0][2])
# print(matrix)

# for raw in matrix:
#     for item in raw:
#         print(item)
