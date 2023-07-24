from tkinter import *

window = Tk()
window.geometry("400x100")
window.title("Shivani's SmartConverter")
window['bg'] = 'pink'


Units = [ 'mm' , 'cm' , 'm' , 'km' ]
menu = StringVar()
menu.set("mm")

dropmenu1 = OptionMenu(window , menu , *Units)
dropmenu1.grid(row=1 , column=1)

menu2 = StringVar()
menu2.set("mm")

dropmenu2 = OptionMenu(window , menu2 , *Units)
dropmenu2.grid(row=1 , column=2)

input = Entry(window,font=(20))
input.grid(row=2, column=1)

output = Label(window,width = 20,borderwidth=2 , relief="solid")
output.grid(row=2, column=2)

def Clear():
  input.delete(0,"end")
  output.config(text = "")

def Convert():
  unit1 = menu.get()
  unit2 = menu2.get()

  try:
      num = int(input.get())
      coverted_num = num
      if unit1 == 'mm' and unit2 == 'cm':
          converted_num = num/10

      elif unit1 == 'mm' and unit2 == 'm':
            converted_num = num/1000

      elif unit1 == 'mm' and unit2 == 'km':
            converted_num = num/1000000
     
      elif unit1 == 'cm' and unit2 == 'mm':
            converted_num = num*10

      elif unit1 == 'cm' and unit2 == 'm':
            converted_num = num/100
      
      elif unit1 == 'cm' and unit2 == 'km':
            converted_num = num*0.00001
      
      elif unit1 == 'm' and unit2 == 'mm':
            converted_num = num*1000

      elif unit1 == 'm' and unit2 == 'cm':
            converted_num = num*100
    
      elif unit1 == 'm' and unit2 == 'km':
            converted_num = num/1000
    

      output.config(text=str(converted_num))
  except:
      output.config(text="Invalid Input")
  
b_convert = Button(window , text = "Convert" , command=Convert)
b_convert.grid(row=3 , column=1)

b_clear = Button(window, text= "Clear", command=Clear)
b_clear.grid(row=3,column=2)

window.mainloop()
