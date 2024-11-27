import os


def olvasas(file_path):
    with open(file_path, "r", encoding="utf-8") as fajl:
        for sor in fajl:
            user = sor.strip().split(";")
            yield user[0], user[1]


def tarolas(file_path, nev, jelszo):
    with open(file_path, "a", encoding="utf-8") as fajl:
        fajl.write(f"{nev};{jelszo}\n")




class AppBackend:
    def __init__(self, users_file, messages_file):
        self.users_file = users_file
        self.messages_file = messages_file
        if not os.path.exists(self.users_file):
            open(self.users_file, "w", encoding="utf-8").close()

        if not os.path.exists(self.messages_file):
            open(self.messages_file, "w", encoding="utf-8").close()

    def user_exists(self, username):
        for stored_user, _ in olvasas(self.users_file):
            if stored_user == username:
                return True
        return False

    def register(self, username, password):
        if self.user_exists(username):
            return False
        tarolas(self.users_file, username, password)
        return True

    def login(self, username, password):
        for stored_user, stored_pass in olvasas(self.users_file):
            if stored_user == username and stored_pass == password:
                return True
        return False

    def save_message(self, username, message):
        tarolas(self.messages_file, username, message)

    def get_messages(self):
        with open(self.messages_file, "r", encoding="utf-8") as f:
            return f.readlines()

    def delete_message(self, message_line):
        with open(self.messages_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if 0 <= message_line < len(lines):
            lines.pop(message_line)

        with open(self.messages_file, "w", encoding="utf-8") as f:
            f.writelines(lines)
