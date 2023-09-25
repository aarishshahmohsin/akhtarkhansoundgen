from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment
from pydub.effects import speedup
  
import os
  
print("enter the text you want to play")
mytext = input()
  
language = 'en'
  
myobj = gTTS(text=mytext, lang=language, slow=False)
  
myobj.save("new.mp3")
audio = AudioSegment.from_file("new.mp3", format="mp3")

audio.export("welcome.mp3", format="mp3")

playsound("./welcome.mp3")
playsound("./1.mp3")
playsound("./welcome.mp3")
playsound("./2.mp3")
playsound("./welcome.mp3")
playsound("./3.mp3")
playsound("./welcome.mp3")
playsound("./x.mp3")
playsound("./welcome.mp3")
playsound("./6.mp3")