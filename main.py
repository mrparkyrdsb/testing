# Palindrome Finder

with open("words.txt", "r") as data_file:
    # data_file is not a string, but a file object
    #print(data_file)

    our_text = data_file.read()
    our_text = our_text.split('\n')
    #print(our_text)

    for word in our_text:
        #print(word)

        if word == word[::-1]:
            print(word,'is a palindrome.')