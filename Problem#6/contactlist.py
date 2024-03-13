'''
Name: Jayden Ly

Lab Time: 3/7/24 12:13 PM
'''
def process_user_contacts(user_input):
    user_contacts = {}

    user_input = user_input.replace(" ", ",") # replace all space with comma

    split_input = user_input.split(',') # split by all commars
    # Put word pairs into a dictionary
    for i in range(0, len(split_input), 2):
        name = split_input[i]                   #first item is name
        phone_number = split_input[i + 1]       #item +1 so second item is phone
        user_contacts[name] = phone_number      #dictionary returns phone if u do this
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if contact_name in user_contacts:
        print(user_contacts[contact_name])          #FIYTB!!!
    else:
        print("Contact not found.")
    

    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
