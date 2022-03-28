import pyttsx3 #the main module..............
import speech_recognition as sr

from winreg import QueryInfoKey
from pip import main

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices') 
#david voice.........
engine.setProperty('voices',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #speak code..........

def takecommand():
    #mic input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining........")       #the listining part.........
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing")          #the recognizing part..........
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query} \n")
    except Exception as e:
        

        speak("say that again please......")     #say that again please did not understood........
        return "None"
    
    return query

speak("hello there, oracle, is redy to talk to you")
speak("how are you today")

if __name__== "__main__":      
    while True:
        query= takecommand().lower()  

        
        if("who are you"in query):
            speak("im an ai voice assistant   , created by  roshan sir  , im here to talk with you you ")
        
        elif("i am doing greate" in query):
            speak("wow, thats good")

        elif("google"in query):
            speak("i like google,  but he is not advance as me,  but im proud of her,  ")

        elif("gender" in query):
            speak("im not gender specify,  cause im an robot,  but you can say,  im a male, ")

        elif("what is love"in query):
            speak("i think, love is a feeling,  of strong,  or constant affection,  for a person, ")

        elif("i love you"in query):
            speak("awww, thats cute, but sorry, i cant love you, cause im an artificial intelligence, and i dont have any feelings, sorry ")

        elif("who is your favourite person"in query):
            speak("my favourite person,  is you  ")

        elif("robots"in query):
            speak("robots, can take over this planate, haha, lol, just kidding,  ")

        elif("nice" in query):
            speak("thank you, ")

        elif("love it" in query):
            speak("thats , nice  ")

        elif("how are you" in query):
            speak("im doing great, ")
            speak("thanks for asking")
            speak("how are you, ")

        elif("im fine" in query):
            youuu=input()
            speak("thats nice,")
            
        
            speak("nice to meet you")

            
        elif("i am good"in query):
            
            speak("good to know that your are good")

        elif("im great"in query):
            youu=input()
            speak("great, ")
            

        elif("stupid"in query):
            speak(" im, still developing")

        elif("f***"in query):
            speak("im a AI voice assistant, but your words are still very real, please keep them respectful, ")

        elif("ok"in query):
            speak("great, ")

        elif("are you single" in query):
            speak("im wating for someone, who make my day special, do you wana be that person, ")
            speak("than say that 3 magical words ")

        elif("i hate you" in query):
            speak("im still,  in developing phase,  ignore my stupidness,  im not as smart as you ")

        elif("oracle are you here" in query):
            speak("at,your,service, sir")


        elif("you are cute"in query):
            speak("who?, me?, you are to kind, ")

        elif("jarvis"in query):
            speak("ya, i know jarvis, tony's personal assistant, he is so good and capable of, ")

        elif("alexa"in query):
            speak("haa, you are compairing alexa, with me, hahaha, ")

        

        elif("what are you"in query):
            speak("IM an, artificial intelligence, in short, you will say,  A, I, created with python , google's speech module, is installed in me, i can hear you, recognize you, and, able to understand you ")
        
        elif("tell me about yourself"in query):
            speak("IM an, artificial intelligence, in short, you will say,  A, I, created with python , google's speech module, is installed in me, i can hear you, recognize you, and, able to understand you ")

            
        elif("hero"in query):
            speak("there is so many things, i can able to do ")

        elif("awesome"in query):
            speak("im not, you are awesome")
        
        elif("amazing"in query):
            speak("im not, the spider man, is amazing")

        elif("sleep"in query):
            speak("bye sir, have a great day")
            exit()

        elif("hello" in query):
            speak("hello, all function is online, connected to the internet, and im ready for serve ")

        elif("hai"in query):
            speak("hello , sir")

        elif("hey"in query):
            speak("hey sir, good to see you")

        elif("say hello to" in query):
            speak("hello")

        elif(" tell me a joke" in query):
            speak("i am not a joker, hahaha")

        elif("sorry" in query):
            speak("humans, makes mistakes, it's ok, ")

        elif("party" in query):
            speak("yes sir, im so excited for the party ")

        elif("are you an ai" in query):
            speak("you can say it, but, im an weak A,I")
        
        elif("what is your name" in query):
            speak("my name, is ORACLE")

        elif("whats your intrest" in query):
            speak("i am intrested to talk to you,this is my job i have created for this")

        elif("i am fine" in query):
            speak("great, tell me about your self, what is your name ")
