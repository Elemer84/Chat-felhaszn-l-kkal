import os

class AppBackend:
    def __init__(self, users_file, messages_file):
        self.users_file = users_file
        self.messages_file = messages_file
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                pass  # Üres fájl létrehozása, ha nem létezik
        if not os.path.exists(self.messages_file):
            with open(self.messages_file, 'w') as f:
                pass  # Üres fájl létrehozása, ha nem létezik

    def register(self, username, password):
        with open(self.users_file, 'a') as f:
            f.write(f"{username}:{password}\n")

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
