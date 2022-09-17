
secret_word = 'innovation'
user_guess = []
chances = 3

while True:
    letter = input('Enter a letter that you guess to be in the secret word: ')

    # Counting the chances left
    if chances <= 1:
        print('You lost!')
        break

    # Eliminating the chances of user inserting more than a letter at a time.
    if len(letter) > 1:
        print('Come on! Just guess one letter at a time!')
        continue

    # Eliminating the possibility of user entering a numeric value
    elif letter.isnumeric():
        print('You entered a number! Please enter an alphabet.')

    # What to do when the user inserts a letter
    if letter in secret_word:
        user_guess.append(letter)
        print(f'Uhuuu!! Good guess!! There is the letter {letter} in the secret word.')
    else:
        print(f'Ops!! There isn´t the letter {letter} in the secret word.')
        chances -= 1

    # Using for to print ****  and appear on the user interface
    temp_secret = ''

    for letter in secret_word:
        if letter in user_guess:
            temp_secret += letter

        else:
            temp_secret += '*'

    if temp_secret == secret_word:
        print(f'Congrats! You discovered the secret word {temp_secret}!')
        break
    else:
        print(f'The secret word is {temp_secret}')

    print(f'Chances left = {chances}')
