import re
test_string = 'if you want to 12-364-5616 call aashiq call him at no 12-384-5616'
search = re.search(r'\d\d-\d\d\d-\d{4}', test_string)
find = re.findall(r'\d{2}-\d{3}-\d{4}', test_string)
print(search)
print(search.group(0))
print(find)
