from tkinter import *
import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from datetime import datetime

root = Tk()
root.geometry("500x500")
root.configure(bg="lightblue")
text_to_speech =pyttsx3.init()

lbl = Label(root, text="computer assistant", bg="lightblue", font=("Bahnshcrift Light",15,"bold"))
lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio ():
    speak("how can i help you")
    speech_recognisor  = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_data =""
        try:
            voice_data = speech_recognisor.recognize_google(audio, language="en-in")
        except sr.UnknownValueError:
            print("please repeat i did not get that")
            speak("please repeat i did not get that")
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        print("my name is zain")
        speak("my name is zan")
    if "time" in voice_data:
        speak("the current time is: ")
        now=datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    
    if "search" in voice_data:
        speak("opening google")
        print("opening google")
        webbrowser.get().open("https://www.google.com/")
        
    if "video" in voice_data:
        speak("opening youtube")
        print("opening youtube")
        webbrowser.get().open("https://www.youtube.com/")
        
    if "write" in voice_data:
        speak("opening notepad")
        print("opening notepad")
        subprocess.popen(["notepad.exe"])


btn = Button(root, text="start", bg="red", fg="white",padx=10, pady=1, font=("Bahnshcrift Light", 15,"bold"), relief=FLAT, command=r_audio)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
  
root.mainloop()