import tkinter as tk


root = tk.Tk()
root.title("Log In")

root.geometry("300x200")

login = tk.Label(root, text="Username: ")
login.pack()

userentry = tk.Entry(root, width=20)
userentry.pack()

login2 = tk.Label(root, text="Password: ")
login2.pack()

passwordentry = tk.Entry(root, show="*", width=20)
passwordentry.pack()

def button_click():
    user = userentry.get()
    password = passwordentry.get()
    if user == "admin":
        if password == "admin":
            print(f"Logged in! User: {user}")
            root.destroy()
            loggedin = tk.Tk()
            loggedin.title("Logged In!")
            loggedin.geometry("500x350")
            logged = tk.Label(loggedin, text=f"Logged in successfully! User: {user}")
            logged.pack()
        else:
            print("Wrong password!")
            wrongpassword = tk.Tk()
            wrongpassword.title("Wrong username!")
            wrongpassword.geometry("150x40")
            wrongpass = tk.Label(wrongpassword, text="Wrong password!")
            wrongpass.pack()
    else:
        wrongusername = tk.Tk()
        wrongusername.title("Wrong username!")
        wrongusername.geometry("150x40")
        wronguser = tk.Label(wrongusername, text="Wrong username!")
        wronguser.pack()
        print("Wrong username!")


loginbutton = tk.Button(root, text="Log in", command=button_click)
loginbutton.pack()

root.mainloop()
