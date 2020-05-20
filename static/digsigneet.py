import random
from hashlib import sha256

def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
    
def gcd_more(a, b):
    lastremainder, remainder = abs(a), abs(b)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if a < 0 else 1), lasty * (-1 if b < 0 else 1)
  
def modinv(a, m):
	g, x, y = gcd_more(a, m)
	if g != 1:
		raise Exception('Modular inverse does not exist')
	return x % m    

        
def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True


def keys():

    p=17
    q=23

    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)
 
    g = coprime(e, phi)
  
    while g != 1:
        e = random.randrange(1, phi)
        g = coprime(e, phi)

    d = modinv(e, phi)

    return ((e, n), (d, n))


def encrypt_fun(privatek, plaintext):
    key, n = privatek
            
    numberRepr = [ord(ch) for ch in plaintext]
    print("Number representation before encryption: ", numberRepr)
    cipher = [pow(ord(ch),key,n) for ch in plaintext]
    
    return cipher


def decrypt_fun(publick, ciphertext):
    key, n = publick
       
    numberRepr = [pow(ch, key, n) for ch in ciphertext]
    plain = [chr(pow(ch, key, n)) for ch in ciphertext]

    print("Decrypted number representation is: ", numberRepr)
    
    return ''.join(plain)
    
    
def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed
    
    
def verify(receivedHashed, message):
    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("No tampering detected ", )
    else:
        print("Verification failed")
        print(receivedHashed, " != ", ourHashed)
        

def main():   
    
    pub, pvt = keys()
    
    print("Your public key is ", pub ," and your private key is ", pvt)
    message = input("Enter a message to encrypt with your private key: ")
    print("")

    hashed = hashFunction(message)
    
    print("Encrypting message with private key ", pvt ," . . .")
    encrypted_msg = encrypt_fun(pvt, hashed)   
    
    print("Your encrypted hashed message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    
    print("")
    print("Decrypting message with public key ", pub ," . . .")

    decrypted_msg = decrypt_fun(pub, encrypted_msg)
    print("Your decrypted message is:")  
    print(decrypted_msg)
    
    print("")
    verify(decrypted_msg, message)
   
main()    