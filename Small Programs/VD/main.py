from pytube import YouTube
import time

url = input("URL: https://youtube.com/")

path = "C://Users//vihaa//OneDrive//Desktop"
name = input("Name of file (Do not put file extension): ")

yt = YouTube("https://youtube.com/"+url)
yt.streams.filter(res="720p", progressive = True, file_extension="mp4").first().download(output_path=path, filename=name+".mp4")

print("The .mp4 file is saved to your desktop")

time.sleep(5)
