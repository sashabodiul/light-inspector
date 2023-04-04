import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
import asyncio
from async_tkinter_loop import async_handler, async_mainloop

# initialize theme for tkinter
root = ThemedTk(theme='blue')
#title
root.title('Light Inspector')

# height and width of the window
h = 640
w = 480
root.geometry(f"{h}x{w}")
root.resizable(False, False)
# background image
image = Image.open("qq.png")
image = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image = image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = image

#not work hour list
yellow_list = [0, 1, 2, 3, 4, 5, 6]
# blind list color list in not work hours
color = ['white','yellow']
# standart work hours dict
standart_color = {
    'red':'green',
    'yellow':'yellow',
    'green':'red'
}

#decorator for async work
@async_handler
async def submit():
    yellow = False
    # get text from input
    time_enter = txt.get()
    if int(time_enter) in yellow_list:
        yellow = True
        while yellow == True:
            for i in color:
                #set blind color yellow <--> white
                road_main.config(background=f'{i}')
                road_secondary.config(background=f'{i}')
                # work in real time with interval 0.5 sec
                await asyncio.sleep(0.5)
    else:
        yellow = False
        standart = True
        while standart == True:
        #check elements in dictionary
            for key,value in standart_color.items():
                if key == 'red' or key == 'green':
                    t = 15
                else:
                    t = 3
                    #set blind normal work time
                road_main.config(background=f'{key}')
                road_secondary.config(background=f'{value}')
                await asyncio.sleep(t)


# Creating a themet label with main text company
header = ttk.Label(root,text='L- I-', font='Ubuntu 40')
header.pack(side='top',anchor='center',pady=[20,40])

# Creating a themed textinput
txt = ttk.Entry(font='Ubuntu 16')
txt.pack(side='top',anchor='center',pady=[0,0])

# Creating a themed button submit
btn_sub = ttk.Button(root,command=submit, text="Submit", cursor='hand2')
btn_sub.pack(side='top',anchor='center',pady=[10,0])

# Creating a themed button
button = ttk.Button(root, text="Quit", command=root.destroy, cursor='hand2')
button.pack(side='bottom',anchor='ne', padx=20,pady=20)

# Creating a themed label
road_secondary = ttk.Label(background='white', border=5)
road_secondary.place(height=150, width=20, x=w//2+100, y=h//2)
road_main = ttk.Label(width=40, background='white', border=5)
road_main.pack(side='bottom')

#run processing(program) in real time
async_mainloop(root)