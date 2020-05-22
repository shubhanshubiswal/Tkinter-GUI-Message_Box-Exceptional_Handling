
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
from csv import DictWriter
import os
win = tk.Tk() 
win.title('Message Box and Exceptional Handling')

#label frame
label_frame = ttk.LabelFrame(win, text = 'Contact Detail')
label_frame.grid(row=0, column = 0, padx=40, pady=10)

#labels
name_label = ttk.Label(label_frame, text = 'Enter your Name please : ', font=('Helvetica', 14))
age_label = ttk.Label(label_frame, text = 'Enter your age please : ', font=('Helvetica', 14,))

# entry box variables 
name_var = tk.StringVar()
age_var = tk.StringVar()

# entry boxes 
name_entry = ttk.Entry(label_frame, width=36, textvariable = name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable = age_var)

#grid
name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_label.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entry.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

def submit():
    # m_box.showwarning('title', 'content of this message box !! ')
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error', 'Please fill both name and age ')
    else:
        try:
            # age = 'fjasdofj' # value error
            # age = '20'
            age = int(age)
        except ValueError:
            m_box.showerror('title','Only digits are allowed in age field')
        else:
            if age < 18:
                m_box.showwarning('warning', 'you are not 18 , visit this content on your own risk')
            
            #write to csv file
            with open('Tkinter_Project7.csv','a',newline='')as f:
                dict_writer=DictWriter(f,fieldnames=['UserName','UserAge'])  

                if os.stat('Tkinter_Project7.csv').st_size==0:
                    dict_writer.writeheader()
                dict_writer.writerow({
                    'UserName':name,
                    'UserAge':age
         
                     })  

    #If after Submitting Values you want to clear the entry boxes     
    name_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)           
   
    

submit_btn = ttk.Button(win, text = 'Submit', command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)
win.mainloop()