import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +88")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")
         
     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
   
     elif "Facebook" in inp:
         os.system("termux-open https://m.facebook.com/")           
                   
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "who are you" in inp:
         subprocess.call(["termux-tts-speak","I am your virtual assistanct Termux, sir"])
         
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","you can call me termux "])
     
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by SKB TEAM"])
     elif "video" in inp:
         os.system("termux-open https://www.facebook.com/100067022092284/posts/pfbid0sQC3g6rHgEhZ9tY1jNcnyTxDRypmcq3wVXBggQeQfc1WKccFkzAL8TePHGequaxml/?app=fbl")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")