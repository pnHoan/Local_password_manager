**Password Manager CLI**

## Overview

This is a simple offline command-line password manager written in Python that allows you to securely store and manage your passwords. The application uses the MVC (Model-View-Controller) architecture to maintain separation between the data (Model), the user interface (View), and the application logic (Controller).

## Features

- Store passwords for different sources (e.g., websites, applications) with associated usernames.
- Encrypt passwords using a master password.
- View all stored passwords and retrieve specific passwords using source and username.
- Delete existing password entries.
- Command-line interface for easy and quick interactions.
- Copy to clipboard 

## Requirements

- Python 3.6+
- Click library 
- Cryptography library
- SQLite3
- Pyperclip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/password-manager-cli.git
   cd password-manager-cli
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the password manager, execute the main script:

```bash
python main.py [COMMAND] [OPTIONS]
```

The available commands are:

- `add`: Add a new password entry to the database.
- `get [username] [source]`: View stored passwords with the username and source provided.
- `get [username] [source] -c`: Copy to clipboard stored passwords with the username and source provided.
- `del [username] [source]`: Delete a password entry.

For example, to add a new password:

```bash
python main.py add_password
```

You will be prompted to enter the username, source (e.g., website), password, and master password for encryption.

For other commands, the application will guide you through the necessary steps.

## Security

The application encrypts passwords using AES256 with the provided master password and stores them in a SQLite database. The passwords are decrypted only when retrieved using the master password. However, it is essential to choose a strong master password and keep it secure to ensure the safety of your passwords.

## Limitations

- This password manager is a simple implementation and may not be suitable for handling large-scale or enterprise-level requirements.
- The application stores passwords locally on your system. Be cautious when using it on shared or public computers.

## Contributing

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, please feel free to submit a pull request.


## Disclaimer

The password manager is provided as-is without any warranties. Always take proper precautions to safeguard your data and use this application responsibly. The developers of this application shall not be liable for any loss or damage caused by the use of this software.
