from tkinter import *
import csv

def res_fun(value,w):
    
    if value == 2:

        name_label = Label(w,text = 'Enter your name ===>').grid(row = 3, column = 0, padx = 10, pady = 10)
        global name_ent
        name_ent = Entry(w)
        age_label = Label(w,text = 'Enter your age ===>').grid(row = 4, column = 0, padx = 10, pady = 10)
        global age_ent
        age_ent = Entry(w)
        phone_label = Label(w,text = 'Enter your phone number ===>').grid(row = 5, column = 0, padx = 10, pady = 10)
        global phone_ent
        phone_ent = Entry(w)
        submit_btn = Button(w,text = 'Submit',width = 20,height = 3,command = get_2).grid(row = 6, column = 0, padx = 10, pady = 10)
        
        name_ent.grid(row = 3, column = 1, padx = 10, pady = 10)
        age_ent.grid(row = 4, column = 1, padx = 10, pady = 10)
        phone_ent.grid(row = 5, column = 1, padx = 10, pady = 10)





    if value == 1:
             try:
                 with open('test.csv','a') as csvfile:
                     pass
                 with open('test.csv','r') as csvfile:
                     count = 2
                     csvreader = csv.reader(csvfile)
                     fields = next(csvreader)
                     for row in csvreader:
                         count = count+1
                         read_lbl = Label(w,text = row).grid(row = count,column = 0, padx = 10, pady = 10)

                         
             except StopIteration:
                 pass


def get_2():
        fields = ['name','age','phone number']
        
        
        with open('test.csv','a') as csvfile:
            csvwriter = csv.writer(csvfile)
            
            csvwriter.writerow(fields)
            rows = [name_ent.get(),age_ent.get(),phone_ent.get()]
            csvwriter.writerow(rows)        

            
