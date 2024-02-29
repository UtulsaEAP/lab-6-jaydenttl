'''
Name: Jayden Ly
Lab Time: 2/29/24 2:32 PM
'''
def check_palindrome(user_input):
    checker = user_input
    reverse_input = checker[::-1]
    if reverse_input == checker:
        return
    else:
        return False

if __name__ == "__main__":
    user_input = input()

    if check_palindrome(user_input) == True:
        print('palindrome: ' + user_input)
    elif check_palindrome(user_input) == False:
        print('not a palindrome: ' + user_input)
