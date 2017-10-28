e = input('Do you want to: add, subtract, times or divide? ')

if e == 'times':
    a = input('choose a number ')
    b = input('choose a number ')
    c = int(a) * int(b)
    print('answer: ' + str(c))
    d = input(Press enter to exit.)
    
elif e == 'subtract':
    a = input('choose a number ')
    b = input('choose a number ')
    c = int(a) - int(b)
    print('answer: ' + str(c))
    d = input(Press enter to exit.)

elif e == 'add':
    a = input('choose a number ')
    b = input('choose a number ')
    c = int(a) + int(b)
    print('answer: ' + str(c))
    d = input(Press enter to exit.)

elif e == 'divide':
    a = input('choose a number ')
    b = input('choose a number ')
    c = int(a) / int(b)
    print('answer: ' + str(c))
    d = input(Press enter to exit.)
