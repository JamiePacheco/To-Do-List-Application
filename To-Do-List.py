from tkinter import *
from tkinter import filedialog

#C:\\Users

root = Tk()
root.title("To Do List")
root.config(bg = "#685E69")
root.geometry("365x400")
root.resizable(FALSE,FALSE)

global filestatusname
filestatusname = False

def open_file():

    global txt_file, filestatusname
    try:
        main_listbox.delete(0,END)

        filestatusname = True

        txt_file = filedialog.askopenfilename(initialdir="C:\\Users", title = "Open File", filetypes=(("Text Files", "*.txt"),))
        text_file = open(txt_file, "r")

        text = text_file.read()
        text = text.split("\n")

        for x in text:
            if x == "":
                pass
            else:
                x = f"- {x}"
                main_listbox.insert(END, x)

        text_file.close()
    except:
        pass

def save_as_file():
    global txt_file, filestatusname
    txt_file = filedialog.asksaveasfilename(initialdir="C:\\Users", title = "Save As", filetypes=(("Text Files", "*.txt"),), defaultextension="*.")
    text_file = open(txt_file, "w")
  
    for ListboxEntry in enumerate(main_listbox.get(0, END)):
        ListboxEntry = ListboxEntry[1].replace("- ", "")
        text_file.write(f"{ListboxEntry}\n")
    
    filestatusname = True
    text_file.close()

def save_file():
    global filestatusname

    if filestatusname:
        text_file = open(txt_file, "w")
        for ListboxEntry in enumerate(main_listbox.get(0, END)):
            ListboxEntry = ListboxEntry[1].replace("- ", "")
            text_file.write(f"{ListboxEntry}\n")
        text_file.close()
    else:
        try:
            save_as_file()
        except:
            pass

def enter():
    main_listbox.insert(END, f"- {Entry_Box.get()}")
    Entry_Box.delete(0, END)

def delete_entry():
    main_listbox.delete(ANCHOR)

def delete_entries():
    main_listbox.delete(0,END)

def new_file():
    global filestatusname
    filestatusname = False
    delete_entries()

Entry_Frame = Frame(root)
Entry_Frame.pack(padx=5, pady=5)

Entry_Label = Label(Entry_Frame, text = "Enter: ", font = ("Times New Roman", 14))
Entry_Label.grid(row=1, column=1, padx=10, pady=10)

Entry_Box = Entry(Entry_Frame, font = ("Times New Roman", 14), width=24)
Entry_Box.grid(row=1, column=2, padx=5, pady=10)

Enter_button = Button(Entry_Frame, text = "Enter", command=enter)
Enter_button.grid(row=1, column=3, pady=10, padx=5)

Text_box_frame = Frame(root)
Text_box_frame.pack(padx=5, pady=5)

Listbox_Scrollbar = Scrollbar(Text_box_frame)
Listbox_Scrollbar.pack(side = RIGHT, fill = Y)

main_listbox = Listbox(Text_box_frame, bg = "white", fg = "black", width=38, height=15, selectbackground="yellow", selectforeground="black", font=("Times New Roman", 14), yscrollcommand=Listbox_Scrollbar.set)
main_listbox.pack(side=LEFT, fill=BOTH, expand=YES)
Listbox_Scrollbar.config(command = main_listbox.yview)

Top_menu = Menu(root)
root.config(menu=Top_menu)

File_handling_Menu = Menu(Top_menu, tearoff="off")
Top_menu.add_cascade(label = "File", menu = File_handling_Menu)
File_handling_Menu.add_command(label="New", command=new_file)
File_handling_Menu.add_command(label="Open", command=open_file)
File_handling_Menu.add_command(label="Save", command=save_file)
File_handling_Menu.add_command(label="Save As", command=save_as_file)

Delete_Entry_Menu = Menu(Top_menu, tearoff="off")
Top_menu.add_cascade(label = "Delete", menu = Delete_Entry_Menu)
Delete_Entry_Menu.add_command(label = "Delete Entry", command = delete_entry)
Delete_Entry_Menu.add_command(label= "Delete All", command = delete_entries)

root.mainloop()