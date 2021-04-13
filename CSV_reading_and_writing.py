import csv
from tkinter import *
import CSVFunModule as cfm

window = Tk()

window.title('Csv file reading and writing')
window.iconbitmap('paper.ico')

r = IntVar()

Radiobutton(window,text = 'Read',variable = r,value = 1).grid(row = 0, column = 0, padx = 10, pady = 10)
Radiobutton(window,text = 'Write',variable = r,value = 2).grid(row = 1, column = 0, padx = 10, pady = 10)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = lambda: cfm.res_fun(r.get(),window)).grid(row = 2, column = 0, padx = 10, pady = 10)

window.mainloop()