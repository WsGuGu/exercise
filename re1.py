import re

s = 'hello python'
pattern = r'\w+\s\w+'
o = re.match(pattern, s)
print(o.group())
s = 'hello python hello python'
pattern = r'(\w+) (\w+)'
o = re.search(pattern, s)
print(o.groups())
print(o.group(1))
print(o.group(2))
s = 'hello python hello python'
pattern = r'(\w+) (\w+)'
o = re.findall(pattern, s)
print(o)