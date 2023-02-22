from tkinter import *
from tkinter import messagebox
def encode():
    Cu=current.get()
    Ne=need.get()
    if len(Cu)!=len(Ne) or len(Cu)!=len(set(Cu)) or len(set(Ne))!=len(Ne):
        messagebox.showerror('Ошибка','Количество символов должно быть равным и они не должны повторяться')
    else:
        d=dict()
        for j in range(len(Cu)):
            d[Cu[j]]=Ne[j]
        l=0
        t=[list(i) for i in text.get('1.0','end').split('\n')]
        for line in t:
            l+=1
            for letter in line:
                if letter in Cu:
                    i=t[l-1].index(letter)
                    text.replace(f'{l}.{i}',f'{l}.{i+1}',d[letter])
                    t[l-1][i]=d[letter]
def decode():
    Cu=need.get()
    Ne=current.get()
    if len(Cu)!=len(Ne) or len(Cu)!=len(set(Cu)) or len(set(Ne))!=len(Ne):
        messagebox.showerror('Ошибка','Количество символов должно быть равным и они не должны повторяться')
    else:
        d=dict()
        for j in range(len(Cu)):
            d[Cu[j]]=Ne[j]
        l=0
        t=[list(i) for i in text.get('1.0','end').split('\n')]
        for line in t:
            l+=1
            for letter in line:
                if letter in Cu:
                    i=t[l-1].index(letter)
                    text.replace(f'{l}.{i}',f'{l}.{i+1}',d[letter])
                    t[l-1][i]=d[letter]
root=Tk()
text=Text(wrap=WORD,font=15)
text.pack()
current=Entry(font=20)
current.pack(side=LEFT)
need=Entry(font=20)
need.pack(side=LEFT)
button1=Button(text='Расшифровать',command=decode,font=20,activebackground='gray50').pack(side=RIGHT)
button2=Button(text='Зашифровать',command=encode,font=20,activebackground='gray50').pack(side=RIGHT)
root.mainloop()
