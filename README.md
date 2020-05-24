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

*tkinter
*os
*hashlib

''' python

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
'''
