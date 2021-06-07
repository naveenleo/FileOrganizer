#Gui
from tkinter import *
import os
import shutil
from tkinter import messagebox


## functions

def mainprog():
    path=leo.get()
    Gtext.set("")
    
    path=path.strip()
    if os.path.isdir(path):
        master='_'
        file_dic={'.psd':master+'PhotoshopFiles','.lnk':master+'Shortcuts','.rar':master+'ZipFiles','.zip':master+'ZipFiles'
                  ,'.png':master+'Icons','.mp3':master+'Music','.mp4':master+'Video','.pdf':master+'Document'
                  ,'.docx':master+'WodrDocument','.py':master+'Python','.jpeg':master+'Photo','.jpg':master+'Photos'
                  ,'.xls':master+'Excel','.xlsx':master+'Excel','.exe':master+'Applications','.txt':master+'TextDocument'
                  ,'@rem@':master+'Others'}

        path+="\\"
        list_files=os.listdir(path)

        #Creating files

        for x in file_dic:
            try:
                os.mkdir(path+file_dic[x])
            except Exception:
                print(x)


        #Moving files

        for file in list_files:
            flag=0
            if not(os.path.isdir(path+file)):
                for x in file_dic:
                    if file.endswith(x) or file.endswith(x.upper()):
                        flag=1
                        shutil.move(path+file,path+file_dic[x])
                if(flag==0):
                    shutil.move(path+file,path+file_dic['@rem@'])


        list_files=os.listdir(path)
        #deleting files
        for x in list_files:
            try:
                if os.path.isdir(path+x) and os.listdir(path+x+"\\")==[]:
                    os.rmdir(path+x)
            except Exception:
                print("Error")

        print("It Works..!!!")
        Gtext.set(">> OPTIMIZED...!!! <<")

    else:
        messagebox.showwarning("Check","Enter a valid directory")
        
    leo.set("")
        



###     Main Program

gui=Tk()

gui.geometry("700x500")
gui.title("File Organizer")
gui.configure(bg='black')

### Icon for gui
cwda =os.path.dirname(os.path.realpath(__file__))
photo = PhotoImage(file = cwda+"\\tkt.png")
gui.iconphoto(False, photo)


leo=StringVar()
Gtext=StringVar()


Label(gui,text='Paste the directory address',font=('algerian',20),bg='black',fg='blue').place(x=20,y=100)

path_entry=Entry(gui,textvariable=leo,font=('Bookman Old Style',21),fg='red',width=38)
path_entry.focus()
path_entry.place(x=20,y=150)

path_button=Button(gui,text="Optimize",font=('Algerian',15),fg='blue',width=10,height=2,command=mainprog)
path_button.place(x=260,y=220)

path_label_green=Label(gui,text="",textvariable=Gtext,font=('courier',18,'bold'),bg='black',fg='Yellow').place(x=200,y=320)

### Identity Leo7
Label(gui,text="@Leo7",font=("Jokerman",20),fg="White",bg="Black").place(x=550,y=430)

gui.mainloop()
