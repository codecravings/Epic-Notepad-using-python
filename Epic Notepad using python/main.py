import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from pygame import mixer

root = tk.Tk()
root.geometry("1200x600")
root.title("Your own notepad")

mixer.init()

##########################################--Menubar--################################
# menubar
menubar = tk.Menu(root)

# file icons
new_icon = tk.PhotoImage(file="icons/new.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save.png")
saveAs_icon = tk.PhotoImage(file="icons/save_as.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

# file
file = tk.Menu(menubar, tearoff=0)

# edit icons
copy_icon = tk.PhotoImage(file="icons/copy.png")
paste_icon = tk.PhotoImage(file="icons/paste.png")
cut_icon = tk.PhotoImage(file="icons/cut.png")
clearAll_icon = tk.PhotoImage(file="icons/clear_all.png")
find_icon = tk.PhotoImage(file="icons/find.png")

# edit
edit = tk.Menu(menubar, tearoff=0)

# view icons
toolbar_icon = tk.PhotoImage(file="icons/tool_bar.png")
statusbar_icon = tk.PhotoImage(file="icons/status_bar.png")

# view
view = tk.Menu(menubar, tearoff=0)

# color theme icon
Light_Default_icon = tk.PhotoImage(file="icons/light_default.png")
Light_Plus_icon = tk.PhotoImage(file="icons/light_plus.png")
Dark_icon = tk.PhotoImage(file="icons/dark.png")
Monokai_icon = tk.PhotoImage(file="icons/monokai.png")
Night_Blue_icon = tk.PhotoImage(file="icons/night_blue.png")
Red_icon = tk.PhotoImage(file="icons/red.png")

# color theme
color_theme = tk.Menu(menubar, tearoff=0)
colorvar = tk.StringVar()
color_dict = {
    "Light Default": ('#000000', '#ffffff'),
    "Light Plus": ('#474747', '#e0e0e0'),
    "Dark": ('#ffffff', '#2d2d2d'),
    "Monokai": ('#d3b774', '#474747'),
    "Red": ('#2d2d2d', '#ffe8e8'),
    "Night Blue": ('#ededed', '#6b9dc2')
}

color_icon_list = [Light_Default_icon, Light_Plus_icon, Dark_icon, Monokai_icon, Red_icon, Night_Blue_icon]

# music
music = tk.Menu(menubar, tearoff=0)


# music play function
def play_music(event=None):
    mixer.music.load("Subconscious_Mind_Programming_Binaural_Beats.mp3")
    mixer.music.play()


music.add_command(label="Play Music", compound=tk.LEFT, accelerator="Ctrl+P", command=play_music)


# music stop functionality
def stop_music(event=None):
    mixer.music.stop()


music.add_command(label="Stop", compound=tk.LEFT, accelerator="Ctrl+W", command=stop_music)

# cascade
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="View", menu=view)
menubar.add_cascade(label="Color_theme", menu=color_theme)
menubar.add_cascade(label="Music", menu=music)

##########################################---Menubar End---##############################

##########################################----Toolbar---#################################

toolbar = ttk.Label(root)
toolbar.pack(side=tk.TOP, fill=tk.X)

# font family
fonts = tk.font.families()
font_family = tk.StringVar()
fontbox = ttk.Combobox(toolbar, width=30, textvariable=font_family, state="readonly")
fontbox['values'] = fonts
fontbox.current(fonts.index("Arial"))
fontbox.grid(row=0, column=0, padx=5)

# font size
font_size = tk.IntVar()
fontsizebox = ttk.Combobox(toolbar, width=14, textvariable=font_size, state="readonly")
fontsizebox['values'] = tuple(range(8, 100, 2))
fontsizebox.current(4)
fontsizebox.grid(row=0, column=1, padx=5)

# bold
bold_icon = tk.PhotoImage(file="icons/bold.png")
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# italic
italic_icon = tk.PhotoImage(file="icons/italic.png")
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# underline
underline_icon = tk.PhotoImage(file="icons/underline.png")
underline_btn = ttk.Button(toolbar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# font color
font_color_icon = tk.PhotoImage(file="icons/font_color.png")
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# left align
align_left_icon = tk.PhotoImage(file="icons/align_left.png")
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

# center align
align_center_icon = tk.PhotoImage(file="icons/align_center.png")
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

# right align
align_right_icon = tk.PhotoImage(file="icons/align_right.png")
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)


# set volume functionality
def set_vols(val):
    value = int(val) / 100
    mixer.music.set_volume(value)


# set volume
volume = tk.Scale(toolbar, orient=tk.HORIZONTAL, command=set_vols)
volume.set(56)
volume.grid(row=0, column=9, padx=5)

#########################################---End Toolbar---###############################


#########################################----Text Editor---##############################

text_editor = tk.Text(root)
text_editor.config(wrap="word", relief=tk.FLAT)

scrollbar = tk.Scrollbar(root)
text_editor.focus_set()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)

# change font family and font functions

current_font_family = "Arial"
current_font_size = 14


def change_font(root):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))


def change_font_size(root):
    global current_font_size
    current_font_size = fontsizebox.get()
    text_editor.configure(font=(current_font_family, current_font_size))


fontbox.bind("<<ComboboxSelected>>", change_font)

fontsizebox.bind("<<ComboboxSelected>>", change_font_size)


# bold function
def bold():
    font_property = tk.font.Font(font=text_editor['font'])
    if font_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, "bold"))
    if font_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


bold_btn.configure(command=bold)


# italic function
def italic():
    font_property = tk.font.Font(font=text_editor['font'])
    if font_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, "italic"))
    if font_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, "roman"))


italic_btn.configure(command=italic)


# underline function
def underline():
    font_property = tk.font.Font(font=text_editor['font'])
    if font_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, "underline"))
    if font_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, "normal"))


underline_btn.configure(command=underline)


# font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)


# align functionality

# left align funcitonality
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config("left", justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "left")


align_left_btn.configure(command=align_left)


# center align funcitonality
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config("center", justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "center")


align_center_btn.configure(command=align_center)


# right align funcitonality
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config("right", justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, "right")


align_right_btn.configure(command=align_right)

text_editor.configure(font=("Arial, 14"))

######################################-----Status Bar---################################

status = tk.Label(root, text="Status Bar")
status.pack(side=tk.BOTTOM, fill=tk.X)

# status bar functionality
text_changed = False


def status_changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, "end-1c").split())
        character = len(text_editor.get(1.0, "end-1c"))
        status.config(text=f"Words : {words} Character : {character}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>", status_changed)

#########################################----End Text Editor----#########################


#########################################---commands---##################################

# file commands

##variable
url = " "


# New file functionality
def new_file(event=None):
    global url
    url = " "
    text_editor.delete(1.0, tk.END)
    root.title("Your own notepad")


file.add_command(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+N", command=new_file)


# open file functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                     filetypes=(("Text File", "*.txt"), ("All File", "*.*")))
    try:
        with open(url, "r") as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())

    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))


file.add_command(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)


##save file functionality
def save_file(event=None):
    global url
    try:
        if url == " ":
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
        else:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding="utf-8") as fw:
                fw.write(content)
    except:
        return


file.add_separator()
file.add_command(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)


# save as functionality
def save_as(

         event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
        content2 = text_editor.get(1.0, tk.END)
        url.write(content2)
        url.close()
    except:
        return


file.add_command(label="Save As", image=saveAs_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)


# exit funcitonality
def exit(event=None):
    global url, text_changed
    try:
        if text_changed is True:
            mbox = messagebox.askyesnocancel("Warning", "Do you want to save the file?")
            if mbox is True:
                if url is True:
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w', encoding="utf-8") as fw:
                        fw.write(content)
                    root.destroy()

                else:
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
                    content2 = text_editor.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
                root.destroy()
        else:
            root.destroy()
    except:
        return


file.add_separator()
file.add_command(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+Q", command=exit)


# edit commands


# find functionality
def find_func(event=None):
    def find():
        word = find_entry.get()
        text_editor.tag_remove('match', 1.0, tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match", start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config("match", foreground="red", background="yellow")

    def replace():
        word = find_entry.get()
        replace_txt = replace_entry.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_txt)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry("450x250+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0, 0)

    # frame
    frame = ttk.LabelFrame(find_dialog, text="Find/Replace")
    frame.pack(pady=20)

    # labels
    find_label = ttk.Label(frame, text="Find : ")
    replace_label = ttk.Label(frame, text="Replace : ")

    # entry
    find_entry = ttk.Entry(frame, width=30)
    replace_entry = ttk.Entry(frame, width=30)

    # buttons
    find_btn = ttk.Button(frame, text="Find", command=find)
    replace_btn = ttk.Button(frame, text="Replace", command=replace)

    # labels grid
    find_label.grid(row=0, column=0, padx=4, pady=4)
    replace_label.grid(row=1, column=0, padx=4, pady=4)

    # entry grid
    find_entry.grid(row=0, column=1, padx=4, pady=4)
    replace_entry.grid(row=1, column=1, padx=4, pady=4)

    # buttons grid
    find_btn.grid(row=2, column=0, padx=8, pady=4)
    replace_btn.grid(row=2, column=1, padx=8, pady=4)

    find_entry.focus()

    find_dialog.mainloop()


edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="Ctrl+C",
                 command=lambda: text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="Ctrl+V",
                 command=lambda: text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut", image=cut_icon, compound=tk.LEFT, accelerator="Ctrl+X",
                 command=lambda: text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All", image=clearAll_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+C",
                 command=lambda: text_editor.delete(1.0, tk.END))
edit.add_command(label="Find", image=find_icon, compound=tk.LEFT, accelerator="Ctrl+F", command=find_func)

# view commands

# hide toolbar and status bar functionality
show_toolbar = tk.BooleanVar()
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status.pack_forget()
        show_statusbar = False
    else:
        status.pack(side=tk.BOTTOM)
        show = True


view.add_checkbutton(label="Tool Bar", image=toolbar_icon, onvalue=True, offvalue=False, variable=show_toolbar,
                     compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label="Status Bar", image=statusbar_icon, onvalue=True, offvalue=False, variable=show_statusbar,
                     compound=tk.LEFT, command=hide_statusbar)


# color theme commands
def change_theme():
    choosen_color = colorvar.get()
    colors = color_dict.get(choosen_color)
    foregroundcolor, bg = colors[0], colors[1]
    text_editor.config(background=bg, fg=foregroundcolor)


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icon_list[count], variable=colorvar, compound=tk.LEFT,
                                command=change_theme)
    count += 1

root.config(menu=menubar)

# shortcut keys

root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as)
root.bind("<Control-q>", exit)
root.bind("<Control-f>", find_func)
root.bind("<Control-p>", play_music)
root.bind("<Control-w>", stop_music)

root.mainloop()