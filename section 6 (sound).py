# from playsound import playsound

# playsound(r"D:\2026\multimedia\3mly\sound.wav")

#####################################################################

# import winsound

# # winsound.Beep(التردد, المدة) - التردد من 37 إلى 32767
# winsound.Beep(38, 3000)
# winsound.Beep(1000, 500)
# winsound.Beep(4000, 5000)
# winsound.Beep(9000, 800)
# winsound.Beep(8000, 3000)

#########################################################################

# from gtts import gTTS
# from playsound import playsound

# # النص المطلوب تحويله إلى صوت
# mytext = (
#     "hello our engineers, welcome to met academy, we hope you will be happy with us"
# )

# # إنشاء كائن gTTS وحفظه كملف mp3
# myjob = gTTS(text=mytext, lang="en")
# myjob.save("welcome.mp3")

# # تشغيل الملف الصوتي
# playsound("welcome.mp3")

##############################################################
# import winsound

# filename = r"D:\2026\multimedia\3mly\sound.wav"
# winsound.PlaySound(filename, winsound.SND_FILENAME)

###################################################################
# import pyttsx3
# engine = pyttsx3.init()

# text = "hello world"
# engine.say(text)

# engine.say(
#     "hello our engineers, welcome to met academy, we hope you will be happy with us"
# )
# engine.runAndWait()

############################################################

# import pyttsx3

# # تهيئة المحرك
# engine = pyttsx3.init()

# # تعيين اللغة العربية (إن كانت مدعومة)
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# engine.say("welcome in python")
# engine.runAndWait()

# #################################################################

# import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# for voice in voices:
#     if "arabic" in voice.name:
#         engine.setProperty("voice", voice.id)
#         break
#     else:
#         print("No Arabic voice found")
# text = "Welcome to the world of programming"
# engine.say(text)
# engine.runAndWait()
