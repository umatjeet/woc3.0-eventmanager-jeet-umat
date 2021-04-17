import pyttsx3
import datetime
import speech_recognition as sr
def takecommand():
    r=sr.Recognizer();
    with sr.Microphone() as source:
        print("Listing.......")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again Please") 
        return "None"       
    return query
q=takecommand()
print(q)