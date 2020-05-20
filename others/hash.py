import random
from hashlib import sha256

def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed

def main():
	hashed=hashFunction(message)

main()