from tkinter import *

window=Tk()
window.title("km to mile converter")
window.minsize(width=400,height=400)

# lable_1=Label(text='Kilometers to mile converter' ,font=('Arial', 24, 'bold'))
# lable_1.grid(column=1,row=1)

miles=Label(text='Enter your miles=',font=('Arial', 15, 'bold'))
miles.grid(column=0,row=0)

lable_2=Label(text='kilometers=',font=('Arial', 15, 'bold'))
lable_2.grid(column=0,row=1)

lable_3=Label(text='your answer will be',font=('Arial', 15, 'bold'))
lable_3.grid(column=1,row=1)
# lable_3.pack()

input = Entry(width=20)
input.grid(column=1,row=0)

def converting():
    result=int(input.get())*1.6
    lable_3['text']=result




button = Button(text='convert', command=converting,font=('Arial', 10, 'bold'))
button.grid(column=1,row=3)


    
# input.pack()
window.mainloop()
