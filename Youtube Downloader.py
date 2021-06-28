import tkinter
from typing import Literal, Set
from pytube import YouTube
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from pynput.mouse import Listener
from pynput import mouse

class App(tk.Frame):
    

    def __init__(self, master):
        super().__init__(master)
        self.pack()
        #Entry Functions
        entry1=self.s = tk.Entry()
        entry1.pack()
        entry2=self.s1 = tk.Entry()
        entry2.pack()
        a="Link"
        b="Konum"
        entry1.insert(0,a)
        entry2.insert(0,b)
        
        #Finished Messagebox
        def message():
            tkinter.messagebox.showinfo(title="Finished",message="Bitti")
         
        #Youtube downloader function 
        def youtub():
            entry1=str(self.s.get())
            entry2=str(self.s1.get())
            from pytube import YouTube
            import pytube
            link = entry1
            konum = entry2
            yt = pytube.YouTube(link)
            stream = yt.streams.first()
            stream.download(output_path=konum)
            message()
        
        #Button Function
        self.button=tk.Button(command=youtub,height=1,text="İndir !")
        self.button.pack()


root = tk.Tk()
myapp = App(root)
myapp.mainloop()
