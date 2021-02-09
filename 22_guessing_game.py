# Guessing Game
secret_No = 7
guess_No = 0
guess_Limit = 3
attempts = 3
while guess_No < guess_Limit:
    guess = int(input("Guess a No...> "))
    guess_No += 1
    if guess == secret_No:
        print('Your guess is right. You are a genius.')
        break
    else:
        attempts -= 1
        if attempts != 0:
            print(f'Your guess is wrong. Try again.(No of limits remained = {attempts})')
else:
    print('''Your guess is wrong and you have exceeded your limits.The secret no. was 7....''')
