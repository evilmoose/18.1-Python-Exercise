def print_uppercase(words):

    for word in words:
        print(word.upper())

def print_uppercase(words):

    for word in words:
        if word.startswith("e") or word.startswisth("E"):
            print(word.upper())

def print_uppercase(words, starts_with):

    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
                break
          
print_uppercase(["hello", "hey", "goodbye", "yo", "yes"], starts_with={"h", "y"})