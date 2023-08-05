import getpass
from tabulate import tabulate


class UI:
    @staticmethod
    def displayError(code, message):
        print(f"Error {code}:{message}")
        pass

    @staticmethod
    def displayMessage(message):
        print(f"{message}")

    @staticmethod
    def getMasterPassword():
        master_password = getpass.getpass("Enter master password: ")
        return master_password

    @staticmethod
    def displayListPasswords(passwordList):
        header = ["Source", "Username", "Password"]
        data = []
        for passwd in passwordList:
            source = passwd.source
            username = passwd.username
            encrypted_password = passwd.encrypted_password.hex()

            data.append([source, username, encrypted_password])

        if len(data) != 0:
            print(tabulate(data, headers=header, tablefmt="fancy_grid"))
        else:
            UI.displayError(404, "No password found in database")

    @staticmethod
    def handleNewPassword():
        username = input("Enter username: ")
        source = input("Enter source (e.g., website): ")
        password = getpass.getpass("Enter your password: ")

        return username, source, password

    @staticmethod
    def displayConfirmationMessage(message):
        while True:
            userInput = input(message)
            if not userInput:
                return True

            if userInput in ["Y", "y"]:
                return True

            if userInput in ["N", "n"]:
                return False

            print("Invalid input! please try again")

    @staticmethod
    def displayPassword(password_string):
        if password_string is not None:
            print(password_string[:5], end="")
            print("*" * len(password_string[5:]))

    @staticmethod
    def getUserInput(promt, defaultValue):
        userInput = input(f"{promt} [{defaultValue}]")
        if userInput:
            return userInput
        else:
            return defaultValue
