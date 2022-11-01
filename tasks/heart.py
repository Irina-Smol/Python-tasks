from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from random import randint

win = Tk()
win.title('calculate')

def calculation():
    number = randint(60, 100)
    showinfo('the percent of love', f'this is love on {number} %')

open_img = Image.open('bear.jpg')
render_img = ImageTk.PhotoImage(open_img)
main_image = Label(win, image=render_img)
main_image.image = render_img
main_image.grid(row=0, columnspan=2)

label1 = Label(win, text='put your name: ', font=('arial', 10, 'bold'))
label1.grid(row=1, column=0, sticky='w')

entry1 = Entry(win, font=('arial', 10, 'bold'))
entry1.grid(row=1, column=1)

label2 = Label(win, text='put partner name: ', font=('arial', 10, 'bold'))
label2.grid(row=2, column=0)

entry2 = Entry(win, font=('arial', 10, 'bold'))
entry2.grid(row=2, column=1)

button = Button(win, text='check', bd=2, font=('arial', 10, 'bold'), fg='red', bg='black', command=calculation)
button.grid(row=3, columnspan=2)

win.mainloop()
