# Conversion of digits in words
Number = input("enter the no  ")
Dict = {
    '1': 'one',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '9': 'nine'
}
output = ''
for digit in Number:
    output = output + Dict.get(digit, "----") + '    '
    # output = output + Dict.get(digit,digit) + '    '
print(output)
