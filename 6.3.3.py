from gtts import gTTS
import os
mytext = "first time i'm using a package in next.py course"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("example6.mp3")
os.system("start example6.mp3")