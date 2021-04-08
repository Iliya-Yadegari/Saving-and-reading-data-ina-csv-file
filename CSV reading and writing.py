import csv
from tkinter import *

def res_fun():
    
    if r.get() == 2:

        name_label = Label(window,text = 'Enter your name ===>').grid(row = 3, column = 0, padx = 10, pady = 10)
        global name_ent
        name_ent = Entry(window)
        age_label = Label(window,text = 'Enter your age ===>').grid(row = 4, column = 0, padx = 10, pady = 10)
        global age_ent
        age_ent = Entry(window)
        phone_label = Label(window,text = 'Enter your phone number ===>').grid(row = 5, column = 0, padx = 10, pady = 10)
        global phone_ent
        phone_ent = Entry(window)
        submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = get_2).grid(row = 63, column = 0, padx = 10, pady = 10)
        
        name_ent.grid(row = 3, column = 1, padx = 10, pady = 10)
        age_ent.grid(row = 4, column = 1, padx = 10, pady = 10)
        phone_ent.grid(row = 5, column = 1, padx = 10, pady = 10)

        count = 2
        if r.get() == 1:
             try:
                 with open('test.csv','w') as csvfile:
                     pass
                 with open('test.csv','r') as csvfile:
                     csvreader = csv.reader(csvfile)
                     fields = next(csvreader)
                     for row in csvreader:
                         count = count+1
                         read_lbl = Label(window,text = row).grid(row = count,column = 0, padx = 10, pady = 10)
             except StopIteration:
                 pass

def get_2():
        fields = ['name','age','phone number']
        rows = [name_ent.get(),age_ent.get(),phone_ent.get()]
        
        with open('test.csv','a') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            csvwriter.writerow(fields)
            csvwriter.writerow(rows) 

window = Tk()

window.title('Storage')

r = IntVar()

Radiobutton(window,text = 'Read',variable = r,value = 1).grid(row = 0, column = 0, padx = 10, pady = 10)
Radiobutton(window,text = 'Write',variable = r,value = 2).grid(row = 1, column = 0, padx = 10, pady = 10)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = res_fun).grid(row = 2, column = 0, padx = 10, pady = 10)

window.mainloop()