import os
import sys
import binascii

def xor(filepath, key):
	decoded = []
	keylist = []
	hFile = open(filepath, 'rb')
	contents = hFile.read()
	hFile.close()

	hFile = open(key, 'r')
	key = hFile.read()
	hFile.close()
 	key.split()

	
	for x in key:
		keylist.append(ord(x))	

	for x in contents:
		decoded.append(ord(x))
	
	ctr  = 0 
	ctr1 = 0
	for x in decoded:
		decoded[ctr] = hex( x ^ keylist[ctr1])
		ctr +=1
		ctr1+=1
		if(ctr1>=len(keylist)-1):
			ctr1=0
	
	return(decoded)
	

if len(sys.argv) == 3:
	decoded = xor(sys.argv[1], sys.argv[2])
	hFile = open('testout.bin', 'wb')
	for x in decoded:
		hFile.write(chr(int(x,16)))
	hFile.close()
else:
	print 'usage:', sys.argv[0], '<file directory> <key file>'