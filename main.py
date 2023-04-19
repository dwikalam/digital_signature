from hashlib import sha3_256
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.utils import file
from ellipticcurve.ecdsa import Signature
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.privateKey import PublicKey
import utils

def interface():
    while True:
        print("1. Tulis surel")
        print("2. Enkripsi surel")
        print("3. Tanda tangani surel")
        print("4. Dekripsi surel")
        print("5. Verifikasi tanda tangan surel")
        print("6. Bangkitkan kunci privat dan kunci publik")
        user_inp = ""
        while user_inp not in ["1", "2", "3", "4", "5", "6"]:
            user_inp = input(">> ")

        if (user_inp == "1"):
            filename = input("Nama file surel (tanpa ekstensi) = ")
            email_body = input("Isi surel: ")
            with open(filename + ".txt", "w") as dest:
                dest.write(email_body)
        
        elif (user_inp == "2"):
            pass
            # masukkan kunci

        elif (user_inp == "3"):
            filename = input("Nama file surel yang akan ditanda tangani (tanpa ekstensi) = ")
            
            privKeyFilename = input("Masukkan file berisi kunci privat (tanpa ekstensi) = ")
            with open(privKeyFilename + ".txt", "r") as priv_source:
                privateKey = PrivateKey.fromString(priv_source.read())
                publicKey = privateKey.publicKey()

                with open(filename + ".txt", "r") as source:
                    file_content = source.read()
                    signature = Ecdsa.sign(file_content, privateKey, hashfunc=sha3_256)
                    with open(filename + "_signed.txt", "w") as dest:
                        dest.write(file_content + f"\n<ds>{signature.toBase64()}</ds>")

                pubKeyFilename = input("Nama file kunci publik akan disimpan (tanpa ekstensi) = ")
                with open(pubKeyFilename + ".txt", "w") as pub_dest:
                    pub_dest.write(publicKey.toString())
        
        elif (user_inp == "4"):
            pass
            # masukkan kunci

        elif (user_inp == "5"):
            filename = input("Nama file surel bertanda tangan tanpa ekstensi = ")

            pubKeyFilename = input("Masukkan file berisi kunci publik (tanpa ekstensi) = ")
            with open(pubKeyFilename + ".txt", "r") as pub_source:
                pubKeyStr = pub_source.read()
                publicKey = PublicKey.fromString(pubKeyStr)
                
                with open(filename + ".txt", "r") as source:
                    email_data = source.read()
                    email_body = utils.strip_sign_tag(email_data)
                    digital_sign_base64 = utils.get_digital_sign(email_data)

                    signature = Signature.fromBase64(digital_sign_base64)
                    if Ecdsa.verify(email_body, signature, publicKey, hashfunc=sha3_256):
                        print("Digital signature valid!\n")
                    else:
                        print("Warning: Digital signature invalid\n")

        else:
            privateKey = PrivateKey()
            publicKey = privateKey.publicKey()
            privKeyFilename = input("Nama file kunci privat akan disimpan (tanpa ekstensi) = ")
            pubKeyFilename = input("Nama file kunci publik akan disimpan (tanpa ekstensi) = ")
            
            with open(privKeyFilename + ".txt", "w") as priv_dest:
                priv_dest.write(privateKey.toString())
            with open(pubKeyFilename + ".txt", "w") as pub_dest:
                pub_dest.write(publicKey.toString())

if __name__ == '__main__':
    interface()