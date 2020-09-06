import re

p = re.compile("ca.e")

m = p.match("cafe")
#print(m.group())

def print_match(m):
    if m:
        print(m.group())
    else:
        print("no matching")