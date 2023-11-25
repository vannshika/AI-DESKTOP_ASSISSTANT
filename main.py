import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
from googlesearch import search
from gtts import gTTS
import os
from bs4 import BeautifulSoup
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import pyautogui




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning!")
    elif(hour>=12 and hour<=18):
        speak("good afternoon!")
    else:
        speak("good evening")   
    speak("I am your desktop assisstant.Please tell me how can I help you")

def takeCommand():
    #it take microphone input fromuser and returns string ouput

  r=sr.Recognizer()
  with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold=1 
      audio= r.listen(source)
   
  try:
      print("Recogonizing..")
      query=r.recognize_google(audio,language='en-in')   
      print(f"user said: {query}\n")

  except Exception as e:
       #print(e)
      print("can you say that again...")
      return"None"
  return query





if __name__ == "__main__":
 wishMe()
while True:
    query=takeCommand().lower()

    
    
    try:
         if 'wikipedia' in query:
            speak('searching om wikipedia..')
            speak("please wait...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according yo wikipedia")
            print(results)
            speak(results)
    except Exception as e:
        speak("Sorry, I couldn't fetch the search results. Please try again.")  
    
    break


if 'hello my assistant' in query or 'hello assistant' in query:
 speak("hi how was your day")
 user_responce=takeCommand().lower()
 if any(word in user_responce for word in['good','fine','great','nice','wonderful']):
  speak("that's wonderful to hear! how can  I assist you furthur")
 else:
  speak("I am sorry to hear that....Hope tomorrow will be better.")
else: 
 if 'open google' in query:
   webbrowser.open("google.com")
 elif'open youtube ' in query:
  webbrowser.open("youtube.com")
 elif 'what is the time' in query:
   strfTime=datetime.datetime.now().strftime("%H:%M")
   print(f"the time is{strfTime}")
   speak(f"the time is{strfTime}") 
 elif 'tell a joke' in query:
   joke=pyjokes.get_joke()
   print(joke)
   speak(joke)
 
 elif 'play' in query:
   query=query.replace('play','')
   speak('playing'+ query)
   pywhatkit.playonyt(query)
 elif'invent' in query:
   speak("please tell me what to write")  
   while True:
      writeInNotepad=takeCommand()
      if writeInNotepad=="exit typing":
         speak("done ")
 elif 'screenshort' in query:
    pyautogui.hotkey('win','PrtScr')
    speak("done") 
            
 elif 'exit' in query:
  speak("bye Have a nice.... day")
  quit()   

      


    