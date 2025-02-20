# single_letter_count
# Write a function called single_letter_count. This function takes in two parameters (two strings). The first parameter should be a word and the second should be a letter. The function returns the number of times that letter appears in the word. The function should be case insensitive (does not matter if the input is lowercase or uppercase). If the letter is not found in the word, the function should return 0.  

# Hint: take advantage of count() method

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())