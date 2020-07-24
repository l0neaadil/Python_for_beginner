# Guessing Game
Secret_No = 7
Guess_No = 0
Guess_Limit = 3
Attempts = 3
while Guess_No < Guess_Limit:
    Guess = int(input("Guess a No... "))
    Guess_No += 1
    if Guess == Secret_No:
        print('Your guess is right.You are a genius.')
        break
    else:
        Attempts -= 1
        if Attempts != 0:
            print(f'Your guess is wrong.Try again.(No of limits remained {Attempts})')
else:
    print('''Your guess is wrong and you have exceeded your limits.The secret no. was 7....''')
