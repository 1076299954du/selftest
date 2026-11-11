database = [['albert', '1234'],
            ['dilbert', '4242'],
            ['smith', '7524'],
            ['duzerui', '2222']]
username = input('User name:')
pin = input('PIN code')
if [username, pin] in database:
    print('Access granted')
