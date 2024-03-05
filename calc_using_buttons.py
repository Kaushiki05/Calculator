import tkinter as tkr
app=tkr.Tk(__name__)
app.title('Calculator')
app.geometry('300x400')

result=tkr.Variable(app)
tkr.Label(app, textvariable = result, font=('Arial',20), bg='white').place(x=20, y=20)


def show(v):
    result.set(result.get()+v)

def evaluate():
    result.set(eval(result.get()))
    
def clear():
    result.set('')

tkr.Button(app, text='1', font=('Arial',20), command=lambda:show('1')).place(x=20, y=250)
tkr.Button(app, text='2', font=('Arial',20), command=lambda:show('2')).place(x=80, y=250)
tkr.Button(app, text='3', font=('Arial',20), command=lambda:show('3')).place(x=140, y=250)
tkr.Button(app, text='4', font=('Arial',20), command=lambda:show('4')).place(x=20, y=200)
tkr.Button(app, text='5', font=('Arial',20), command=lambda:show('5')).place(x=80, y=200)
tkr.Button(app, text='6', font=('Arial',20), command=lambda:show('6')).place(x=140, y=200)
tkr.Button(app, text='7', font=('Arial',20), command=lambda:show('7')).place(x=20, y=150)
tkr.Button(app, text='8', font=('Arial',20), command=lambda:show('8')).place(x=80, y=150)
tkr.Button(app, text='9', font=('Arial',20), command=lambda:show('9')).place(x=140, y=150)
tkr.Button(app, text='0', font=('Arial',20), command=lambda:show('0')).place(x=80, y=300)
tkr.Button(app, text='+', font=('Arial',20), command=lambda:show('+')).place(x=200, y=300)
tkr.Button(app, text='-', font=('Arial',20), command=lambda:show('-')).place(x=200, y=250)
tkr.Button(app, text='*', font=('Arial',20), command=lambda:show('*')).place(x=200, y=200)
tkr.Button(app, text='/', font=('Arial',20), command=lambda:show('/')).place(x=200, y=150)

tkr.Button(app, text='=', font=('Arial',20), command=evaluate).place(x=140, y=300)
tkr.Button(app, text='C', font=('Arial',20), command=clear).place(x=20, y=300)


app.mainloop()
