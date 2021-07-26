# import gmpy2
# import binascii
#
# from rsa import transform
#
# n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
# p = 275127860351348928173285174381581152299
# q = 319576316814478949870590164193048041239
# e = 65537
# phi = (p - 1) * (q - 1)
# d = gmpy2.invert(e, phi)
# c = "hello".encode()
# c = transform.bytes2int(c)
# m = pow(c, d, n)
# print(m)
# # print(binascii.unhexlify(hex(m)[2:]).decode())
#
# k = int(pow(m, e, n))
# k = transform.int2bytes(k)
# k = k.decode()
# print(k)

# import rsa
# pubkey, prikey = rsa.newkeys(256)
# print(pubkey)
# print(prikey)
# message = b"hello"
# en = rsa.encrypt(message, pubkey)
# print(en)
# de = rsa.decrypt(en, prikey)
# print(de)
# PublicKey(59422391769993503495832588805934977937411348577468247056835271696316980097533, 65537)
# PrivateKey(59422391769993503495832588805934977937411348577468247056835271696316980097533, 65537, 55568010467610996158591269627241574299582650554504712287320335738468450327553, 48956847442662925134332242350590643358081, 1213770797631272532190274943338516093)
import base64
from Cryptodome import Random
from Cryptodome.Hash import SHA
from Cryptodome.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Cryptodome.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Cryptodome.PublicKey import RSA
message = "hello client, this is a message"
with open("client-public.pem") as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    print(cipher_text.decode('utf-8'))