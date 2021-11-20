import pyttsx3 #text to speech recognization
import datetime # to know date and time
import pytz #time zone functionalities
import speech_recognition as sr #use in spoken words to text
import wikipedia
import smtplib # helps in sending mails
from myids import password, my_gmail, destination
import webbrowser #for browsing on internet
import os #provides functions for interacting with the operating system
import pyautogui # allows to control the mouse and keyboard functions (in taking screenshots)
import psutil #used to know the battery status(it installed with sensors)
import pyjokes #module used to get jokes
import requests #allows us to to send http requests
from bs4 import BeautifulSoup #python library for pulling data out of html and xml files

p = password
g = my_gmail
d = destination

engine = pyttsx3.init('sapi5') #text to speech application
voices = engine.getProperty('voices') #gets the value of an engine property
engine.setProperty('voice', voices[1].id) #comes out with female voice

#defining a function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#callinf function

#defining a time function
def time():
    t_now = datetime.datetime.now().strftime('%H:%M:%S')# creates datetime object containing the current local time (imports datetime module)
    # print(t_now)
    speak("Time is ")
    speak(t_now) #calling function

#defining function to know date by using pytz module
def date():
    t_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))# creates datetime object containing the current local date (imports datetime module)
    #calling a function
    speak(t_date.strftime('%d %B, %Y'))

#defining a function to greet
def greet():
    hour = int(datetime.datetime.now().hour) #function called hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("This is bee")
    strtime = datetime.datetime.now().strftime("%H:%M:%S")# used to convert date and time to their string representation
    speak(f"its {strtime}", ) #f(formatted string literals that contain replacement fields in curley brackets), used to convert date and time objects to their string representation
    speak("How may i help you sir!!")

#takecommand function is defined using def
def takecommand():
    #repeatedly record phrases from source
    r = sr.Recognizer()
    #Recognizing speech input from the microphone(uses as audio source)
    with sr.Microphone() as source:
        print("Listening..") #calling function
        audio = r.listen(source) #listen for the first phrase and extract it into audio data
    try:
        print("Recognizing..")
        speak("Recognizing sir")
        source = r.recognize_google(audio, language='en-in') #recognize speech using google speech Recognition
        print(f"User said: {source}\n")
    except Exception as e: #used to create an instance of the class networkerror
        # print(e)
        print("Say that again please.....")
        speak("say that again please.....")
        return "None"
    return source
#create a python file with sender mail id and password with the receiver mail id by naming them as my_gmail, password, 
#destination respectively. Now create another python file by importing the sender mail id, password and receiver mail id 
#from the previous created python file as naming p, g, d as password, my_gmail, destination and run code with print(p ,d, g).
def sendemail(to, content):
    #enable low security in gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo() # to connect our server to gmail server
    server.starttls() # to provide security
    server.login(g, p)# insecure connection
    server.sendmail(g, to, content)
    server.close()
#defining a screenshot function
def screenshot():
    img = pyautogui.screenshot() #method that takes screenshot (pyautogui controls the functions of mouse and keyboard)
    img.save("D:\\be.png") #passing name of screenshot to the save() function
    speak("screenshot taken.")
#defining a function pc using module psutil to know battery status
def pc():
    pc = str(psutil.cpu_percent()) #Return a float representing the current system-wide pc utilisation as a percentage
    print(pc)
    speak(f"you used {pc} of pc.")
    battery = psutil.sensors_battery() #returns a tuple consisting percent, secsleft, power_plugged
    speak(f"you used {battery} of battery.")
    print(f"you used {battery} of battery.")
#defining a function joke by using pyjokes module
def jokes():
    joke = pyjokes.get_joke('en', category = 'all')#returns a single joke from a certain categories and language
    print(joke) #calling function
    speak(joke)

if __name__ == '__main__': #main function
    greet()
    while True:
        query = takecommand().lower() # all the commands said by user will be stored here in 'query' and will be converted to lower case for easy recognition of command
        if "time" in query:
            #calling function
              time()
        elif "how are you" in query:
              speak("i am fine, thank you")
              speak("how about you sir")
        elif 'fine' in query or "good" in query:
              speak("it's good to know that your fine")
        elif "introduce" in query:
            #calling function
             speak("Allow me to introduce Myself")
             speak("I am bee..")
             speak('A virtual artificial intelligence and i am here to assist you a variety of task as best as i can')
             speak('Twenty Four Hours a day,..seven days a week')
             speak("system is now fully operational Ready to service Sir!!")
        elif "temperature" in query:
             search = "temprature in phagwara"
             url = f"https://www.google.com/search?q={search}"
             r = requests.get(url)
             data = BeautifulSoup(r.text, "html.parser")
             temp = data.find("div", class_="BNeawe").text
             speak(f"current{search} is {temp}")
        elif "date" in query:
              date()
        elif 'wikipedia' in query:
              speak("Searching sir...")
              query = query.replace("wikipedia", "") #replaces a specified phrase with another specified phrase
              result = wikipedia.summary(query, 2) #wikipedia.summary helps in finding result for the search with 2 sentences
              print(result)
              speak(result)
        elif "send email"  in query:
           try:
              speak("what should i say: ")
              content = takecommand()
              to = d #destination gets the mail
              sendemail(to, content) #send the content to the destination mail id
              print("Email sent successfully.")
              speak("Email sent successfully.")
              #if any error occured used to an instance of the class
           except Exception as e:
              print(e)
              print("Email has not been sent.")
              speak("Email has not been sent.")
        elif "open google" in query:
              webbrowser.open_new_tab("google.com")#helps in opening website in specific browser of new tab
        elif "open youtube" in query:
              webbrowser.open_new_tab("youtube.com") #helps in opening website in specific browser of new tab
        elif 'open gdb compiler' in query:
            speak("Opening GDB Compiler sir") #helps in opening website in specific browser of new tab
            webbrowser.open_new_tab("https://www.onlinegdb.com/online_c++_compiler")
        elif 'open u m s' in query:
            speak("Opening U..M..S ") #helps in opening website in specific browser of new tab
            webbrowser.open_new_tab("https://ums.lpu.in/lpuums/")

        elif "search on chrome" in query:
              speak("what should i search")
              search = takecommand() #uses the takecommand definition function
              chromepath = 'C://Users//91630//AppData//Local//Google//Chrome//Application//chrome.exe %s' #executable path of google chrome
              webbrowser.get(chromepath).open_new_tab(search+'.com') #helps in opening needed website in google chrome with a new tab
        elif "play music" in query:
              speak('Enjoy the music sir..')
              music = 'D:\\Music' #location of the music
              songs = os.listdir(music) #method used in python to get the list of all files and directories in the music directory
              os.startfile(os.path.join(music, songs[0])) #allows us to start a file with associated program by joining one or more path components
        elif "restart" in query:
              speak("do you really want to restart")
              reply = takecommand()
              if "yes" in reply:
                  os.system('shutdown /r /t 1') #method execute the command in a subshell, it code helps in system restart
              else:
                   break
        elif "shutdown" in query:
              speak("do you really want to shutdown")
              reply = takecommand()
              if "yes" in reply:
                  os.system('shutdown /s /t 1') #method execute the command in a subshell, it code helps in system shutdown
              else:
                   break
        elif "write down note" in query:
              speak("what to notedown")
              note = takecommand()
              remember = open("data.txt", 'w') #a statement given to open a text document and giving write permissions
              remember.write(note) #recording the notes
              remember.close()
              speak("Notes complete" + note)
        elif "do you have note" in query:
              remember = open('data.txt', 'r') .read() #giving read permissions for the recorded document notes
              speak("remembered notes" + remember)
        elif "screenshot" in query:
              screenshot() #calling function
        elif "battery" in query:
              pc() #calling function
        elif "joke" in query:
              jokes() #calling function
        elif "exit" in query:
             speak("Thank. You..")
             quit()