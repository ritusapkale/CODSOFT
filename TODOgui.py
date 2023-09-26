from tkinter import *
from tkinter import messagebox

def add():
    tasks = task_input.get()
    if tasks == '':
        messagebox.showerror(title='Not Item Added', message='Please Add a task')
    else:
        task_list.insert(END, tasks)
        task_input.delete(0, END)
def delete():
    d = task_list.curselection()
    if not d:
        messagebox.showerror(title='No Item Selected', message='Select task to delete.')
    else:
        task_list.delete(d)

def edit():
    v = task_list.curselection()

    if not v:
        messagebox.showerror(title='No Item Selected', message='Select task to edit.')
    else:
        e = task_list.get(v)
        task_input.insert(0, string=e)
        task_input.focus()
        task_list.delete(v)

def reset():
    is_ok = messagebox.askyesno(title='Confirmation!!!!', message='Are you sure, you want to reset the list?')
    if is_ok:
        task_input.delete(0, END)
        task_list.delete(0, END)


BACKGROUND_COLOR = '#7C73C0'

window = Tk()
window.title('To Do List')
window.config(padx=100, pady=100, bg=BACKGROUND_COLOR)



heading = Label(text='To Do List', fg='black', font=('Times New Roman', 40, 'italic'), anchor=CENTER,
                bg=BACKGROUND_COLOR)
heading.grid(row=0, column=1)

add_label = Label(text='Write your Task:', font='20', bg=BACKGROUND_COLOR)
add_label.grid(row=2, column=0, padx=10, pady=10)

tasks_label = Label(text='Tasks :', font='20', bg=BACKGROUND_COLOR)
tasks_label.grid(row=3, column=0, padx=10, pady=10)


task_input = Entry(width=40)
task_input.grid(row=2, column=1)
task_input.focus()

task_list = Listbox()
task_list.grid(row=3, column=1)


add_button = Button(text='ADD', fg='#2841e0', width=15, command=add)
add_button.grid(row=2, column=2, padx=10, pady=10)

del_button = Button(text='DELETE', fg='#2841e0', width=15, command=delete)
del_button.grid(row=4, column=0, padx=10, pady=10)

edit_button = Button(text='Update', fg='#2841e0', width=15, command=edit)
edit_button.grid(row=4, column=1, padx=15, pady=15)

reset_button = Button(text='Delete All Tasks', fg='#2841e0', width=15, command=reset)
reset_button.grid(row=4, column=2, padx=15, pady=15)

window.mainloop()