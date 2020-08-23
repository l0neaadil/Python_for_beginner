import re

test_string = 'Shah 12 Fayiz Wayiz Nayiz 8494 1234 00 Zahoor Sher'
result = re.findall(r'\d{2}', test_string)
print(result)
result = re.findall(r'\s\d{2}\s', test_string)
print(result)
result = re.findall('[1-5][2-6][4-7]', test_string)
print(result)
result = re.findall(r'\w{2}ah', test_string)
print(result)
result = re.search(r'[A-G][a-z]*', test_string)
print(result.group(0))
result = re.findall(r'[FWN]ayiz', test_string)
for name in result:
    print(name)

