#1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

word = "hello"
print(word.upper())

#2. Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(words, must_start_with=None):
    """
    Prints each word in the given list, in all uppercase, if it starts with any of the letters in the
    optional `must_start_with` parameter (or all words if `must_start_with` is not specified).
    """
    if must_start_with:
        words = [word for word in words if word[0].lower() in must_start_with]
    else:
        words = [word.upper() for word in words]
    for word in words:
        print(word)


#3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def print_upper_words(words):
    """
    Prints each word in the given list that starts with the letter 'e', in all uppercase.
    """
    for word in words:
        if word[0].lower() == 'e':
            print(word.upper())


#4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

