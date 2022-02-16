import random
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

if __name__ == '__main__':
    privateKey = rsa.generate_private_key(public_exponent=65537, key_size=2048,);
    publicKey = privateKey.public_key();
    print("Public Key for this session: ")
    print(publicKey)
    print("Private Key for this session: ")
    print(privateKey)
    random.seed();
    s = random.randrange(0, 39)
    while True:
        userIn = input("Command: ")
        if userIn == "reset":
            random.seed();
            s = random.randrange(0, 39)
        elif userIn == "private key":
            privateKey = input("Enter private key: ");
        elif userIn == "private key":
            publicKey = input("Enter public key: ");
        elif userIn == "encrypt":
            print("Message Encryption")
            result = ""
            text = input("Enter Message: ")
            s = random.randrange(0,39)
            for i in range(len(text)):
                char = text[i]
                if (char.isupper()):
                    c_index = ord(char) - ord('A')

                    c_shifted = (c_index + s) % 26 + ord('A')

                    c_new = chr(c_shifted)

                    result += c_new
                elif(char.islower()):
                    c_index = ord(char) - ord('a')

                    c_shifted = (c_index + s) % 26 + ord('a')

                    c_new = chr(c_shifted)

                    result += c_new
                elif(char.isdigit()):
                    c_new = (int(char) + s) % 10

                    result += str(c_new)
            print(result)
            rsaResult = publicKey.encrypt(
                result.encode('UTF-8'),
                padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
            )
            print(rsaResult)
            encf = open("rsaencode.txt", "wb")
            encf.write(rsaResult)
            encf.close()
        elif userIn == "decrypt":
            encr = open("rsaencode.txt", "rb")
            openDecode = encr.read()
            decryptMessage = openDecode
            print(decryptMessage)
            rsaDecrypt = privateKey.decrypt(
                decryptMessage,
                padding.OAEP( mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
            )
            newResult = ""
            decrypter = str(rsaDecrypt)
            print(decrypter)
            for i in range(2,len(decrypter)-1,1):
                char = str(decrypter)[i]
                if (char.isupper()):
                    c_index = ord(char) - ord('A')

                    c_og_pos = (c_index - s) % 26 + ord('A')

                    c_og = chr(c_og_pos)

                    newResult += c_og
                elif(char.islower()):
                    c_index = ord(char) - ord('a')

                    c_og_pos = (c_index - s) % 26 + ord('a')

                    c_og = chr(c_og_pos)

                    newResult += c_og
                else:
                    c_og = (int(char) - s) % 10

                    newResult += str(c_og)
            print(newResult)
