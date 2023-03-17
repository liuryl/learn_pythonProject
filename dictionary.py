# customer={
#     "name":"john smith",
#     "age":30,
#     "is_verified":True
# }
# 实用get访问字典中某一个项目时若字典中没有返回none，字典中没有bir时可以为bir设置默认值
# print(customer.get("bir","jan 1 1988"))
'''重新赋值'''
# customer["name"]="jack"
# print(customer["name"])
'''添加新的内容'''
# customer["birthday"]="jan 1 1899"
# print(customer["birthday"])
# print(customer)

# phone=input("phone: ")
# digits_map={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# for ch in phone:
#     output+=digits_map.get(ch,"!")
# print(output)

# message = input(">")
'''根据空格进行分离'''
# words=message.split(' ')
# emojis={
#     ":)":"😀",
#     ":(":"🙃"
# }
# output=""
# for word in words:
#     output+=emojis.get(word,word)+" "
# print(output)