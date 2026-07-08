# Standard approach:

string_ = input("Enter string: ").lower()
updated_string = ""

for index, char in enumerate(string_):
    if(index % 2 == 0):
        updated_string += char.upper()
    else:
        updated_string += char

print(updated_string)


# List comprehension approach:

string_ = input("Enter String: ").lower()

updated_string = "".join([char.upper() if(index % 2 == 0) else char for index, char in enumerate(string_)])

print(updated_string)