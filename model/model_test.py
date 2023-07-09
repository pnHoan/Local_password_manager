import unittest
import os
from model import Password, PasswordManager

MASTER_PASSWORD = "master"
USERNAME1 = 'john'
SOURCE1 = "example.com"
PLAIN_PASS1 = "pass1"
USERNAME2 = 'dave'
SOURCE2 = "example.com"
PLAIN_PASS2 = "pass2"
PLAIN_PASS3 = "pass3"


class PasswordManagerTests(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test.db'
        self.manager = PasswordManager(self.db_path)

    def tearDown(self):
        os.remove(self.db_path)

    def test_add_password(self):
        password = Password(USERNAME1, SOURCE1)
        password.encrypt_password(MASTER_PASSWORD, PLAIN_PASS1)

        # Add password
        self.manager.add_password(password)

        # Retrieve added password
        retrieved_password = self.manager.get_passwd(USERNAME1, SOURCE1)
        self.assertIsNotNone(retrieved_password)
        self.assertEqual(retrieved_password.username, USERNAME1)
        self.assertEqual(retrieved_password.source, SOURCE1)
        self.assertEqual(retrieved_password.decrypt_password(MASTER_PASSWORD), PLAIN_PASS1)

    def test_get_passwords(self):
        # Add multiple passwords
        password1 = Password(USERNAME1, SOURCE1)
        password2 = Password(USERNAME2, SOURCE2)
        password1.encrypt_password(MASTER_PASSWORD, PLAIN_PASS1)
        password2.encrypt_password(MASTER_PASSWORD, PLAIN_PASS2)

        # Add password
        self.manager.add_password(password1)
        self.manager.add_password(password2)

        # Retrieve all passwords
        passwords = self.manager.get_passwords()
        self.assertEqual(len(passwords), 2)

        # Check the details of each password
        retrieved_password1 = passwords[0]
        self.assertEqual(retrieved_password1.username, USERNAME1)
        self.assertEqual(retrieved_password1.source, SOURCE1)
        self.assertEqual(retrieved_password1.decrypt_password(MASTER_PASSWORD), PLAIN_PASS1)

        retrieved_password2 = passwords[1]
        self.assertEqual(retrieved_password2.username, USERNAME2)
        self.assertEqual(retrieved_password2.source, SOURCE2)
        self.assertEqual(retrieved_password2.decrypt_password(MASTER_PASSWORD), PLAIN_PASS2)

    def test_update_password(self):
        # Add a password
        original_password = Password(USERNAME1, SOURCE1)
        original_password.encrypt_password(MASTER_PASSWORD, PLAIN_PASS1)
        self.manager.add_password(original_password)

        # Retrieve the password
        retrieved_password = self.manager.get_passwd(USERNAME1, SOURCE1)
        self.assertIsNotNone(retrieved_password)

        # Update the password
        updated_password = Password(USERNAME1, SOURCE1)
        updated_password.encrypt_password(MASTER_PASSWORD, PLAIN_PASS2)
        self.manager.update_password(retrieved_password, updated_password)

        # Retrieve the updated password
        retrieved_updated_password = self.manager.get_passwd(USERNAME1, SOURCE1)
        self.assertIsNotNone(retrieved_updated_password)
        self.assertEqual(retrieved_updated_password.decrypt_password(MASTER_PASSWORD), PLAIN_PASS2)

    def test_delete_password(self):
        # Add a password
        password = Password(USERNAME1, SOURCE1)
        password.encrypt_password(MASTER_PASSWORD, PLAIN_PASS1)
        self.manager.add_password(password)

        # Delete the password
        self.manager.delete_password(USERNAME1, SOURCE1)

        # Retrieve the deleted password
        deleted_password = self.manager.get_passwd(USERNAME1, SOURCE1)
        self.assertIsNone(deleted_password)


if __name__ == '__main__':
    unittest.main()
