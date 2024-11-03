import tkinter
import customtkinter
from yt_dlp import YoutubeDL

#System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame settings
app = customtkinter.CTk()   #To initialise it
app.geometry("720x480")     #To set the size of the app
app.title("Youtube Downloader")     #To set the title of the app

#=============================================FUNCTIONS HERE==================================
def my_hook(d):
    if d['status'] == 'downloading':
        # print ("downloading "+ str(round(float(d['downloaded_bytes'])/float(d['total_bytes'])*100,1))+"%")
        value = round(float(d['downloaded_bytes'])/float(d['total_bytes'])*100,1)
        percentage.configure(text = str(value) + "%")
        percentage.update()
        progressBar.set(value/100)

    if d['status'] == 'finished':
        filename=d['filename']
        print(filename)

def start_download():
    try:
        youtubeLink = link.get()
        # Configuration for YoutubeDL
        ydl_opts = {
            # 'format': 'best',
            'format': 'best', #video[width<=1080]+bestaudio/best
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [my_hook]
        }
        with YoutubeDL(ydl_opts) as yt_dlp_object:
            yt_dlp_object.download([youtubeLink])
        print("Download Complete!")
        onCompleteLabel.configure(text="Download Completed!", text_color = "green")
    except:
        print("Youtube link is invalid!")
        onCompleteLabel.configure(text="Download Failed!", text_color = "red")

def clearing():
    if (progressBar.get() != 0.0) and (progressBar.get() != 1.0):
        print(progressBar.get())
        onCompleteLabel.configure(text="Wait for download to be completed!", text_color = "red")
    else:
        #Clear progress bar
        progressBar.set(0)
        #Clear percentage value
        percentage.configure(text="0%")
        percentage.update()
        url_var.set("")
        onCompleteLabel.configure(text="Page Resetted!", text_color = "green")

#=============================================UI ELEMENTS HERE==================================
#Title
title = customtkinter.CTkLabel(app, text= "Insert YouTube link here:")
title.pack(padx=10, pady=10)

#YouTube link field
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Progress bar
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Download button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=10, pady=10)

#Clear all button
clearAll = customtkinter.CTkButton(app, text = "Clear All", command = clearing)
clearAll.pack(padx=10, pady=10)

#Labels
onCompleteLabel = customtkinter.CTkLabel(app, text="")
onCompleteLabel.pack()


# Run the app continuously
app.mainloop()