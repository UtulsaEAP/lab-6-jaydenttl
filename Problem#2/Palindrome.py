'''
Name: Jayden Ly
s
Lab Time: 2/29/24 2:32 PM
'''
def check_palindrome(user_input):
    checker = user_input
    reverse_input = checker[::-1]
    if reverse_input == checker:
        print('palindrome: ' + user_input)
        
    else:
        print('not a palindrome: ' + user_input)
        

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
