from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x250'); window.title('optic Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load song',  width = 8, font = ('Times', 12), command = self.load)
        start = Button(window, text = 'start music',  width = 8,font = ('Times', 12), command = self.play)
        Pause = Button(window,text = 'Pause music',  width = 8, font = ('Times', 12), command = self.pause)
        Stop = Button(window ,text = 'Stop music',  width = 8, font = ('Times', 12), command = self.stop)
        Load.place(x=0,y=50);start.place(x=220,y=50);Pause.place(x=220,y=150);Stop.place(x=0,y=150) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()
