from tkinter import *
import math

def click(value):
    ex=entryField.get()
    answer=''

    try:

        if value=='C':
            ex=ex[0:len(ex)-1]
            entryField.delete(0,END)
            entryField.insert(0,ex)
            return

        elif value=='CE':
            entryField.delete(0,END)

        elif value=='√':
            answer=math.sqrt(eval(ex))

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value== chr(247): #7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer=eval(ex)

        else:
            entryField.insert(END,value)
            return


        entryField.delete(0,END)
        entryField.insert(0,answer) 

    except SyntaxError:
        pass

root=Tk()
root.title('Calculator')
root.config(bg='white')
root.geometry('590x300+100+100')


entryField=Entry(root,font=('arial',20,'bold'),bg='silver',fg='black',bd=10,relief=SUNKEN,width=20)
entryField.grid(row=0,column=0,columnspan=8)


button_text_list = ["C", "CE", "√", "+",
                    "1", "2", "3", "-", 
                    "*", "x\u00B3", "x\u00B2", "4", "5", "6",
                    "=", ".", chr(247), "0", "7", "8","9"]
rowvalue=1
columnvalue=0
for i in button_text_list:

    button=Button(root,width=5,height=2,bd=2,relief=SUNKEN,text=i,bg='dimgrey',fg='black',
              font=('arial',18,'bold'),activebackground='silver',command=lambda button=i: click(button))
    button.grid(row=rowvalue,column=columnvalue,pady=1)
    columnvalue+=1
    if columnvalue>6:
        rowvalue+=1
        columnvalue=0


root.mainloop()