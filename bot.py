import re


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('There isn\'t contact with this name.')
        except ValueError:
            print('Please enter the correct format of name and phone number. Correct format:\n1. The length of the nunber must be a 12 digits.\n2. Use a gap between name and number.')
    return wrapper

@input_error
def add_contact(user_input, name_number_dict):
    match = re.match(r'add (\w+) (\d{12})', user_input)
    if match:
        name = match.group(1)
        number = match.group(2)
        name_number_dict[name] = number
        print(f'Contact {name} has been added.')
    else:
        raise ValueError

@input_error
def show_contact(name_number_dict):
    if name_number_dict:
        for name, number in name_number_dict.items():
            print(f'{name} - {number}')
    else:
        print('There are any contacts.')

@input_error
def find_number(user_input, name_number_dict):
    match = re.match(r'phone (\w+)', user_input)
    if match:
        name = match.group(1)
        phone_number = name_number_dict[name]
        print(f'{name} - {phone_number}')
    else:
        raise KeyError

@input_error
def change_the_number(user_input, name_number_dict):
    match = re.match(r'change (\w+) (\d{12})', user_input)
    if match:
        old_name = match.group(1)
        new_number = match.group(2)
        if old_name in name_number_dict:
            name_number_dict[old_name] = new_number
            print(f'Phone number for {old_name} has been changed to {new_number}.')
        else:
            print(f'There isn\'t contact for "{old_name}".')
    else:
        raise ValueError

def main():
    print('What can this bot do?\n1. Save the contact (name and phone number). Please, remember: number - only 12 digits. Use command: add [name] [number]\n2. Change the phone number of the recorded contact. Please, remember: number - only 12 digits. Use command: change [name] [new_number]\n3. Search for the phone number of the specified contact. Use command: phone [name]\n4. Show all previously saved contacts. Use command: show all.')
    name_number_dict = {}
    while True:
        user_input = input('>>> ')
        if user_input.lower() == 'hello':
            print('How can I help you?')
        elif user_input.lower().startswith('add'):
            add_contact(user_input, name_number_dict)
        elif user_input.lower().startswith('change'):
            change_the_number(user_input, name_number_dict)
        elif user_input.lower().startswith('phone'):
            find_number(user_input, name_number_dict)
        elif user_input.lower() == 'show all':
            show_contact(name_number_dict)
        elif user_input.lower() in ['exit', 'close', 'good bye']:
            print('Good bye!')
            raise SystemExit
        else:
            print('Sorry, but I don\'t understand what are you talking about.')

main()