"""Caesar Cipher"""
#!/bin/python
n = int(raw_input().strip())
s = raw_input().strip(); new_s=[]
k = int(raw_input().strip())
print ''.join([chr((((ord(i)+k)-65)%26)+65) if i.isupper() else chr((((ord(i)+k)-97)%26)+97) if i.isalpha() else i for i in s])
