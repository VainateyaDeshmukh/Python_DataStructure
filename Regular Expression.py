#  A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings,
#  using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.


import re

 a= re.match('app','application ')
 print(a)
 print(a.start())
 #
 c=a.end()
 print(c)
 d=a.span()
 print(d)
 print(a.group())
# #
 a = re.match('app','myapplication')    #find first
 print(a)
 a = re.search('app','myapplication app') #find first
 print(a)
 a = re.findall('app','myapplication apply')  #finds all
 print(a)

#          #METACHARACTER[]
 b= re.search('[xyz]','this is my application')
 print(b)
 b= re.search('m[xyz]','this is my application')
 print(b)
 b= re.search('n[xyz]','this is my application')   #there is no comabination of ny/nx/nz
 print(b)
 b= re.search('m[w-z]','this is my application')
 print(b)
#
#
  \w = [a-zA-Z0-9_]    #(Match Alphanumeric Character)

 b= re.search ('m[a-zA-Z0-9_]','this is my application')
 print(b)
 b= re.search ('m[a-zA-Z0-9_]','this is mY application')
 print(b)
 b= re.search ('m[a-zA-Z0-9_]','this is m1 application')
 print(b)
 b= re.search ('m[a-zA-Z0-9_]','this is m_ application')
 print(b)
 b.group()
# #
 b= re.search('m[\w]','this is my appliction')
 print(b)
 b= re.search ('m[\w]','this is my application')
 print(b)
 b= re.search ('m[\w]','this is mY application')
 print(b)
 b= re.search ('m[\w]','this is m1 application')
 print(b)
 b= re.search ('m[\w]','this is m_ application')
 print(b)
#
#
#
 \W = Opposite of \w #('wont Match alphanumetic character )
 b= re.search ('m[\W]','this is m? application')
 print(b)


#
 \d = [0-9] #(Matches digit)
 b= re.search ('m[\d]','this is m200 application')
 print(b)
 b= re.search ('m[\d]+','this is m200 application')
 print(b)
 b= re.search ('m[\d]','this is m application')
 print(b)
 b= re.search ('m[\d]*','this is m application')
 print(b)
 b= re.search ('m[\d]*','this is m200 application')
 print(b)
#
#
\D = opposit of \d
 b= re.search ('m[\D]','this is m? application')
 print(b)
 b= re.findall ('m[\w]','my name is manoj application')
 print(b)
 b= re.findall ('m[\w]+','my name is manoj application')
 print(b)




 str = 'SBI 1000'
 b = re.search('[\d]+','SBI 1000')
 print (b)
 print(b.group())
#
#
email1 = 'My primary email is manoj@abc.com and' 'the second one is mannoj1@abc.com'
b = re.findall('[\w]+@[\w]+.[\w]+',email1)
print (b)
#
#
 phone = "My phone is (020)111-2222 and (022)222-3333"
 ph = re.findall("\(\d{3}\)\d{3}-\d{4}",phone)
 print (ph)
#
#
 str = 'SBI -NSE - 28/03 (15:59)'
 d = re.findall("\d{2}/\d{2}")
 print(d)
#
#
# phone=""