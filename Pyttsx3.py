# pyttsx3
تبدیل متن به صدا#
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate,80)#سرعت صدا
volume=engine.getProperty('volume')
engine.setProperty('volume', 1.0)
engine.say('hello')
engine.runAndWait()#
