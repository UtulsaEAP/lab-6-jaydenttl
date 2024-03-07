'''
Name: Jayden Ly
s
Lab Time: 2/29/24 2:14 PM
'''
def food_input():
    user_input = input()
    tokens = user_input.split()
    while (user_input != "quit 0"):
        print('Eating ' + tokens[1] + ' ' + tokens[0] +' a day keeps you happy and healthy.')
        
    

if __name__ == "__main__":
    food_input()
