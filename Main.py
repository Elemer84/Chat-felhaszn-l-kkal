from me_fuggvenyek import AppBackend
from me_chat_app import ChatApp

if __name__ == "__main__":
    backend = AppBackend("users.txt", "messages.txt")
    app = ChatApp(backend)
    app.run()