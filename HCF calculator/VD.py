from tkinter import *
from tkinter import filedialog
import threading
import time
import os
from pytube import YouTube

class YoutubeDownloader:

    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")

        # create widgets
        self.lbl_url = Label(master, text="Video URL:")
        self.lbl_url.pack()
        self.ent_url = Entry(master, width=50)
        self.ent_url.pack(pady=10)

        self.lbl_name = Label(master, text="File Name:")
        self.lbl_name.pack()
        self.ent_name = Entry(master, width=50)
        self.ent_name.pack(pady=10)

        self.btn_browse = Button(master, text="Browse", command=self.browse_directory)
        self.btn_browse.pack()

        self.btn_download = Button(master, text="Download", command=self.download_video)
        self.btn_download.pack(pady=20)

        self.lbl_status = Label(master, text="")
        self.lbl_status.pack()

        # set variables
        self.video_url = ""
        self.video_name = ""
        self.directory_path = ""

    def browse_directory(self):
        self.directory_path = filedialog.askdirectory()

    def download_video(self):
        self.video_url = self.ent_url.get()
        self.video_name = self.ent_name.get()

        # validate inputs
        if not self.video_url or not self.video_name:
            self.show_alert("Please enter a valid URL and file name.")
            return

        try:
            # get video object and stream
            yt = YouTube(self.video_url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()

            # set download path and start download
            download_path = os.path.join(self.directory_path, self.video_name + ".mp4")
            stream.download(download_path)

            # update status label
            self.lbl_status.config(text="Download complete!")
        except Exception as e:
            self.show_alert("Error: " + str(e))

    def show_alert(self, message):
        alert_window = Toplevel(self.master)
        alert_window.title("Error")
        alert_label = Label(alert_window, text=message)
        alert_label.pack(padx=10, pady=10)
        alert_button = Button(alert_window, text="OK", command=alert_window.destroy)
        alert_button.pack(pady=10)

# create window and run app
root = Tk()
app = YoutubeDownloader(root)
root.mainloop()
