# Minda Elemér ui1vd6

Ez egy egyszerű chat alkalmazás 
lehet regisztrálni, bejelentkezni, üzeneteket bevinni és törölni



A következő modulok találhatók a programban:



Main.py

Elösször is Importáljuk a szükséges osztályokat a megfelelő modulokból.
Létrehozunk egy backend változót az ME_AppBackend osztályból, amely a fájlokat kezeli.
Létrehozunk app változót a ChatApp osztályból, amely a grafikus felületért felelős, és megadjuk neki hogy használja a ME_AppBackend modul funkcióit.
majd utánna itt történik a program futtatása




chat_app.py

Ebben a modulban a ChatApp osztály felelős a grafikai megjenenítésért tkinter segítségével.
Az osztály funkciói:
Inicializálás (__init__):
Bejelentkezési képernyő (create_login_frame):
Chat felület (create_chat_frame):
Regisztráció (register):
Bejelentkezés (login):
Üzenetek betöltése (load_messages):
Üzenet mentése (save_message):
Üzenet törlése (delete_message):
Kijelentkezés (me_logout):
Futtatás (run):



me_fuggvenyek.py

ebben a modulban a ME_AppBackend class felelős a program logikájáért amely a felhasználók és üzenetek kezelését végzi fájlokban
Az osztály funkciói:
Inicializálás (init):
Felhasználói ellenőrzés (user_exists):
Regisztráció (register):
Bejelentkezés (login):
Üzenet mentése (save_message):
Üzenetek lekérése (get_messages):
Üzenet törlése (delete_message):

kettő segédfügvény az osztálynak:
Olvasás (olvasas):
Tárolás (tarolas):
