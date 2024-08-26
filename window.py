from tkinter import *
from tkinter.ttk import *
import miniaudio

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
        #use vlc to stream audio from website url
        with miniaudio.IceCastClient('https://www.radio.net/s/freeukraine') as source:
            stream=miniaudio.stream_any(source,source.audio_format)
            with miniaudio.PlaybackDevice() as device:
                device.start(stream)
