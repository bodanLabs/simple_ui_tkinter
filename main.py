import tkinter as tk
from lib.write_to_file import write

root = tk.Tk()
root.title("User-Login")
root.geometry('500x300')
root.config(background='blue')

def save_user_data():
    username=user_txt.get()
    password=pass_txt.get()
    write("data.txt",f'{username} -> {password}\n')


user_l = tk.Label(root, text="Username",font=('Arial',15),bg='blue')
user_l.pack()

user_txt = tk.Entry(root,width=30)
user_txt.pack(padx=10,pady=10)

pass_l = tk.Label(root, text="Password",font=('Arial',15),bg='blue')
pass_l.pack()

pass_txt = tk.Entry(root,width=30,show="*")
pass_txt.pack(padx=10,pady=10)


button = tk.Button(root,text="Log-in",font=('Arial',20),activebackground='red',activeforeground='white',command=save_user_data)
button.pack(pady=10)




root.mainloop()