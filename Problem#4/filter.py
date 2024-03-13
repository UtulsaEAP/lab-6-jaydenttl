'''
Name: Jayden Ly
ssdaklfsj
Lab Time: 2/29/24 3:06 PM
'''
def process_and_print(input_string):
    # Split into separate strings
  all_num = input_string.split()
    # Convert strings to integers and filter out negative values
  int_num = list(map(int, all_num))
  neg_num = list(filter(lambda n: n < 0,int_num))
    # Sort integers in reverse order
  neg_num.sort(reverse=True)
    # Print sorted integers
  for value in neg_num:
    print(value, end=' ')         #PROPER PRINT LIST 
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
