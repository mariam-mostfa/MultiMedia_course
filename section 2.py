# IF CONDISTION:
x = 5
y = 6
if x > y:
    print("yes")
elif x == y:
    print("x==y")
else:
    print("no")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NESTED IF:
age = 22
name = "soha"
if age > 20:
    if name == "soha":
        print("true")
    else:
        print("false")
else:
    print("no")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# and :
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
else:
    print("false")
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # or
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
else:
    print("false")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NOT
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
else:
    print("false")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# LOOPS 1-FOR
for i in range(4):
    print("hi")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for i in range(1, 4):
    print("welcome")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
for i in range(1, 6, 2):
    print("MET")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     2-NESTED FOR :
for i in range(4):
    print("hi")
    for j in range(2):
        print("welcome")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\
# WHILE:
i = 0
while i < 6:
    print(i)
    i = i + 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NESTED WHILE:
i = 0
while i < 4:
    print(i)
    i = i + 1
    j = 1
    while j < 3:
        print(j)
        j = j + 1
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BREAK:
for i in range(5):
    if i == 3:
        break
    print(i)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CONTINUE:
for i in range(5):
    if i == 3:
        continue
    print(i)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# list []
# بتاخد قيم نصيه ورقميه وممكن اعمل list جوا list وبتاخد قيم boolean
Lista = ["ahmed", 1, True, 10.5, [1, 2, 3, [4, 5, 6]]]
# لطباعه list كلها
print(Lista)
# لطباعه اول عنصر فى list
print(Lista[0])
print(Lista[4][3][0])
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
names = ["ali", "mohamed", "noha", "omar", "soha"]
names.append("sohaila")
print(names)
names.insert(2, "sohaila")
print(names)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# الحذف
names = ["ali", "mohamed", "noha", "omar", "soha"]
names.pop()
print(names)
names.pop(1)
print(names)
names.remove("noha")
print(names)
names.clear()
print(names)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SORT:
names = ["ali", "mohamed", "noha", "omar", "soha"]
names.sort()
print(names)
names.sort(reverse=True)
print(names)
