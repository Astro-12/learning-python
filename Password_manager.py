import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb")as key_file:
        key_file.write(key)
'''write_key() generates a fernet key and let it gets store in a local file named key.key'''

def load_key():
        with open("key.key", "rb") as file:
            key = file.read()
        return key
'''Reads and return the saved fernet key from key.key'''

def get_salt():
    if os.path.exists("salt.salt"):
        with open("salt.salt", "rb")as f:
            return f.read()
    else:
        salt = os.urandom(16)
        with open("salt.salt", "wb")as f:
            f.write(salt)
        return salt
'''get_salt():generate or loads salt
    salt is a random value stored in a file 
    you generate and laod this password once and everytime you load your passwords you read this salt
    A salt is a random (but not secret) value used with your password to produce a unique encryption key'''
def validate_master_password(fer):
    try:
        with open('passwords.txt', 'r')as f:
            for line in f:
                if "|" in line:
                    user, enc_pwd = line.strip().split("|")
                    fer.decrypt(enc_pwd.encode())
                    break   
    except FileNotFoundError:
        return
    except Exception:
        print("Invalid master password or data is corrupted.")
        exit()

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,  
        iterations=390000,
        backend=default_backend()
    )
    
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
'''PBKDF2HMAC (Password-Based Key Derivation Function 2, HMAC variant):
    usage:
    Takes the password (entered by the user), 
    the salt (from get_salt()), 
    a hash algorithm (SHA256), 
    a key length (32 bytes for Fernet),
    and a high number of iterations (e.g., 390,000).
Runs these through PBKDF2HMAC to "stretch" the password into a strong key.
This makes brute-force and dictionary attacks much harder.'''
import os
if not os.path.exists("key.key"):
    write_key()
''' If key.key is not existing will create one with write_key.'''

master_pwd = input("Enter master password: ")
salt = get_salt()
key = derive_key(master_pwd, salt)
fer = Fernet(key)
''' after loading the code creates a fernet object'''
'''Purpose: All encryption and decryption is done through this object.'''
validate_master_password(fer)



def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" in data:
                    user, pwd = data.split("|")
                    decypted_pwd = fer.decrypt(pwd.encode()).decode()
                    print("User: ", user, "| Password: ", decypted_pwd)
    except FileNotFoundError:
        print("No passwords stored yet.")
        '''decrypts the encryted password
        lets the user see the real password
        '''
                    
def add():
    Name = input('Account name: ')
    pwd = input('Password: ')
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()   
    with open('passwords.txt', 'a') as f:
        f.write(Name + "|" + encrypted_pwd + "\n")
        '''The user input name and password
        password is converted into encryption through fernet
        .encode()turns the data into bytes
        .decode()turns the data back into string format for reading
        '''

while True:
    
    mode =input("Would you like to add new passwords or veiw the existing ones? (add/view)or 'q' to quit.. ").lower()
    if mode == 'q':
        break  
    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Invalid response, please enter 'add', 'view' or 'q'")
        continue
    
    '''Later enhacements for this project:
    Password Generator: Add an option to generate strong, random passwords automatically.
    Limit Login Attempts: If a user enters the wrong master password multiple times, temporarily lock them out
Safe File Handling: Create backups of passwords.txt before making changes, and allow user to restore from backups

    '''