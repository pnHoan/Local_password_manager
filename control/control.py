import click
import view.view as view
import model.model as model


class PasswordManagerController:
    def __init__(self, db_path):
        self.model = model.PasswordManager(db_path)
        self.view = view.UI

    @click.command()
    def add_password(self):
        username, source, password = self.view.insertPassword()
        masterPassword = self.view.getMasterPassword()

        password_instance = model.Password(username=username, source=source)
        password_instance.encrypt_password(master_password=masterPassword, plain_password=password)

        self.model.add_password(password_instance)
        self.view.displayMessage("Password inserted")

    # @click.command()
    # def get_all_passwords(self):
    #     master_password = click.prompt("Enter your master password", hide_input=True)
    #     passwords = self.model.get_passwords(master_password)
    #     self.view.display_passwords(passwords)

    @click.command()
    @click.argument("username", required=True)
    @click.argument("source", required=True)
    def get_password(self, username, source):
        masterPassword = self.view.getMasterPassword()

        password = self.model.get_passwd(username, source)
        password.decrypt_password(masterPassword)
        if password:
            self.view.displayPassword(password)
        else:
            self.view.display_error("Password not found.")

    @click.command()
    def update():
        pass

    @click.command()
    def delete():
        pass
               
