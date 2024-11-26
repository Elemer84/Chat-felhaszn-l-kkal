import os


class AppBackend:
    def __init__(self, users_file, messages_file):
        self.users_file = users_file
        self.messages_file = messages_file

        # Csak akkor hozunk létre új fájlt, ha nem létezik
        if not os.path.exists(self.users_file):
            open(self.users_file, 'w').close()  # Üres fájl létrehozása, ha nem létezik

        if not os.path.exists(self.messages_file):
            open(self.messages_file, 'w').close()  # Üres fájl létrehozása, ha nem létezik

    def user_exists(self, username):
        """ Ellenőrzi, hogy létezik-e már a felhasználó a fájlban. """
        with open(self.users_file, 'r') as f:
            for line in f:
                stored_user, _ = line.strip().split(":")
                if stored_user == username:
                    return True  # Felhasználó már létezik
        return False

    def register(self, username, password):
        """ Felhasználó regisztrálása, ha nem létezik már a felhasználó. """
        if self.user_exists(username):
            return False  # Ha létezik, nem regisztráljuk újra

        # Ha nem létezik, regisztráljuk
        with open(self.users_file, 'a') as f:
            f.write(f"{username}:{password}\n")
        return True  # Sikeres regisztráció

    def login(self, username, password):
        with open(self.users_file, 'r') as f:
            for line in f:
                stored_user, stored_pass = line.strip().split(":")
                if stored_user == username and stored_pass == password:
                    return True
        return False

    def save_message(self, username, message):
        with open(self.messages_file, 'a') as f:
            f.write(f"{username}: {message}\n")

    def get_messages(self):
        with open(self.messages_file, 'r') as f:
            return f.readlines()

    def delete_message(self, message_line):
        with open(self.messages_file, 'r') as f:
            lines = f.readlines()

        if 0 <= message_line < len(lines):
            lines.pop(message_line)

        with open(self.messages_file, 'w') as f:
            f.writelines(lines)
