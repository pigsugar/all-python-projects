import hashlib
from simplecrypt import encrypt, decrypt
value = "peter : hello"
def SHA256():
    result = hashlib.sha256(value.encode())
    print("sha256 encrypted data: ", result.hexdigest())
SHA256()
def MD5():
    result = hashlib.md5(value.encode())
    print("MD5 encrypted data: ", result.hexdigest())
MD5()
message = "peter : hello"
hex_string = ""
def encryption():
    global hex_string
    ciphercode = encrypt('AIM',message)
    hex_string=ciphercode.hex()
    print("encryption " , hex_string)
def decryption():
    global hex_string
    byte_str = bytes.fromhex(hex_string)
    original = decrypt("AIM", byte_str)
    final_message=original.decode("utf-8")
    print("decryption " , final_message)
encryption()
decryption()

