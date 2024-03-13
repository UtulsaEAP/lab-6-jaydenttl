'''
Name: Jayden Ly
Lab Time: 2/29/24 2:14 PM
'''
def food_input():
    while True:
        user_input = input()
        tokens = user_input.split()
        if (user_input != 'quit 0'):
            print ('Eating '+ tokens[1]+ ' '+tokens[0]+ ' a day keeps you happy and healthy.')
        else:
            break
    '''while True:
        user_input = input()
        tokens = user_input.split()
        if (user_input != 'quit 0'):
            print('Eating ' + tokens[1] + ' ' + tokens[0] +' a day keeps you happy and healthy.')
        else:
            False'''
        
    
if __name__ == "__main__":
    food_input()
