import tkinter as t
f=t.Tk()
# f.minsize(500,400)
f.geometry('600x410')
f.maxsize(900,500)
f.title('Word Counter')
def show(a):
    b=ta.get(1.0,'end-1c')
    if a==1:
        b=b.strip()
        # print(b.count(' ')+1)
        r.config(text='Word: '+str(b.count(' ')+1),fg='dark blue')
    elif a==2:
        r.config(text='Character: '+str(len(b)),fg='black')
        # print(len(b))    
    else:
        r.config(text='Sentence: '+str(b.count('.')),fg='dark red')

    # print('hello',a)
ta=t.Text(f,width=39,height=8,bg='#d1e3eb',font=('bold',18))
ta.place(x=40,y=20)
b1=t.Button(f,text='Count Word',bg='dark blue',fg='white',font=('bold'),command=lambda:show(1))
b1.place(x=40,y=280)
b2=t.Button(f,text='Count charcter',bg='black',fg='white',font=('bold',12),command=lambda:show(2))
b2.place(x=240,y=280)
b3=t.Button(f,text='Count Sentence',bg='dark red',fg='white',font=('bold'),command=lambda:show(3))
b3.place(x=426,y=280)
res=t.Label(f,text='Result :',height=-2,width=6,font=('bold',20))
res.place(x=37,y=340)
r=t.Label(f,font=('bold',16))
r.place(x=165,y=344)
f.mainloop()

