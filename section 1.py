print("welcome to python")
print("i love python")
print("i love php")
name = "mariam"
name = "mariam"
X = """"
mariam
mostafa
mosaad
3M
"""
print(name)

x = "hello world"
print(x.index("w"))
print(x.index("rld"))

name = "mariam mostafa"
print(name.upper())
name = "mariam mostafa"
print(name.lower())
# اول حرف ف االجمله كبير فقط
name = "mariam mostafa"
print(name.capitalize())
# اول حرف فى كل كلمه فى الجمله كبير
name = "mariam mostafa"
print(name.title())
# isupper / is lower
# بترجع ب true أو false حسب حاله الحروف
name = "mariam mostafa"
print(name.islower())

# concatenation (+)
name = "ail "
print("welcome," + name + "in the game")

# integer
x = 5
print(x)
x = 5 + 5
print(x)
# محاوله دمج رقم مع قيمه نصيه خطأ
# z=5+"5" type error

# str()
# print(5*5+years) type error
print(str(5 * 5) + "years")

# float
x = 4.5
print(x)

# boolean
# تحتمل قيمتين True or False
x = 10
y = 20
print(x < y)

# input function
# الحصول على بيانات من المستخدم وتخزينها فى متغير
name = input("Enter your name")
age = input("Enter yor Age")
print("your name is " + name)
print("your age is " + age)

# tuple ()
tuple = (1, 2, 3)
# tuple [0] = 5 #### type error
print(tuple)

# dictionary {}
info = {"name": "Amr", "age": 25, "country": "Mansoura"}
print(info)
print(info["name"])
print(info.get("id"))  #### None


# عباره عن داله بتحول string إلى list
programing_lan = "python php html css  javascript "
print(programing_lan.split())
programing_lan = "python_php_html_css"
print(programing_lan.split("_"))
print(programing_lan.split("h"))

# ف بايثون ببدأ عدد index من الصفر
name = "Ahmed"
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
# # لطباعه الكلمه كلها من الاول للاخر
print(name[0:])
# # لطباعه من الحرف الاول للثالث 0,1,2
print(name[0:3])
