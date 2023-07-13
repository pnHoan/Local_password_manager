import getpass
from tabulate import tabulate


class UI():
    @staticmethod
    def displayError(code, message):
        print(f"Error {code}:{message}")
        pass

    @staticmethod
    def displayMessage(message):
        print(f"{message}")

    @staticmethod
    def getMasterPassword():
        return getpass("Enter master password: ")

    @staticmethod
    def displayListPasswords(passwordList):
        header = ["Source", "Username", "Password"]
        data = []
        for passwd in passwordList:
            source = passwd.source
            username = passwd.username
            encrypted_password = passwd.encrypted_password.hex()

            data.append([source, username, encrypted_password])

        if (len(data) != 0):
            print(tabulate(data, headers=header, tablefmt="fancy_grid"))
        else:
            UI.displayError(404, "No password found in database")
