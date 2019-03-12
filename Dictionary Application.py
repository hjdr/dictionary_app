import json
from difflib import get_close_matches


dictionary_data = json.load(open("data.json"))

print(type(dictionary_data))


def dict_user_search_and_retrieve():
    user_input = input("Enter word to search for meaning: ").strip()
    while user_input not in dictionary_data.keys():
        possible_matches = get_close_matches(user_input, dictionary_data.keys(), n=1)
        if possible_matches:
            user_input_yn = input("Did you mean {}? (Enter Y/N) ".format(possible_matches[0])).upper().strip()
            if user_input_yn == "Y" or user_input_yn == "YES":
                output = "\n".join(str(item) for item in dictionary_data[possible_matches[0]])
                return output
            else:
                user_input = input("That word is not in the dictionary, try again: ").lower().strip()
        else:
            user_input = input("That word is not in the dictionary, try again: ").lower().strip()
    if user_input.lower() in dictionary_data:
        output = "\n".join(str(item) for item in dictionary_data[user_input])
        return output
    elif user_input.title() in dictionary_data:
        output = "\n".join(str(item) for item in dictionary_data[user_input])
        return output
    elif user_input.upper() in dictionary_data:
        output = "\n".join(str(item) for item in dictionary_data[user_input])
        return output


print(dict_user_search_and_retrieve())

