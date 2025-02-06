class PinError(Exception):
    pass
correctPin = 1212
pin = int(input('Enter 4 digit PIN'))
try:
    if(pin == correctPin):
        print('Account Unblocked')
    else:
       raise PinError('Entered Pin is',pin)

except PinError as e:
    print('Incorrect pin: ',e)
