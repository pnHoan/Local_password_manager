import sqlite3
import model.aes256 as aes256


class Password:
    def __init__(self, username, source, salt=''):
        self.username = username
        self.source = source
        self.salt = salt

    def encrypt_password(self, master_password, plain_password):
        self.salt = aes256.get_random_string(16)

        key = aes256.key_gen(master_password, self.salt)

        # Encrypt the password using the key
        self.encrypted_password = aes256.encrypt(plain_password.encode(), key)

    def decrypt_password(self, master_password):
        key = aes256.key_gen(master_password, self.salt)

        # decrypt the password using the key
        # self.encrypted_password = aes256.decrypt(self.encrypted_password, key)

        # temp Return for testing
        return aes256.decrypt(self.encrypted_password, key).decode()


class PasswordManager:
    def __init__(self, db_path='passwords.db'):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS passwords (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    source TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    encrypted_password BLOB NOT NULL
                )
            ''')
            conn.commit()

    def add_password(self, new_password):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO passwords (username, source, salt, encrypted_password) VALUES (?, ?, ?, ?)
                ''', (new_password.username, new_password.source, new_password.salt, new_password.encrypted_password))
            conn.commit()

    def get_passwords(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT username, source, salt, encrypted_password FROM passwords')
            rows = cursor.fetchall()

            passwords = []
            for row in rows:
                username, source, salt, encrypted_password = row
                password = Password(username, source, salt)
                password.encrypted_password = encrypted_password
                passwords.append(password)
            return passwords

    def get_passwd(self, username, source):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT username, source, salt, encrypted_password FROM passwords WHERE username = ? AND source = ?', (username, source,))
            row = cursor.fetchone()

            if row is None:
                return None

        username, source, salt, encrypted_password = row
        password = Password(username, source, salt)
        password.encrypted_password = encrypted_password
        return password

    def update_password(self, old_password, new_password):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            UPDATE passwords SET username = ?, source = ?, salt = ?, encrypted_password = ? WHERE username = ? AND source = ?
            ''', (new_password.username, new_password.source, new_password.salt, new_password.encrypted_password, old_password.username, old_password.source,))
            conn.commit()

    def delete_password(self, username, source):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
            DELETE FROM passwords WHERE username = ? AND source = ?
            ''', (username, source))

            conn.commit()
