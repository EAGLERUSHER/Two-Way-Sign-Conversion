# - *- coding: utf- 8 - *-
from textblob import  TextBlob

word10=TextBlob("i am hungry")
m=word10.translate(from_lang='en',to='ta')
print(m)

import gtts as gt 
import os      
 
TamilText=str(m)
tts = gt.gTTS(text=TamilText, lang='ta')
tts.save("Tamil-Audio.mp3")
os.system("Tamil-Audio.mp3")


