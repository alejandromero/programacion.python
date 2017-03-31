"""CamelCase"""
#!/bin/python
import re
s = raw_input().strip(); s=s[0].upper()+s[1:]
print len(re.findall('[A-Z][^A-Z]*', s))