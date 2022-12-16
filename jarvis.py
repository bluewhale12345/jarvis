import speech_recognition as sr
import pyttsx3

listner=sr.Recognizer()
engine = pyttsx3.init()
engine.say('hi i am jarvis')
engine.say('my programer made me for no use so i quit my job')
engine.runAndWait()
try:
  with sr.Microphone() as source:
    print('listening.....')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    command = command.lower()
    if 'jarvis' in command: 
        print(command)
except:
    pass 
