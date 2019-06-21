# This program adds two numbers provided by the user.
# Store input numbers.
mks = input('Enter marks of the student: ')
print('Student has scored '+ mks +' marks')

if mks > '60':
    print('Student has passed.')
elif mks == '60':
    print('Student has passed with ' + mks +' marks')
else:
    print('Student has failed.')