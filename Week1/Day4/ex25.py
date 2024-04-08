def break_words(stuff):
    """This Function will break up words for us. """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print (word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word =  words.pop(-1)
    print (word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
#chats in terminal
# python
# Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "all good things come to those who wait."
# >>> words = ex25.break_words(sentence) 
# >>> words
# ['all', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_word(words)
# all
# >>> ex25.print_last_word(words)  
# wait.
# >>> words 
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> ex25.print_first_word(sorted_words)
# all
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['all', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)  
# all
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)   
# all
# who
# >>> help(ex25)
# Help on module ex25:

# NAME
#     ex25

# FUNCTIONS
#     break_words(stuff)
#         This Function will break up words for us.

#     print_first_and_last(sentence)
#         Prints the first and last words of the sentence.

#     print_first_and_last_sorted(sentence)
#         Sorts the words then prints the first and the last one.

#     print_first_word(words)
#         Prints the first word after popping it off.

#     print_last_word(words)
#         Prints the last word after popping it off.

#     sort_sentence(sentence)
#         Takes in a full sentence and returns the sorted words.

#     sort_words(words)
#         Sorts the words.

# FILE
#     c:\users\lenovo\dei\day4\ex25.py



# >>> help(ex25.break_words)
# Help on function break_words in module ex25:

# break_words(stuff)
#     This Function will break up words for us.