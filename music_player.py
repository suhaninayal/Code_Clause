import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer


mixer.init()

class MusicPlayer:#music player class
    def __init__(self,root):
        self.root=root
        self.root.title("MUSIC PLAYER")
        self.root.geometry("300x150")


# load music files
        self.songs=[]
        self.current_song_index=1


#creating buttons for play,pause,stop,and select folders
        self.play_button=tk.Button(root,text="play",command=self.play_music)
        self.pause_button=tk.Button(root,text="Pause",command=self.pause_music)
        self.stop_button=tk.Button(root,text="stop",command=self.stop_music)
        self.select_folder_button=tk.Button(root,text="Select Folder",command=self.select_folder)

#adds buttons to the windows
        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.select_folder_button.pack(pady=10)



        #select folder
    def select_folder(self):
        folder_selected=filedialog.askdirectory()
        if folder_selected:
            self.songs=[os.path.join(folder_selected,song) for song in os.listdir(folder_selected) if song.endswith('.mp3')]
            if self.songs:
                self.current_song_index=1
                self.play_music()


    def play_music(self):
        if self.songs:
            mixer.music.load(self.songs[self.current_song_index])
            mixer.music.play()


    def pause_music(self):
        if mixer.music.get_busy():
            mixer.music.pause()


    def stop_music(self):
        if mixer.music.get_busy():
            mixer.music.stop()

if __name__=='__main__':
    root=tk.Tk()
    app=MusicPlayer(root)
    root.mainloop()
