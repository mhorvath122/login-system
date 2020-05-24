from tkinter import *
import os
import hashlib




 #Destroy Password not recognised Window
def delete():
    screen4.destroy()
 #Destroy User not found Window    
def delete1():
    screen5.destroy()
 
    
 
 # After Save popup Window
def saved():
    screen10 = Toplevel(screen)
    screen10.title("Saved")
    screen10.geometry("100x100")
    Label(screen10, text = "Saved").pack()



 # Event after pressed the button in Create Notes Window 
def save(event):
    filename = raw_filename.get()
    notes = raw_notes.get()
    
    data = open(".\\notes\\" + username1 + "-" + filename, "a")
    data.write(notes + '\n')
    data.close()
    
    saved()



 #Create Notes Window
def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    
    screen9 = Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("300x250")
    Label(screen9, text = "Please enter a filename for the note below: ").pack()
    Entry(screen9, textvariable = raw_filename).pack()
    Label(screen9, text = "Please enter the notes for the file below: ").pack()
    entry1 = Entry(screen9, textvariable = raw_notes)
    entry1.pack()
    button = Button(screen9, text = "Save")
    button.pack()
    button.bind('<Button-1>', save)
    screen9.bind('<Return>', save)
   
    
   
 # Event after pressed the button in View Notes Window
def view_notes1(event):
    filename1 = raw_filename1.get()
    data = open(".\\notes\\" + username1 + '-' + filename1, "r")
    data1 = data.read()
    screen12 = Toplevel(screen)
    screen12.title(raw_filename1.get())
    screen12.geometry("400x400")
    Label(screen12, text = data1).pack()
    data.close()



 # View Notes Window
def view_notes():
    screen11 = Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("250x250")
    all_files = os.listdir(".\\notes")
    user_files = []
    
    for x in all_files:
        y = x.split('-')
        if y[0] == username1:
            user_files.append(y[1])

    Label(screen11, text = "Please use one of the filenames below").pack()
    Label(screen11, text = user_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen11, textvariable = raw_filename1).pack()
    button = Button(screen11, command = view_notes1, text = "OK")
    button.pack()
    button.bind('<Button-1>', view_notes1)
    screen11.bind('<Return>', view_notes1)



 # Event after pressed the button in Delete Note Window
def delete_note1(event):
    filename3 = username1 + "-" + raw_filename2.get()
    os.remove(".\\notes\\" + filename3)
    screen14 = Toplevel(screen)
    screen14.title("Notes")
    screen14.geometry("400x400")
    Label(screen14, text = raw_filename2.get() + " removed").pack()
   


 # Delete Note Window 
def delete_note():
    screen13 = Toplevel(screen)
    screen13.title("Info")
    screen13.geometry("250x250")
    all_files = os.listdir(".\\notes")
    user_files = []
    
    for x in all_files:
        y = x.split('-')
        if y[0] == username1:
            user_files.append(y[1])
    
    Label(screen13, text = "Please use one of the filenames below").pack()
    Label(screen13, text = user_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen13, textvariable = raw_filename2).pack()
    button = Button(screen13, command = delete_note1, text = "OK")
    button.pack()
    button.bind('<Button-1>', delete_note1)
    screen13.bind('<Return>', delete_note1)



 # Start Session after logged in
def session():
    screen8 = Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("400x400")
    Label(screen8, text = "Welcome to the Dashboard").pack()
    Button(screen8, text = "Create Note", command = create_notes).pack(pady = 10)
    Button(screen8, text = "View Note", command = view_notes).pack(pady = 10)
    Button(screen8, text = "Delete Note", command = delete_note).pack(pady = 10)
    


 # If the login was successful
def login_success():
    session()
    screen2.destroy()
    
    

 # If the password is wrong    
def password_not_recognised():
    
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete3).pack()
    
    
    
 # If the user name is not exist    
def user_not_found():
    
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User Not Found")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found", fg = "red").pack(pady = 10)
    Button(screen5, text = "OK", command = delete4).pack(pady = 10)
    


 # Event after pressed the button in Register Window
def register_user(event):
    username_info = username.get()
    password_info = password.get()
    cpyted = hashlib.md5(password_info.encode())
    
    
    file  = open(".\\users\\"+username_info, "w")
    file.write(username_info+"\n")
    file.write(cpyted.hexdigest())
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text = "Registration Success", fg = "green", font = ("Calibri", 11)).pack()




 # Event after pressed the button in Login Window
def login_verify(event):
    
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    cpyted = hashlib.md5(password1.encode())
    
    
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    list_of_files = os.listdir(".\\users")
    if username1 in list_of_files:
        file1 = open(".\\users\\"+username1, "r")
        verify = file1.read().splitlines()
        if cpyted.hexdigest() in verify:
            login_success()
        else: 
            password_not_recognised()
    else: 
        user_not_found()
    
    
    
    
 # Register Window
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "Please enter details below").pack(pady = 20)
    Label(screen1, text = "Username: ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack(pady = 5)
    Label(screen1, text = "Password: ").pack()
    password_entry = Entry(screen1, show = "*", textvariable = password)
    password_entry.pack(pady = 5)
    button1 = Button(screen1, text = "Register", width = 10, height = 1)
    button1.pack(pady = 20)
    button1.bind("<Button-1>", register_user)
    screen1.bind("<Return>", register_user)
    
  
    
 #Login Window  
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack(pady = 20)
    
    global username_verify
    global password_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1
    
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack(pady = 5)
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, show = "*", textvariable = password_verify)
    password_entry1.pack(pady = 5)
    button1 = Button(screen2, text = "Login", width = 10, height = 1)
    button1.pack(pady = 20)
    button1.bind("<Button-1>", login_verify)
    screen2.bind("<Return>", login_verify)
    
    
    
 #Startup Window   
def main_screen():
    try:
        os.mkdir('users')
    except FileExistsError:
        pass
    
    try:
        os.mkdir('notes')
    except FileExistsError:
        pass
    
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack(pady = 10)
    Button(text = "Login", height = "2", width = "30", command = login).pack(pady = 20)
    Button(text = "Register", height = "2", width = "30", command = register).pack()
    
    screen.mainloop()

main_screen()    




