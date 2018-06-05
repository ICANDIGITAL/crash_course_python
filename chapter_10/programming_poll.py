filename = 'programming_poll.txt'
#User input prompts.
prompt = '\nPlease, enter the primary reason why you enjoy programming.\n'
prompt += 'Enter \'q\' to quit: '
"""
A "While Loop" that asked users for the most significant reason 
that they like programming and stores the information in a separate .txt file.
"""
while True:
    response = input(prompt)
    if response == 'q':
        break
    else:
        print("Thank You! For your response.")
        with open(filename, 'a') as file_object:
            file_object.write(response)