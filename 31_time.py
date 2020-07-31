import time

i = 0
while i < 8:
    print('\r value = ', i, end='')   # see the difference without using end='' and \r
    i += 1
    time.sleep(1)
