# # tkinter: استدعاءمكتبه الخاصه بالواجهات الرسوميه
# from tkinter import *

# #  بستخدمها لانشاء واجهه رسوميه:TK
# # myframe: اسم المتغير الذي سيتم استخدامه للتحكم في النافذة
# myframe = Tk()
# # mainloop(): داله بستخدمها علشان النافذه تفضل مفتوحه
# myframe.mainloop()

# # =========================================================================
# from tkinter import *

# myframe = Tk()
# # علشان اغير اسم النافذه
# myframe.title("My App")
# # بتحدد حجم نافذة التطبيق
# # 500: عرض النافذه
# # 400:طول النافذه
# myframe.geometry("500x400")

# myframe.mainloop()

# # =========================================================================

# # لانشاء زر على الواجهه
# from tkinter import *

# myframe = Tk()
# myframe.title("My App")
# myframe.geometry("500x400")

# Button(): داله بستخدمها لانشاء زر
# myframe: المكان اللى هيتحط عليه الزر
# text: اسم الزر
# fg: لون النص
# bg: لون خلفيه الزر
# font="Helvatica 20 bold": نوع الخط والحجم والسمك
# padx:=> مساحه داخليه للعنصر على محور x
# pady:=> مساحه داخليه للعنصر على محور y
# command: عند الضغط على الزر يقوم بعمل شئ معين

# mybutton = Button(
#     myframe,
#     text="Exit",
#     fg="red",
#     bg="gray",
#     font="Helvatica 20 bold",
#     padx=80,
#     pady=10,
#     command=exit,
# )

# # لعرض لزر على الواجهه
# mybutton.pack()
# # mybutton.pack(side=LEFT)

# myframe.mainloop()

# # ======================================================================

# # # لانشاء زر واشاء داله عند الضغط على الزر يقوم بتنفيذ الداله
# from tkinter import *


# # عملت داله وحطيت فيها امر الخروج
# def myfunction():
#     exit()


# # command: حطيت فيها اسم الداله بتاعتى لما اضغط عليها هينفذ اللى جوا الداله وهو امر الخروج
# myframe = Tk()
# myframe.title("My App")
# myframe.geometry("500x400")
# mybutton = Button(
#     myframe,
#     text="Exit",
#     fg="red",
#     bg="gray",
#     font="Helvatica 20 bold",
#     padx=80,
#     pady=10,
#     command=myfunction,
# )
# mybutton.pack()
# myframe.mainloop()

# # ==============================================================================

# from tkinter import *
# # مكتبه خاصه بالويب
# import webbrowser
# # عملت داله عند تنفيذها تقوم بفتح لينك على ويب
# def myfunction():
#     webbrowser.open("https://www.google.com/")

# myframe = Tk()
# myframe.title("My App")
# myframe.geometry("500x400")

# # لانشاء label
# mylabel = Label(myframe, text="Web Browser", font="Helvatica 0 bold")
# # pady: هنا بتبعد العنصر دا عن العنصر اللى بعده
# mylabel.pack(pady=20)
# # command: تنفيذ الداله
# mybutton = Button(
#     myframe,
#     text="Google",
#     fg="black",
#     bg="gray",
#     font="Helvatica 12 bold",
#     padx=80,
#     pady=10,
#     command=myfunction,
# )
# mybutton.pack()
# myframe.mainloop()

# # =========================================================================


# # لادخال نص
# from tkinter import *

# # مكتبه خاصه بالويب
# import webbrowser
# # عملت داله عند تنفيذها تقوم بفتح لينك على ويب
# def myfunction():
#     # هات النص اللى موجود عندى فى المربع text
#     link = mytext.get()
#     webbrowser.open(link)

# myframe = Tk()
# myframe.title("My App")
# myframe.geometry("500x400")

# # لانشاء label
# mylabel = Label(myframe, text="Web Browser", font="Helvatica 10 bold")
# mylabel.pack(pady=20)

# # لادخال نص
# mytext = Entry(myframe, width=40)
# mytext.pack(pady=10)

# # command: تنفيذ الداله
# mybutton = Button(
#     myframe,
#     text="Go To Link",
#     fg="black",
#     bg="gray",
#     font="Helvatica 12 bold",
#     padx=80,
#     pady=10,
#     command=myfunction,
# )
# mybutton.pack()
# myframe.mainloop()

# # ============================================================================


# pack: ابسط طريقه لعرض العناصر على النافذه

# from tkinter import *

# root = Tk()
# root.geometry("500x400")
# mybutton = Button(
#     root,
#     text="My Button",
#     fg="red",
#     bg="white",
#     padx=10,
#     pady=5,
#     font="Helvatica 10 bold",
# )
# # pack() → دي أسهل طريقة علشان تعرض عنصر في النافذة.
# # side=LEFT → خلي الزرار يتحط من الجهة الشمال.
# # padx=10 → مسافة من الجنب يمين وشمال.
# # pady=20 → مسافة فوق وتحت.
# # anchor="nw" → يربطه بأعلى الشمال (north-west).
# # anchor(n s e w):بيتحكم ف الاتجاهات شمال جنوب شرق غرب
# mybutton.pack(side=LEFT, padx=10, pady=20, anchor="nw")
# # لانشاء  حقل ادخال
# myinput = Entry(root, width=20)
# # ipadx: اضافه مساحه داخليه للعنصر على محور x
# # ipady:اضافه مساحه داخليه للعنصر على محور y
# # fill=x or y or Both:مربع الادخال يكبر كل ماكبرت الواجهه على محور x اوy
# # expand=True: هستخدمها لو انا مستخدمه خاصيه side
# myinput.pack(side=LEFT, padx=10, pady=20, anchor="nw", ipady=50, fill=X, expand=True)
# root.mainloop()
