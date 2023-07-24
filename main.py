from tkinter import *

window = Tk()
window.title("SmartConverter")

Units = ['mm' , 'cm' , 'm']
menu = StringVar()
menu.set("mm")

dropmenu1 = OptionMenu(window , menu , *Units)
dropmenu1.grid(row=1 , column=1)

menu2 = StringVar()
menu2.set("mm")

dropmenu2 = OptionMenu(window , menu , *Units)
dropmenu2.grid(row=1 , column=2)

input = Entry(window)
input.grid(row=2, column=1)

output = Label(window,borderwidth=5 , relief="solid")
output.grid(row=2, column=2)
window.mainloop()
