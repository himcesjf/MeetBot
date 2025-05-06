import pyttsx3
#import objc

#print(objc.__version__)
#engine = pyttsx3.init()
'''
engine = pyttsx3.init(driverName='espeak')  # 'nsss' 'espeak' drivers
engine.say("Hello, this is a test.")
engine.runAndWait()
'''

engine = pyttsx3.init(driverName='nsss')
engine.say("Hello, this is a test using the nsss driver.")
engine.runAndWait()