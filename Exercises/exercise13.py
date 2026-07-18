import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")

#Encryption

print("Encryption:")
plain_text = input("Enter the data that is to be encrypted:")
cipher_text = ""

for letter in plain_text:
    index = key.index(letter)  #index is random variable we assign to get assign to plain text basiicaly index is 0 to whatever end of list is number astat na
    cipher_text += chars[index]

print(f"Plain text    : {plain_text}")
print(f"Encrypted text: {cipher_text}")

#Decryption

print("Dencryption:")
cipher_text = input("Enter the data that is to be decrypted:")
plain_text = ""

for letter in cipher_text:
    index = chars.index(letter)  #index is random variable we assign to get assign to plain text basiicaly index is 0 to whatever end of list is number astat na
    plain_text += key[index]

print(f"Encrypted text: {cipher_text}")
print(f"Decrypted text: {plain_text}")