def print_upper_words(words):
    """ all words caps """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """ words starting with e only"""
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words3(words, must_start_with):
    """ words starting with specific letter"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
        
    
