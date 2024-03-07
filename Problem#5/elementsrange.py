'''
Name: Jayden Ly

Lab Time: 2/29/24 5:30 PM
'''
def filter_and_print_range(integer_list, min_val, max_val):
    #write your code here


    filtered_list = list(filter(lambda n: min_val <= n <= max_val, integer_list))
    restr_list = list(map(str, filtered_list))
    comma_list = []
    for _ in range(len(restr_list)):
        comma_list += ','

    list_w_comma = [restr_list+comma_list for restr_list, comma_list in zip(restr_list, comma_list)]
    print(''.join(map(str,list_w_comma)))
    


if __name__ == "__main__":
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = list(map(int, user_input.split()))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = list(map(int, (user_input.split())))

    filter_and_print_range(integer_list, min_val, max_val)

    # Call the function to filter and print the numbers in the given range
   
