# Egyszerű beléptető rendszer felület, felhasználónként jegyzetek készítése funkcióval  (Login System)
## Bevezetés

A program célja az, hogy kezelni tudja a felhasználókat, mindenki csak a saját jegyzeteihez férjen hozzá, a jelszavakat pedig hashelés után tároljuk, hogy ne lehesen kiolvasni.

A következő funkciókat valósítottuk meg:

* Regisztráció
* Belépés
* Jegyzetek létrehozása
* Jegyzetek megtekintése
* Jegyzetek törlése

A projekt egy .py file-t tartalmaz.

használt könyvtárak: 

 * tkinter
 * os
 * hashlib

## A program felépítése

Induláskor létrehozunk 2 mappát, ha nincsenek még létrehozva a 'users' és a 'notes' mappát. Ezután feljön a kezdőképernyő, ahol 2 lehetőségünk van belépni vagy regisztrálni. 

```python

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
```

Regisztráció esetén kimenti a felhasználónevet és a hashelt jelszót egy fileba a 'users' mappába, később ezek között fogja keresni a felhasználónevet és a jelszavat. 

```python
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
 ```  
 
 Belépéskor a regisztrált felhasználók közül keresi, hogy létezik-e a felhasználó, ha nem akkor azt írja ki, ha létezik a felhasználó, akkor ellenőrzi, hogy jó-e a jelszó. Mivel hashelve van tárolva a jelszó, neki is hashelni kell, amit beírunk ide.
 
 ```python
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
  ```
