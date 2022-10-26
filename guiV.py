import tkinter as tk
from PIL import Image,ImageTk
root =tk.Tk()
root.title('ENCRYPT/DECRYPT')
root.geometry('600x900')
root.minsize(600,600)
root.maxsize(600,900)
def clear():
    text1.delete(1.0,tk.END)
def encrypt():
    r=key.get()
    x=True
    try:
        int(r)
    except ValueError:
        x=False
    if x:
        q=int(r)
        es=text1.get(1.0,tk.END)
        rend = {'a': q + 1, 's': q + 2, 'd': q + 3, 'f': q + 4, 'g': q + 5, 'h': q + 6, 'j': q + 7, 'k': q + 8,
                'l': q + 9, 'q': q + 10, 'w': q + 11, 'e': q + 12, 'r': q + 13, 't': q + 14, 'y': q + 15, 'u': q + 16,
                'i': q + 17, 'o': q + 18, 'p': q + 19, 'z': q + 20, 'x': q + 21, 'c': q + 22, 'v': q + 23, 'b': q + 24,
                'n': q + 25, 'm': q + 26
                }
        b = es.translate(str.maketrans(rend))
        solution.config(text=b)
        root.clipboard_clear()
        root.clipboard_append(b)
        root.update()
    else:
        a="ERROR WRONG KEY(ONLY NUMERIC KEY)"
        solution.config(text=a)
def decrypt():
    z=key.get()
    y=True
    try:
        int(z)
    except ValueError:
        y=False
    if y:
        r=int(z)
        ds=text1.get(1.0,tk.END)

        rdend = {r + 1: 'a', r + 2: 's', r + 3: 'd', r + 4: 'f', r + 5: 'g', r + 6: 'h', r + 7: 'j', r + 8: 'k',
                 r + 9: 'l', r + 10: 'q', r + 11: 'w', r + 12: 'e', r + 13: 'r', r + 14: 't', r + 15: 'y', r + 16: 'u',
                 r + 17: 'i', r + 18: 'o',
                 r + 19: 'p', r + 20: 'z', r + 21: 'x', r + 22: 'c', r + 23: 'v', r + 24: 'b', r + 25: 'n', r + 26: 'm'
                 }
        qw = ds.translate(str.maketrans(rdend))
        solution.config(text=qw)
        return qw

    else:
        a = "ERROR WRONG KEY(ONLY NUMERIC KEY)"
        solution.config(text=a)
root.configure(bg='black')
logo=Image.open("logo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo,background='black')
logo_label.image=logo
logo_label.grid(column=0,row=1,columnspan=3)
line1=tk.Label(root,text="Encrypt and Decrypt your Text ",background='black',foreground='white',font='Impact',width=60)
line2=tk.Label(root,text="(note-all the text has to be in lowercase)",background='black',foreground='white',font='Impact')
line1.grid(column=0,row=2)
line2.grid(column=0,row=3,sticky=tk.N)
ch1=tk.Button(root,text="ENCRYPT",activebackground='#47CAF3',bg='#FC3EF3',fg='black',font='Quicksilver',command=encrypt)
ch1.grid(column=0,row=7,pady=10,ipadx=10,ipady=10,sticky=tk.W,padx=100)
ch2=tk.Button(root,text="DECRYPT",activebackground='#47CAF3',bg='#FC3EF3',fg='black',font='Quicksilver',command=decrypt)
ch2.grid(column=0,row=7,pady=10,ipadx=10,ipady=10,sticky=tk.E,padx=100)
clear=tk.Button(root,text="CLEAR",activebackground='white',bg='#47CAF3',fg='black',font='Quicksilver',command=clear)
clear.grid(column=0,row=5,pady=10)
text1=tk.Text(root,width=60,height=8)
text1.grid(column=0,row=4,sticky=tk.N)
keyt=tk.Label(root,text="PRIVACY KEY :",fg='RED',font='Quicksilver',bg='black')
keyt.grid(column=0,row=6,sticky=tk.W,padx=160)
key=tk.Entry(root,text='')
key.grid(column=0,row=6,sticky=tk.E,padx=160)
st=tk.Label(root,text='PROCESSED TEXT DATA ',fg='purple',bg='black',font='Quicksilver')
st.grid(column=0,row=8,sticky=tk.N,pady=20)
stt=tk.Label(root,text='ENTER THE TEXT  ',fg='purple',bg='black',font='Quicksilver')
stt.grid(column=0,row=3,sticky=tk.S,pady=25)
solution=tk.Label(root,text='',foreground='green',background='white',width=80,height=10)
eee=tk.Label(root,text='',fg='red',bg='black')
eee.grid(column=0,row=10,sticky=tk.S,rowspan=9)
copys=tk.Label(root,text="[COPIED TO CLIPBOARD]",fg='purple',bg='black',font='WALLEY,15')
copys.grid(column=0,row=10,sticky=tk.S,)

solution.grid(column=0,row=9,pady=0,sticky=tk.N)
root.mainloop()