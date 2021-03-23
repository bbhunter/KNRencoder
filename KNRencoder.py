#! usr/bin/env python3
import urllib.parse as urlparse
import html
import base64
user_input = input ("Enter the String to Encode: ")
print('\n')

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }


def urlencode():
	quote_encoded = urlparse.quote(user_input)
	quote_plus_encoded = urlparse.quote_plus(user_input)

	print("Quote Encoded: " + quote_encoded)
	print("Quote Plus Encoded: " + quote_plus_encoded)

def html_encode():
	"""Produce entities within text."""
	html_encoded =  "".join(html_escape_table.get(c,c) for c in user_input)
	print("HTML Encoded: " + html_encoded)

def base64_encode():
	string_bytes = user_input.encode("ascii") 
	base64_bytes = base64.b64encode(string_bytes) 
	base64_string = base64_bytes.decode("ascii") 
	print("Base64 Encoded: " + base64_string)




urlencode()
html_encode()
base64_encode()