from tkinter import *
from pytube import YouTube 
import os 


root = Tk()
root.title("The better Youtube Video Downloader")
#putting dimensions 
window_width = 700
window_height = 500
#getting the screen dimensions 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#finding the center point 
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

#putting it in center 
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#window is resizable 
root.resizable(0,0)

#adding background color 
root.configure(bg = "cyan")

Label(root,text = "WELCOME TO YOUTUBE DOWNLOADER",font = "Helvetica 23 bold",bg= "cyan").pack()


#making a list for getting the user input for the specific format
list1 = []

#getting the user input for format
def getting_format(choice1):
    choice1 = setup1.get()
    list1.append(choice1)


#list containing different formats 
formats = ["Format", "mp3","mp4"]

#setting up the option menu for format
setup1 = StringVar(root)
setup1.set(formats[0])

#putting the menu in place 
option_menu2 = OptionMenu(root,setup1,*formats, command = getting_format).place(x = 100, y = 250)

#This gives you the list of resolutions
resolutions_given = ["Resolution","144p","240p","360p","480p","720p"]

'''
the list is created to store the video resolutions chosen by the user and then
using it to set it to the resolution
'''
list2 = []

#setting up the option menu for resolution
setup2 = StringVar(root)
setup2.set("Resolution")
option = StringVar()
setup2.set(resolutions_given[0])

#getting the option chosen by the user (here it is specfically for the resolution)
def display_selected(choice2):
    choice2 = setup2.get()
    list2.append(choice2)
    
#putting the menu in place
option_menu1 = OptionMenu(root,setup2,*resolutions_given, command = display_selected).place(x = 100,y= 280)
    
link = StringVar(root)

Label(root,text = "Paste the link here:",font = "Helvetica 18 bold",bg = "cyan").place(x = 50, y = 100 )
link_enter = Entry(root,width = 30, textvariable= link).place(x = 50, y = 125 )

def downloader():
    url = YouTube(str(link.get())) 
    Label(root, text = "Title of the video : " + url.title,font = "aerial 17 bold",bg= "yellow").place(x = 50, y = 150)
    Label(root, text = "Views of the video : " + str(url.views),font = "aerial 15 bold",bg= "cyan").place(x = 50, y = 170)
    Label(root, text = "Length of the video : " + str(url.length) + " seconds ",font = "aerial 15 ",bg= "cyan").place(x = 50, y = 190)
    if list1[-1] == "mp4":
        video = url.streams.filter(res = list2[-1]).first()
        video.download()
    else:
        audio = url.streams.filter(only_audio=True).first()
        # check for destination to save file
        destination = '.'
        #str(">> ") or '.'
  
        #downloading the file
        out_file = audio.download(output_path=destination)
        
        #saving the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        
        
    Label(root,text = "Congratulations!Your file has been downloaded", font = "aerial 15 bold").place(x = 160,y = 400)
    
    

Button(root,text = "Download", width = 30, command = downloader, bg = "red", font = "aerial 15 bold").place(x= 150, y = 350)

root.mainloop()

'''
ideas:
1) you get to choose between mp3 and mp4 
2) you get to choose resolutions (480,1080,720,4k)
3)  

#https://youtu.be/ZrWKq3iKDAY



'''