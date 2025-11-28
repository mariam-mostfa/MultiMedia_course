# # # Play video files in python
# import cv2

# cap = cv2.VideoCapture(r"D:\2026\multimedia\3mly\video2.mp4")

# # التحقق من أن الفيديو مفتوح بشكل صحيح
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow("Video Player", frame)
#         if cv2.waitKey(25) & 0xFF == ord("q"):
#             break
#         # بيمسح الذاكره اللي كان بيستخدمها الفيديو
# cap.release()
# # غلق كل النوافذ اللي انشاتها المكتبه
# cv2.destroyAllWindows()
# # #######################################################
# #  slit video into group of image
# import cv2
# import os
# import shutil

# filename = r"D:\2026\multimedia\3mly\video2.mp4"
# # التحقق من الملف
# if os.path.exists("output"):
#     shutil.rmtree("output")
# os.makedirs("output")
# #  قراءه ملف الفيديو
# cap = cv2.VideoCapture(filename)
# # متغير لحساب عدد الاطارات المحفوظه
# count = 0

# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow("window-name", frame)
#         #  بيحول كل اطار في الفيديو لصوره منفصله وبيحفظها بترتيب رقمي في المجلد
#         cv2.imwrite("./output/frame%s.jpg" % count, frame)
#         count = count + 1
#         if cv2.waitKeyEx(25) & 0xFF == ord("q"):
#             break
#     # ret  يساوي  false اذن لا يوجد اطاارت و يخرج
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()
# ####################################################################
# # Label the image with date and time (hour/second)
# import cv2
# import os
# import shutil

# # الحصول علي الوقت والتاريخ
# from datetime import datetime

# filename = r"D:\2026\multimedia\3mly\video2.mp4"
# if os.path.exists("output1"):
#     shutil.rmtree("output1")
# os.makedirs("output1")

# cap = cv2.VideoCapture(filename)
# count = 0
# while cap.isOpened():
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow("window-name", frame)
#         # الوقت الحالي و بعدين يحوله لدقايق وساعات و ثواني  ويحفظ الصوره ب اسم يعتمد علي الوقت
#         t = datetime.now()
#         #  بتحول النص لوقت (دقايق ساعات ثواني) string format time
#         # 14.30.55 >>> 301455
#         ts = t.strftime("%M%H%S")

#         cv2.imwrite("./output1/frame%s.jpg" % int(ts), frame)
#         count = count + 1
#         if cv2.waitKeyEx(10) & 0xFF == ord("q"):
#             break
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()
