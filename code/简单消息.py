# 2-1 简单消息： 将一条消息存储到变量中，再将其打印出来。
msg = "我是一条消息"
print(msg)


# 2-2 多条简单消息： 将一条消息存储到变量中，将其打印出来；再将变量的值修改为一条新消息，并将其打印出来。
msg = "我是一条新的消息"
print(msg)

# 2-3 个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，
# 如 “Hello Eric, would you like to learn some Python today?” 。
name = "三木先生"
print("Hello " + name + "，" + " 学习Python好玩吗？")

# 2-4 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name = "dengsenzhong"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
name = "三木先生"
ana = '"老实人，最后的结局也是悲惨的。"'
print(name + "说过，" + ana)

# 2-6 名言 2 ： 重复练习 2-5 ，但将名人的姓名存储在变量 famous_person 中，再创建要显示的消息，并将其存储在变量 message 中，
# 然后打印这条消息。
famous_person = "三木先生"
message = "说：诗和远方，那是他向往的地方。"
print(famous_person + message)

# 2-7 剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合 "\t" 和 "\n" 各一次。
# 打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数 lstrip() 、 rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
name = "   三木先生\t\n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())
