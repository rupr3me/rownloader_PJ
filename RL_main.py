from pytube import YouTube
from pytube import Stream
import sys
from tendo import singleton
from tkinter import * 
import tkinter.ttk as ttk


tk = Tk()


tk.title("RownLoader - Youtube Downloader")
tk.geometry("640x480")
tk.resizable(False, False)

RownLoader = PhotoImage(file="noname.png")
label1 = Label(tk, image=RownLoader)
label1.pack()

Phere = PhotoImage(file="noname2.png")
label2 = Label(tk, image=Phere)
label2.pack()


label4 = Label(tk, height=1)
label4.pack()

url_input = Entry(tk,width=50)
url_input.pack()




def dw_run():
    singleton.SingleInstance()
    rllurl = url_input.get()
    yt = YouTube(rllurl)
    st = Stream(rllurl, 0, 0)
    print("검색중...")
    #Showing details
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("파일사이즈", st.filesize)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    dw_location = input("어디에 저장할까요? : ")

    #Starting download
    print("Downloading...")
    ys.download(dw_location)
    print("Download completed!!")


label3 = Label(tk, height=2)
label3.pack()

down = PhotoImage(file="noname3.png")
btn1 = Button(tk, image=down, command=dw_run)
btn1.pack()

tk.mainloop()