from tkinter import *
from tkinter.ttk import *
import requests
from playsound import playsound

#the idea is to branch this button out to another ifle where we can listen to a random piece of stalker music from the game and radio stations.
class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("New Window")
        self.geometry("200x200")
        label = Label(self, text="This is a new Window")
        label.pack()
        label.configure(background='red')
        self.configure(background='blue')

        #play the sound
        url = 'https://www.youtube.com/watch?v=SCGA38auFIc&t=346s'

        #stream audio
        with requests.get(url,stream=True) as r:
            r.raise_for_status()
            with open("temp_audio.mp3","wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        playsound('temp_audio.mp3')

        #get around the above error with Selenium browser addon

#https://www.youtube.com/watch?v=S3oPb63TPUY
#https://www.radio.net/s/freeukraine