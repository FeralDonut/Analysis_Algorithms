"""
Jose-Antonio Rubio
CS 370-400
Programming Project 2
"""

import sys, hmac, base64, struct, hashlib, time
import pyqrcode


# source: https://stackoverflow.com/questions/8529265/google-authenticator-implementation-in-python
def generateTOTP(secret, intervals_no):
	key = base64.b32decode(secret, True)
	msg = struct.pack(">Q", intervals_no)
	h = hmac.new(key, msg, hashlib.sha1).digest()
	o = ord(h[19]) & 15
	h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
	return h

# source: https://pypi.org/project/PyQRCode/
def generateQR(text_string):
    big_code = pyqrcode.create(text_string)
    big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    big_code.show()

# main
key = "PASSCODE"
TOTP_string = "otpauth://totp/Secure%20App:rubioj%40oregonstate.edu?secret=" + key + "&issuer=Secure%20App"

if len(sys.argv) == 2:
	if sys.argv[1] == "--generate-qr":
		generateQR(TOTP_string)
	elif sys.argv[1] == "--get-otp":
		print(generateTOTP(key, intervals_no=int(time.time())//30))
	else:
		print("wrong command!")
		exit()
