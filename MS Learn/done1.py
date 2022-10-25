

user_input = ''


inputs = []


while user_input.lower() != 'done':
    
    if user_input:
        inputs.append(user_input)
        print(f"You have entered: {inputs} correct?")
        
    user_input = input('Enter a new value, or done when done: ')