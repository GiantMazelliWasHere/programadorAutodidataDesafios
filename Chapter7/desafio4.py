list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    answer = input('Type a number between 1 - 10 or "q" to quit: ')
    if answer == 'q':
        break
    
    try:
        answer = int(answer)
    
    except ValueError:
        print('Please type a number or "q" to quit!')
    
    if answer in list:
        print('You guessed correctly!')
    else:
        print('You guessed incorrectly!')

