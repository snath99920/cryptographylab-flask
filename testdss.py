from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA1
import base64

class DSS():
    # def __init__(ds1, message = 'test'):
        # ds1.message = message

    def set_message(ds1, message):
        ds1.message = message
        # print(ds1.message)
        # print("")

    def gen_keys(ds1, bits, e=None):
        '''Generates the public and private keys for the object'''
        if(e==None):
            key = RSA.generate(bits)
        else:
            key = RSA.generate(bits, e=e)
        ds1.private_key = key.exportKey('DER')
        ds1.public_key = key.publickey().exportKey('DER')
        return ds1.public_key.hex()
    
    def gen_hash(ds1, h):
        # h = SHA1.new()
        h.update(ds1.message.encode('utf8'))
        return h.hexdigest()

    def gen_DS(ds1, h):
        '''Generates the Digital Signature for the message by encrypting the hash
           of the message with private key'''
        h2 = SHA1.new()
        h2.update(ds1.message.encode('utf8'))
        h = h2.hexdigest()
        if(h == h2.hexdigest()):
            try:
                key = RSA.import_key(ds1.private_key)
                signature = pkcs1_15.new(key).sign(h2)
            except:
                return 
            ds1.signature = signature
            sig = str(base64.b64encode(bytes.fromhex(signature.hex())))
            sig64 = sig[1:]
            return signature.hex(), sig64
        else:
            raise ValueError

    def verify(ds1, ds, h):
        '''Decryptes the signature using Public key and compares the value with
           original hash'''
        h2 = SHA1.new()
        h2.update(ds1.message.encode('utf8'))
        if(True):
            key = RSA.import_key(ds1.public_key)
            try:
                pkcs1_15.new(key).verify(h, ds)
                s = "The signature is valid."
            except (ValueError, TypeError):
                s = "The signature is not valid."
            print(s)
            print("")    
            return s
        else:
            raise ValueError    

def main():
    ds1 = DSS()
    h = SHA1.new()
    message=input("Enter the message to be encrypted: ")
    ds1.set_message(message)
    print("Message set successfully")
    print("")
    ds1.gen_hash(h)
    print("Hash is: ", ds1.message)
    print("")
    ds1.gen_keys(1024)
    print("Keys generated")
    print("")
    ds1.gen_DS(h)
    print("Digital signature successfully generated")
    print("")
    ds1.verify(ds1.signature,h)
# ds1 = DSS()

main()