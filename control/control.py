import view.view as view
import model.model as model
import pyperclip as pc


class PasswordManagerController:
    def __init__(self, db_path):
        self.model = model.PasswordManager(db_path)
        self.view = view.UI

    def add_password(self):
        username, source, password = self.view.handleNewPassword()
        masterPassword = self.view.getMasterPassword()

        password_instance = model.Password(username=username, source=source)
        password_instance.encrypt_password(
            master_password=masterPassword, plain_password=password
        )

        self.model.add_password(password_instance)
        self.view.displayMessage("Password inserted")

    def get_password(self, username, source):
        masterPassword = self.view.getMasterPassword()

        password = self.model.get_passwd(username, source)

        if password:
            plain_password = password.decrypt_password(masterPassword)
            self.view.displayPassword(plain_password)
        else:
            self.view.displayError(404, "Password not found.")

    def get_password_to_clipboard(self, username, source):
        masterPassword = self.view.getMasterPassword()

        password = self.model.get_passwd(username, source)

        if password:
            plain_password = password.decrypt_password(masterPassword)
            pc.copy(plain_password)
        else:
            self.view.displayError(404, "Password not found.")

    # def update_password(self, username, source):
    #     oldPassword = self.model.get_passwd(username, source)
    #     if oldPassword is None:
    #         self.view.displayError(404, "Not found")
    #         return
    #
    #     # Get new password
    #     username, source, password = self.view.handleNewPassword()
    #     masterPassword = self.view.getMasterPassword()
    #
    #     newPassword = model.Password(username=username, source=source)
    #     newPassword.encrypt_password(
    #         master_password=masterPassword, plain_password=password
    #     )
    #
    #     if self.master_password_authentication(masterPassword):
    #         self.model.update_password(oldPassword, newPassword)
    #         self.view.displayMessage("Update successful")
    #     else:
    #         self.view.displayError(401, "Authenticaion fail")

    def delete_password(self, username, source):
        toDelPassword = self.model.get_passwd(username, source)
        if toDelPassword is None:
            self.view.displayError(404, "Not found")

        if self.view.displayConfirmationMessage(
            "Are you sure you want to delete ? This action cannot be undone. [Y/n]"
        ):
            self.model.delete_password(username=username, source=source)
        else:
            self.view.displayMessage("Deletion Successful")

    def get_all_password(self):
        passwords = self.model.get_all_passwords()

        if passwords:
            self.view.displayListPasswords(passwordList=passwords)
        else:
            self.view.displayError(404, "Empty database")

    # @staticmethod
    # def master_password_authentication(master_password):
    #     hashed = hashlib.sha256()
    #     hashed.update(master_password.encode('utf-8'))
    #
    #     with open("authentication.bin", 'rb') as file:
    #         authentication_password = file.read()
    #
    #     if hashed == authentication_password:
    #         return True
    #     else:
    #         return False
