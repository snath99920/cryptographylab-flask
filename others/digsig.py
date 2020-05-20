import random
from hashlib import sha256

def check_coprime(a, b):
	while (b!=0):
		a=b
		b=a%b
	return a

def gcd_more(a, b):
	lr, r = abs(a), abs(b)
	x, xr, y, yr = 0, 1, 1, 0
	while r:
		lr, (q, r) = r, divmod(lr, r)
		x, xr = xr - q*x, x 
		y, yr = yr - q*y, y
	return lr, xr*(-1 if a<0 else 1), yr*(-1 if b<0 else 1)

def modinv(a, b):
	g, x, y = gcd_more(a, b)
	if (g!=1):
		raise Exception("No modinv")
	return (x%m)

def is_prime(n):
	if n == 2:
		return True
	if int(n)<2 or int(n)%2 == 0:
		return False
	for i in range (3, int(n**0.5)+2, 2):
		if (n%i==0):
			return False
	return True

def keys(p, q):
	if not (is_prime(p) and is_prime(q)):
		raise ValueError("Prime numbers expected")
	elif (p == q):
		raise ValueError("Distinct numbers expected")

	n=p*q
	cyph=(p-1)*(q-1)

	e=random.randrange(1,cyph)

	g=check_coprime(e, cyph)

	while (g != 1):
		e=random.randrange(1,cyph)
		g=check_coprime(e,cyph)

	d=modinv(e, cyph)
	return ((e,n), (d,n))

def hash_en(message):
	hashed = sha256(message.encode("UTF-8")).hexdigest()
	return hashed

def encrypt_fun(pk, txt):
	key, n = pk
	numrep = [ord(char) for char in txt]
	cipher = [pow(ord(char), key, n) for char in txt]
	return cipher

def decrypt_fun(pubk, cip_txt):
	key, n = pubk
	numrep = [pow(char, key, n) for char in cip_txt]
	plain = [chr(pow(char, key, n)) for char in cip_txt]
	return ''.join(plain)

def verify(rhash, message):
	hashed = hash_en(message)
	if (rhash == hashed):
		print("No tampering detected!")
	else:
		print("Verification failed!")

def main():
	message=input("Enter the message you want to send: ")
	p=input("Enter prime1: ")
	q=input("Enter prime2: ")

	pub, pvt = keys(p, q)
	print("Pvt key:", pvt, " and public key: ", pub)

	hashed = hash_en(message)

	enc_mess = encrypt_fun(pvt, hashed)

	dec_mess = decrypt_fun(pub, enc_mess)

	verify(dec_mess, message)

main()