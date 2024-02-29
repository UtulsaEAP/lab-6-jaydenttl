'''
Name: Jayden Ly
Lab Time: 2/29/24 2:52 PM
'''
def process_input(input_string):
      # Split into separate strings
  splitted = input_string.split(' ')
    # Convert strings to floats
  fsplitted = list(map(float, splitted))
    # Get max and average
  average_value = sum(fsplitted) / len(splitted)
  max_value = max(fsplitted)

  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
