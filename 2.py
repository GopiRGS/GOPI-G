import tkinter as tk
from tkinter import messagebox

def show_login():
    intro_frame.pack_forget()
    login_frame.pack(expand=True, fill='both')

root = tk.Tk()
root.geometry("1080x800")
root.title("Login System")
root.config(bg="#2c3e50")


intro_frame = tk.Frame(root, bg="#2c3e50")
intro_label = tk.Label(intro_frame, text="Welcome Login", font=("Helvetica", 30), fg="white", bg="#2c3e50")
intro_label.pack(pady=20)
intro_button = tk.Button(intro_frame, text="Go to Login", command=show_login, font=("Helvetica", 20), bg="#3498db", fg="white", padx=11, pady=5)
intro_button.place(relx=0.88, rely=0.89, anchor='se') 
intro_frame.pack(expand=True, fill='both')

login_frame = tk.Frame(root, bg="#2c3e50")
login_label = tk.Label(login_frame, text="Login Page", font=("Helvetica", 30), fg="white", bg="#2c3e50")
login_label.pack(pady=20)
label_username = tk.Label(login_frame, text="Username", font=("Helvetica", 12), fg="white", bg="#2c3e50")
label_username.place(relx=0.75, rely=0.7, anchor='e')  
entry_username = tk.Entry(login_frame, font=("Helvetica", 12))
entry_username.place(relx=0.75, rely=0.75, anchor='e')  
label_password = tk.Label(login_frame, text="Password", font=("Helvetica", 12), fg="white", bg="#2c3e50")
label_password.place(relx=0.75, rely=0.8, anchor='e')  
entry_password = tk.Entry(login_frame, show="*", font=("Helvetica", 12))
entry_password.place(relx=0.75, rely=0.85, anchor='e')
login_button = tk.Button(login_frame, text="Login", font=("Helvetica", 12), bg="#3498db", fg="white", padx=10, pady=5)
login_button.place(relx=0.75, rely=0.9, anchor='e')  
new = tk.Label(login_frame, text="Don't have an account?", font=("Helvetica", 12), bg="#2c3e50", fg="white")
new.place(relx=0.68, rely=0.97, anchor='e')  
account_button = tk.Button(login_frame, text="Signup", font=("Helvetica", 12), bg="#3498db", fg="white", padx=10, pady=5)
account_button.place(relx=0.75, rely=1.0, anchor='se')

root.mainloop()
