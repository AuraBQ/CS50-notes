def main():
    camel = input("camelCase: " )
    # Prints the camel input as 'snake_case: [input]', ends on a new line.
    print('snake_case: ', end='')
    # Converts to snake case, separating all words by underscores and making them lowercased.
    snake = convert(camel)

# str.isupper() method returns True if all the characters are in upper case, otherwise False.
def convert(camel):
    # Uses for loop on the camel input, character represents each character in our input.
    for character in camel:
        # If all letters in the input are capital, separate them by an _ and lowercase the string. Ends the line.
        if character.isupper():
            print('_' + character.lower(), end='')
        else:
            # If the letters in the string are not all capitalized, prints every individual letter and ends on a new line, not separated by underscores.
            print(character, end='')


main()
