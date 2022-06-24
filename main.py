from tkinter import *
import tkinter as tk
from tkinter import ttk
#from chempy import *
from cProfile import label
from element import *
import element
import sys
import os
from genericpath import exists
from os import system
from tkinter import messagebox

myObject = element.PeriodicalSystem

# root window
root = tk.Tk()
root.title('ქიმია')
if sys.platform.startswith('win'):
    root.iconbitmap('bio.ico')
else:
    logo = PhotoImage(file='bio.gif')
    root.tk.call('wm', 'iconphoto', root._w, logo)
root.geometry('600x500') 
root.resizable(False, False)

# create a notebook
notebook = ttk.Notebook(root, width=600, height=500)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = Frame(root, width=600, height=500, bg='#0c456b') #notebook if i want 2 tab
frame1.pack(padx=0, pady=200)
#frame2 = Frame(notebook, width=600, height=500, bg='#0c456b')
#frame2.pack(padx=0, pady=200)

frame1.pack(fill='both', expand=True)
#frame2.pack(fill='both', expand=True)

# add frames to notebook

#frame1

notebook.add(frame1, text='ელემენტი')


# Group Box
groupbox1 = ttk.LabelFrame(frame1, text='ელემენტის საძიებო სისტემა', width=360, height = 60)
groupbox1.grid(row=0, column=1, sticky='NW', padx=10, pady=10, ipadx=10, ipady=5)

groupbox2 = ttk.LabelFrame(frame1, text='რეზულტატი', width=200, height=160)
groupbox2.grid(row=1, column=1, sticky='NW', padx=10, pady=10, ipadx=5, ipady=5)


#Input-Output 
element_input_label = Label(groupbox1, text='სახელი:')
element_input_label.place(x = 10, y = 10)

element_input = Entry(groupbox1,font=('acadnusx', 12))
element_input.place(x = 80, y =10)

elemName = Label(groupbox2, text=f'სახელი: ')
elemName.place(x = 10, y = 10)


elemSymbol = Label(groupbox2, text=f'სიმბოლო: ')
elemSymbol.place(x = 10, y = 35)

elemRow = Label(groupbox2, text=f'რიგი: ')
elemRow.place(x = 10, y = 60)

elemPeriod = Label(groupbox2, text=f'პერიოდი: ')
elemPeriod.place(x = 10, y = 85)

elemRowNum = Label(groupbox2, text=f'რიგის ნომერი: ')
elemRowNum.place(x = 10, y = 110)


# Functions

def displayLabel(elemArr):
    elemName.configure(text=f'სახელი: {elemArr[0]}')
    elemSymbol.configure(text=f'სიმბოლო: {elemArr[1]}')
    elemRow.configure(text=f'რიგი: {elemArr[2]}')
    elemPeriod.configure(text=f'პერიოდი: {elemArr[3]}')
    elemRowNum.configure(text=f'რიგის ნომერი: {elemArr[4]}')

def filterElemet():
    for i in myObject:
        if element_input.get() == myObject[i]['input'] or element_input.get().upper() == myObject[i]['სიმბოლო'].upper():
            currentElement = [myObject[i]['სახელი'], myObject[i]['სიმბოლო'], myObject[i]['რიგი'], myObject[i]['პერიოდი'],
            myObject[i]['რიგის ნომერი']]
            displayLabel(currentElement)

root.bind('<Enter>', filterElemet)
#button    
Mybutton = Button(frame1, text='ძებნა', command = filterElemet, ) 
Mybutton.place(x=277, y=30)





################################################################
#frame2
#notebook.add(frame2, text='Tab',)

# Group Box
#groupbox3 = ttk.LabelFrame(frame2, text='TEST', width=300, height = 60)
#groupbox3.grid(row=2, column=3, sticky='WN', padx=5, pady=5, ipadx=5, ipady=5)

thisPath = os.path.dirname(os.path.realpath(__file__))
fe = os.environ['WINDIR'] + '\\Fonts\\acadnusx.ttf'
file_exist = exists(fe)

if file_exist != 1:
    messagebox.showinfo(
        'შეტყობინება', 'თქვენს მოწყობილობაში ვერ მოიძებნა პროგრამისთვის განკუთვნილი ფონტი acadnusx, ' 
        'იმისათვის რომ პროგრამამ სრულყოფილად იმუშავოს, გთხოვთ დააინსტალიროთ install ღილაკის დაკლიკვით და '
        'შემდეგ გადატვირთოთ მოწყობილობა')

system(f'start {thisPath}\\acadnusx.ttf')


root.mainloop()