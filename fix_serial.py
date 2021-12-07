#! python3
import re
from tkinter import *
from tkinter import filedialog

file = ''
example_string = ''
def file_to_fix():
    global file
    file = filedialog.askopenfilename() 
    lbl_done.configure(text="got file")
    return file
def example_serial():
    global example_string
    example_string = example_txt.get()
    lbl_done.configure(text="got example")
    return example_string
def close():
    window.destroy()
    window.quit()

def run(file,example_string):
    pattern = []
    # "/Users/a1/Desktop/Programming/fix_serial/12345.txt"
    with open(file,'r') as reader:
        list1 = reader.readlines()
    for i in range(len(list1)-1):
        list1[i] = list1[i][:-1]
    test = list1
    done = ''
    example = ''
    ind = []
    flag = False
    for i in range(len(example_string)):
        if example_string[i].isdigit():
            example += '0'
        elif example_string[i].isalpha():
            example += '1'
        else:
            example += '2'
    for i in range(len(test)):
        pattern.append('')
        for j in range(len(test[i])):
            if test[i][j].isdigit():
                pattern[i] += '0'
            elif test[i][j].isalpha():
                pattern[i] += '1'
            else:
                pattern[i] += '2'
        if not ind:
            match = re.search(example,pattern[0])
            try:
                ind = list(match.span())
            except:
                flag = True
            try:
                if pattern[i][ind[0]-1] == pattern[i][ind[0]] or pattern[i][ind[1]] == pattern[i][ind[1]-1]:
                    pattern[i] = pattern[i].replace("0", "2",ind[0])
            except:
                pass
            match = re.search(example,pattern[0])
            try:
                ind = list(match.span())
            except:
                flag = True

    if flag == False:
        for i in range(len(test)):
            test[i] = test[i][ind[0]:ind[1]]
        for elt in test:
            for i in range (len(elt)):
                done += elt[i]
            done+='\n'
        
        with open("/Users/a1/Desktop/Programming/fix_serial/done.txt","w+") as writer:
            writer.writelines(done)
        lbl_done.configure(text="done")
    else:
        lbl_done.configure(text="error")
    
window = Tk()
window.title("fix qr-code")
window.geometry('500x200')
lbl = Label(window, text="Choose '.txt' file to fix: ",font = ("Arial Bold", 20),padx=20, pady=20)  
lbl.grid(column=0, row=0)  
file_to_fix_btn = Button(window, text="Choose File",command= file_to_fix)
file_to_fix_btn.grid(column=1, row=0)
lbl = Label(window, text="Serial number example: ",font = ("Arial Bold", 20),padx=20, pady=20)  
lbl.grid(column=0, row=1)  
example_btn = Button(window, text="Apply",command= example_serial)
example_btn.grid(column=2, row=1)
example_txt = Entry(window,width=10)  
example_txt.grid(column=1, row=1)  
run_btn = Button(window, text="Run",command=lambda: run(file,example_string))
run_btn.grid(column=1, row=2)
lbl_done = Label(window, text="",font = ("Arial", 14),padx=5, pady=5)  
lbl_done.grid(column=2, row=2) 
close_btn = Button(window, text="Exit",command= close)
close_btn.grid(column=0, row=2)
window.mainloop()





        

