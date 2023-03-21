# Palindrome Reader
# ICS4U
# Park's Solution

with open("words.txt", "r") as data_file:
    # data_file variable is considered a file object
    # it represents the data read from words.txt

    our_text = data_file.read() # .read() is a file method that reads the contents of our file as a gigantic string
    our_text = our_text.split('\n') # .split() is a string method that helps to convert a large string into a list
    # .split('\n') is using '\n' as an indicator to split the strings
    # example 'hello\nworld'.split('\n') --> ['hello', 'world']

    for word in our_text: # this is a for loop that iterates through the our_text list
        # word will represent the words in our file one by one
      
        if word == word[::-1]: # [::-1] is a slicing/indexing hack in python to help us reverse any sliceable objects
            # as long as the word and the reversed version of the word are equal, the word itself will be a palindrome
            print(word, 'is a palindrome.')
