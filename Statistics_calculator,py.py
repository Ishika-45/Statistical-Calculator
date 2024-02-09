from tkinter import *
import tkinter as tk 
import statistics as st
from tkinter.messagebox import askyesno

root=tk.Tk()
root.title("Project:1")
root.minsize(500,500)
root.maxsize(1920,1080)
root.iconbitmap("python.ico")
root.configure(bg="black")

title_label = tk.Label(root,text = 'Title: Measure of Central Tendancy and Dispersion', font=('Algerian',16),bg="black",foreground="white").pack()
author_label = tk.Label(root,text = 'Author Details: Ishika Bansal',font= ('Arial',14,"bold italic"),bg="black",foreground="white").pack()

number_label =tk.Label(root,text = 'Enter List of Numbers: ',font=('Arial',10),bg="black",foreground="white" ).place(x=10, y=75)
b_l1=StringVar()
e1=Entry(root,textvariable=b_l1,justify=LEFT).place(x=180,y=75)
lbl=tk.Label(root,text='Output',font = ('Arial',10),bg = 'black',foreground='white').place(x=10,y=100)
lb2=tk.Label(root,text="Output is here!!",bg="white",width=50)
lb2.pack(padx=100,pady=50)
ctLabel = tk.Label(root,text = 'Measure of Central Tendancy',font=('Arial',12),bg="black",foreground="white" ).place(x=10, y=150)

r1_ct = tk.Radiobutton(root,text = "Arithmetic Mean",command=lambda:mean(),bg="black",foreground="white").place(x=10, y=170)
r2_ct = tk.Radiobutton(root,text = "Harmonic Mean", command=lambda:harmonicmean(),bg="black",foreground="white").place(x=10, y=190)
r3_ct = tk.Radiobutton(root,text = "Geometric Mean", command=lambda:geometricmean(),bg="black",foreground="white").place(x=10, y=210)
r4_ct = tk.Radiobutton(root,text = "Mode", command=lambda:mode(),bg="black",foreground="white").place(x=10, y=230)
r5_ct = tk.Radiobutton(root,text = "Median", command=lambda:median(),bg="black",foreground="white").place(x=10, y=250)

dispLabel = tk.Label(root,text = 'Measure of Dispersion',font=('Arial',12),bg="black",foreground="white" ).place(x=10, y=280)

b1=tk.Radiobutton(root,text="Range",command=lambda:rang(),bg="black",foreground="white").place(x=10,y=300)
b2=tk.Radiobutton(root,text="Variance",command=lambda:variance(),bg="black",foreground="white").place(x=10,y=320)
b3=tk.Radiobutton(root,text="Standard Deviation",command=lambda:sd(),bg="black",foreground="white").place(x=10,y=340)

def mean():
    l1=list(map(int,b_l1.get().split(",")))
    st1="Mean is: "+str(st.mean(l1))
    print(st1)
    lb2.config(text=st1)

def median():
    l1=list(map(int,b_l1.get().split(",")))
    st1="Median is: "+str(st.median(l1))
    print(st1)
    lb2.config(text=st1)

def mode():
    l1=list(map(int,b_l1.get().split(",")))
    st1="Mode is: "+str(st.mode(l1))
    print(st1)
    lb2.config(text=st1)
    
def geometricmean():
    l1=list(map(int,b_l1.get().split(",")))
    st1="Geometric Mean is: "+str(st.geometric_mean(l1))
    print(st1)
    lb2.config(text=st1)

def harmonicmean():
    l1=list(map(int,b_l1.get().split(",")))
    st1="Harmonic Mean is: "+str(st.harmonic_mean(l1))
    print(st1)
    lb2.config(text=st1)

def rang():
    l1=list(map(int,b_l1.get().split(",")))
    a=int(max(l1))
    b=int(min(l1))
    st1="Range is: "+str(a-b)
    lb2.config(text=st1)

def variance():
     l1=list(map(int,b_l1.get().split(",")))
     st1="Variance is: "+str(st.variance(l1))
     lb2.config(text=st1)

def sd():
     l1=list(map(int,b_l1.get().split(",")))
     st1="Standard Deviation is: "+str(st.stdev(l1))
     lb2.config(text=st1)  

def confirn():
    ans = askyesno(title='Confirmation',message='Do you Want to Exit ? ')
    if ans:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", confirn)

quitButton = Button(text = 'EXIT', command=confirn,bg="black",foreground="white").pack(padx=5, pady=20, side=tk.BOTTOM)     

root.mainloop()
        

         