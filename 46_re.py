import re 
text = "let's learn regex"
new_text = re.sub('\s', '_', text)  # replacing all white space characters with underscore(_)
print(new_text)

