# Distance conversion
distance = float(input('Enter the distance (in kms) you want to convert:... '))
unit = input('''Enter 
  'm' [for meter] or 'c' [for centimeter]
   in which you want distance to be converted
   ''')
if unit.lower() == 'm':
    D = distance * 1000
    print(f'{distance} km = {D} m')
else:
    D = distance * 100000
    print(f'{distance} km = {D} cm')
