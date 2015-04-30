import Tkinter
from PIL import Image, ImageTk

def createGUI():
    #create window
    window = Tkinter.Tk()
    window.geometry("1296x810+50+10")
    window.title("Project name here");

    #background
    im = Image.open('bckg.jpg')
    tkimage = ImageTk.PhotoImage(im)
    myvar=Tkinter.Label(window,image = tkimage)
    myvar.place(x=0, y=0, relwidth=1, relheight=1)

    #textbox
    v = Tkinter.StringVar()
    txtBox = Tkinter.Entry(window, textvariable = v)
    txtBox.pack()
    v.set("enter username")
    txtBox.focus_set()
    username = v.get()

    print(username)

    #run
    window.mainloop()