import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange
encryptor = PKCS1_OAEP.new(publickey)
encrypted = encryptor.encrypt(b'This is a private message intended to be encrypted using RSA.')
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted message:', encrypted) #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

print ('decrypted', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()