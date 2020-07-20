# Cars
process = ""
stopped = True
while process != 'quit':
    process = input('>  What to do  ').lower()
    if process == 'start':
        if stopped:
            print('car started...')
            stopped = False
        else:
            print('car is already started...')
    elif process == 'stop':
        if stopped:
            print('car is already stopped')
        else:
            print('car stopped')
            stopped = True
    elif process == 'music':
        print("music player is ready to use")
    elif process == 'help':
        print(""" press
         'start button' to start the car
          'stop button' to stop the car AND
          'qd button' to open the doors.       
        """)
    elif process == 'qd':
        print('Door is open...')
    elif process != 'quit':
        print('your car is not understanding what you are saying')
else:
    print('car will get in lockdown mode in 3 minutes')
