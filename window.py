from tkinter import *
from tkinter.ttk import *
import pafy

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

        #steram the audio
        video = pafy.new(url='https://www.youtube.com/watch?v=h4VJGNNSQnw&list=RDMMimBlPXbAv6E&index=3',ydl_opts={'nocheckcertificate':True})
        print(video)
        best=video.getbestaudio()
        stream_urls=best.url
        print(stream_urls)

        #get around the above error with Selenium browser addon

#https://www.youtube.com/watch?v=S3oPb63TPUY
#https://www.radio.net/s/freeukraine