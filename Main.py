from me_fuggvenyek import AppBackend
from chat_app import ChatApp

backend = AppBackend("felhasznalok.txt", "messages.txt")
app = ChatApp(backend)
app.run()
