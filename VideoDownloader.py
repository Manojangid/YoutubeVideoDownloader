import youtube_dl
import pafy
from tkinter import *
from threading import *
from tkinter import messagebox

# Operation Function
def startMyThread():
    x = Thread(target=getInformation, daemon=True)
    x.start()

def getInformation():
    label_info_var.set("Getting Video information, Please wait...")
    url = entry_url_var.get()
    video = pafy.new(url)
    label_info_var.set("Video Information : ")
    label_title_var.set("Title : " + str(video.title))
    label_channel_var.set("Channel : " + str(video.author))
    label_rating_var.set("Rating : " + str(video.rating))
    label_views_var.set("Views : " + str(video.viewcount))
    label_likes_var.set("Likes : " + str(video.likes))
    label_dislikes_var.set("Dislikes : " + str(video.dislikes))

    # ListItems for video resolutions
    label_quality = Label(root, text="Select video resolution :",font='Helvetica 10 bold').grid(row=9, column=0, padx=16, pady=8, sticky=W)

    streams = video.streams
    i = 1
    for qaulity in streams:
        listbox.insert(i, qaulity)
        i = i + 1
    listbox.grid(row=10, column=0, padx=16, sticky=W)
    listbox.select_set(0)
    # Download Now
    button_download.grid(row=11, column=0, pady=8,padx=2)
    button_download_mp3.grid(row=11, column=0, padx=16,pady=8, sticky=W)

def startMyThreadDownloading():
    x = Thread(target=downloadNow, daemon=True)
    x.start()

def startMyThreadForMp3():
    x = Thread(target=DownloadMp3, daemon=True)
    x.start()

def DownloadMp3():
    label_download_var = StringVar()
    Label(root, textvariable=label_download_var).grid(row=12, column=0, padx=16, pady=16, sticky=W)
    label_download_var.set("Downloading...")
    url = entry_url_var.get()
    video = pafy.new(url)
    bestaudio = video.getbestaudio()
    bestaudio.download()
    label_download_var.set("Download Completed.")

def downloadNow():
    button_download.configure(state=DISABLED)
    label_download_var = StringVar()
    Label(root, textvariable=label_download_var).grid(row=12, column=0, padx=16, pady=16, sticky=W)
    # starting download

    label_download_var.set("Downloading...")
    url = entry_url_var.get()
    video = pafy.new(url)
    streams = video.streams
    for i in streams:
        print(i)

    if "3gp" in str(listbox.get(ACTIVE)):
        best = video.getbest(preftype="3gp")
        best.download()
    elif "webm" in str(listbox.get(ACTIVE)):
        best = video.getbest(preftype="webm")
        best.download()
    elif "mp4" in str(listbox.get(ACTIVE)):
        best = video.getbest(preftype="mp4")
        best.download()
    else:
        label_download_var.set("Please select video resolution.")
    label_download_var.set("Download Completed.")


# Main GUI Setup
root = Tk()
root.geometry("550x550")
root.minsize(550, 550)
root.title("YouTube Downloader")

def About_us():
    msg = "YouTube Video Downloader\nDesigned and Developed by Manoj Jangid\n\n" \
          "Open Source Libraries used:\n" \
          "-> pafy 0.5.5\n" \
          "-> youtube_dl\n" \
          "-> tkinter\n\n" \
          "Copyright 2019 YouTube Video Downloader"
    messagebox.showinfo("About us",msg)
#menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="About us", command=About_us)

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Help", menu=filemenu)
root.config(menu=menubar)


# Widgest
# row 1
label_paste = Label(root, text="Paste video url here : ",font='Helvetica 12 bold').grid(row=0, column=0, padx=16, pady=16)
entry_url_var = StringVar()
entry_url = Entry(root, width=50, textvariable=entry_url_var).grid(row=1, column=0, padx=26, sticky=W)

# row 2
label_info_var = StringVar()
label_info = Label(root, textvariable=label_info_var,font='Helvetica 10 bold').grid(row=2, column=0, padx=16, pady=8, sticky=W)
label_title_var = StringVar()
label_title = Label(root, textvariable=label_title_var).grid(row=3, column=0, padx=16, sticky=W)
label_channel_var = StringVar()
label_channel = Label(root, textvariable=label_channel_var).grid(row=4, column=0, padx=16, sticky=W)
label_rating_var = StringVar()
label_rating = Label(root, textvariable=label_rating_var).grid(row=5, column=0, padx=16, sticky=W)
label_views_var = StringVar()
label_views = Label(root, textvariable=label_views_var).grid(row=6, column=0, padx=16, sticky=W)
label_likes_var = StringVar()
label_likes = Label(root, textvariable=label_likes_var).grid(row=7, column=0, padx=16, sticky=W)
label_dislikes_var = StringVar()
label_dislikes = Label(root, textvariable=label_dislikes_var).grid(row=8, column=0, padx=16, sticky=W)

listbox = Listbox(root, width=35, height=6)
button_download = Button(root, text="Download Video", command=startMyThreadDownloading)
# Button Go for get all information
button_go = Button(root, text="Go", command=startMyThread).grid(row=1, column=2, padx=2)
button_download_mp3 = Button(root, text="Download Mp3", command=startMyThreadForMp3)

root.mainloop()
