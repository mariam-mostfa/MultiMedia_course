# FUNCTION:
# without return
def y():
    n1 = 5
    n2 = 10
    n = n1 + n2
    print(n)


y()


# --------------------------------------------
# with return :
def r():
    n1 = 5
    n2 = 10
    n = n1 + n2
    return n


n = r()
print(n)


# -------------------------------------------------------
# PARAMETERS:
def w(name, age):
    print(name, age)


w("soha", 25)


# ------------------------------------------------------
def my_fun(child3, child2, child1):
    print("The youngest child is " + child3)


my_fun(child1="ali", child2="ahmed", child3="soha")


# -----------------------------------------------------------------------------
def my_function(country="EGYPT"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# ---------------------------------------------------
# ARGUMENT:
def q(*args):
    print(args)
    print(args[1])
    print(args[0:2])


q("soha", "ahmed", 25, "mans", 90)


# ---------------------------------------
def x(**kwargs):
    print(kwargs)


x(first="soha", last="ahmed", age=25, address="mans")
