import pyttsx3
import pyaudio
import datetime
from requests.models import ContentDecodingError
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

from wikipedia.wikipedia import random

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)

    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("This is bee")
    strtime =  datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"its {strtime}",)
    speak("How may i help you sir!!")


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('vg733834@gmail.com','gupta.ad')
    server.sendmail('vg733834@gmail.com',to,content)
    server.close()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio=r.listen(source)
    try:
        print("Recognizing..")
        speak("Recognizing sir")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please.....")
        return "None"
    return query


if __name__=="__main__" :
    wishMe()
    while 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "introduce" in query:
            speak("Allow me to introduce Myself")
            speak("I am bee..")
            speak('A virtual artificial intelligence and i am here to assist you a variety of task as best as i can')
            speak('Twenty Four Hours a day,..seven days a week')
            speak("system is now fully operational Ready to service Sir!!")

        elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            speak('Opening StackOverflow')
            webbrowser.open("stackoverflow.com")

        elif 'play music'in query:
            speak('Playing Music')
            music_dir='D:\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[6]))

        elif 'open code'in query:
            codepath="C:\\Users\\vg733\\AppData\\Local\\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif 'open gdb compiler'in query:
            speak("Opening GDB Compiler sir")
            webbrowser.open("https://www.onlinegdb.com/online_c++_compiler")

        elif 'open u m s'in query:
            speak("Opening U..M..S ")
            webbrowser.open("https://ums.lpu.in/lpuums/")
