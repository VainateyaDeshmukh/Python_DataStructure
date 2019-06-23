import re
str = 'List of item are 1kg Rice, 5kg Wheat, 2ltr oil and 1kg Apples'
b= re.findall('kg [\w]+[\w]',str)
print(b)

