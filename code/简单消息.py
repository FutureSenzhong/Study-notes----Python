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


# 2-8 数字 8 ： 编写 4 个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字 8 。为使用 print 语句来显示结果，
# 务必将这些表达式用括号括起来，也
# 就是说，你应该编写 4 行类似于下面的代码：
# print(5 + 3)
# 输出应为 4 行，其中每行都只包含数字 8 。
print(4+4)
print(10-2)
print(2*4)
print(8/1)
# 2-9 最喜欢的数字： 将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。
m = 404
msg = "我最喜欢的数字是：" + str(m)
print(msg)
# Python 之禅： 在 Python 终端会话中执行命令 import this ，并粗略地浏览一下其他的指导原则。
# 简单就是最好的
# 行之有效就是最完美的
# 列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 下标访问列表
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
# 负数索引表示反向取数据，-1表示最后一个元素，-2表示倒数第二个元素，以此类推。。。
message = "我的第一辆自行车是 " + bicycles[0].title() + "."
print(message)

# 3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为 names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ["王欣", "蒲佳", "李敏"]
print(names[0])
print(names[1])
print(names[2])
print(names[-1])
print(names[-2])
print(names[-3])
# 3-2 问候语： 继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
print(names[0] + '是一个男朋友')
print(names[1] + '也是一个男朋友')
print(names[2] + '是一个女朋友')
# 3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言，如 “I would like to own a Honda motorcycle”
types = ['走路', '骑自行车', '坐公交车', '打车', '自驾探险者']
print('我更喜欢' + types[-1] + '去上班。')
# 通过下表修改列表的元素，你可以修改任何列表元素的值，而不仅仅是第一个元素的值。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# 在列表中添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
# 在列表中通过下表插入元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# 通过下标删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
# 使用pop方法删除元素，并返回该元素可以试用变量保存起来
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 如果你不确定该使用 del 语句还是 pop() 方法，
# 下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；
# 如果你要在删除元素后还能继续使用它，就使用方法 pop() 。
# 使用remove删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'ducati', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# 注意方法 remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。
# 3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少 3 个你想邀请的人；然后，使用
# 这个列表打印消息，邀请这些人来与你共进晚餐。
# 3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 以完成练习 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。
# 3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
# 使用 insert() 将一位新嘉宾添加到名单开头。
# 使用 insert() 将另一位新嘉宾添加到名单中间。
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
# 3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习 3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
# 晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
# 3.3 　组织列表
# 在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。这虽然在大多数情况下都是不
# 使用方法 sort() 对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
n_cars = cars.sort()
print(cars)
print(n_cars)
# 反向排序
cars.sort(reverse=True)
print(cars)
# 使用函数 sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
n_cars = sorted(cars)
print(cars)
print(n_cars)
# 反转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
n_cars = reversed(cars)
print(next(n_cars))
print(next(n_cars))
print(next(n_cars))
print(next(n_cars))
print(cars)
cars.reverse()
print(cars)
# for遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#  range() 让你能够轻松地生成一系列的数字，取值范围是避开区间取值
for value in range(1, 5):
    print(value)
    # 1
    # 2
    # 3
    # 4

l = [i ** 2 for i in range(1, 11)]
print(l)

# 你首先应该考虑的是，编写清晰易懂且能完成所需功能的代码；等到审核代码时，再考虑采用更高效的方法

# for i in range(1, 1000001):
#     print(i)

l = (i for i in range(1, 80000001))
print(type(l))
# print(l)
# l = list(l)
# print(max(l))
# print(min(l))
# print(sum(l))
# 使用切片来操作列表的一部分, 切片会创建一个新的列表, 对于嵌套列表只会拷贝子列表的内存地址(浅拷贝)
players = ['charles', 'martina', 'michael', 'florence', 'eli', [1, 3, "ss"]]
print(id(players[-1]))
n = players[:]
print(players, id(players))
# n.append("三木先生")
n[-1].append("三木先生")
print(players, id(players))
print(n, id(n))
print(id(n[-1]))

# if
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
# 如果你只想执行一个代码块，就使用 if-elif-else 结构；如果要运行多个代码块，就使用一系列独立的 if 语句。

# 关于字典的最近遇到的一个面试题，字典的key有什么要求
# 回答是不可变的都可以
# 这种回答还是太浅显了，在Python中一切皆是对象，对于对象内部，只要实现了__hash__()方法的对象，都认为是不可变的，
# 所以实现了__hash_()方法的对象，都可以作为字典的key，常数，元组，字符串等其内部的实现也是基于了__hash__()方法
# 但是要注意的是类似于元组嵌套一个列表的数据结构，因为列表的可变性，当包含在元组的内部时，元组的hash值就可以改变，故而不能成为字典的key
# 解释器在运行时就会报错TypeError: unhashable type: 'list'
d = {"a": 1, "b": 2, 3: "c", (1, 2): "d"}
print(d)
# d1 = {"a": 1, "b": 2, 3: "c", (1, 2, [1, 2, "sds"]): "d"}
# print(d1)


# 字典的基本操作
# 一个简单的字典
people = {
    'name': '三木先生',
    'age': 27,
    'pro': '程序员',
}

# 通过键取值
print(people['name'])
print(people['age'])
print(people['pro'])

# 三木先生
# 27
# 程序员

# 字典是一种动态结构，可随时在其中添加键 — 值对。要添加键 — 值对，可依次指定字典名、用方括号括起的键和相关联的值。
people['money'] = 100000000

print(people)
# {'name': '三木先生', 'age': 27, 'pro': '程序员', 'money': 100000000}

# 修改字典的值
people['money'] = 0
print('三木先生赌输了，现在一无所有，存款为：' + str(people['money']))
# 三木先生赌输了，现在一无所有，存款为：0

# 对于字典中不再需要的信息，可使用 del 语句将相应的键 — 值对彻底删除。使用 del 语句时，必须指定字典名和要删除的键。
del people['money']
print(people)
# {'name': '三木先生', 'age': 27, 'pro': '程序员'}

# 一个 Python 字典可能只包含几个键 — 值对，也可能包含数百万个键 — 值对。
# 鉴于字典可能包含大量的数据， Python 支持对字典遍历。
# 字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有键 — 值对、键或值。

for k, v in people.items():
    print(str(k) + ':' + str(v))

# name:三木先生
# age:27
# pro:程序员

for k in people.keys():
    print(str(k))

# name
# age
# pro
