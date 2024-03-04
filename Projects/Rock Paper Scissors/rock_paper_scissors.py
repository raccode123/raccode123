def main():
    '''
    _summary_ Pythonic Rock, Paper, Scissors game. 
    
    
    '''
    #import modules
    import random as rd
    
    #define wins in tuple
    wins = (('rock', 'scissors'),
        ('scissors', 'paper'),
        ('paper', 'rock'))

    #define variables
    choices = ('rock', 'paper', 'scissors')
    cpu_score = 0
    user_score = 0
    round_counter = 0
    
    #print welcome message
    print('\n----Welcome to python Rock, Paper, Scissors----')
    print('\nRules: First to five wins, wins!')
    
    while cpu_score < 5 and user_score < 5:
        # Print choices
        print(f'\nChoose from: {", ".join(choices)}\n')
        
        # Get players input
        user_input = input('Enter choice: ').lower()
        
        # Generate random choice for CPU 
        cpu_input = choices[rd.randint(0,2)]
        
        # Check if user's choice is valid
        if user_input not in choices:
            print("\nInvalid choice. Try again.")
            continue
        
        # Print round banner and users choice
        round_counter += 1
        print(f'\n----ROUND {round_counter}----\n')
        print(f'\nUSER: {user_input.upper()} | CPU: {cpu_input.upper()}')
        
        # Determine the winner
        if user_input == cpu_input:
            print('\nRESULT: DRAW')      
        elif (user_input, cpu_input) in wins:
            user_score += 1
            print('\nRESULT: USER WINS!')
        else:
            cpu_score += 1
            print('\nRESULT: CPU WINS!')
        
        # Display scores
        print(f'\nUSER SCORE: {user_score} | CPU SCORE: {cpu_score}')
                    

    
    # Print final round banner and scores        
    print(f'\n----FINAL SCORES----')
    print(f'\nUSER: {user_score} | CPU: {cpu_score}')
    
    # Determine overall score
    if user_score > cpu_score:
        print('\nUSER WINS!!!!!!!!!!!\n')
    else:
        print('\nCPU WINS!!!!!!!!!!!!\n')
        
if __name__ == '__main__':
    main()