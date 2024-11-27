from me_fuggvenyek import ME_AppBackend
from chat_app import ChatApp

backend = ME_AppBackend("felhasznalok.txt", "messages.txt")
app = ChatApp(backend)
app.run()
