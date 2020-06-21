import time
import hashlib
import random

# Random a letter
def random_letter():
    letter = chr(random.randint(97, 122))
    return letter

# Encryption method
def encryption(sentence):

    current_time = time.strftime("%d%m%Y%H%M") # Get a timestamp
    keys = hashlib.md5(current_time.encode()).hexdigest() # Encrypt timestamp using MD5

    # Create a alphabet sequence
    passbook = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,'0': 0,'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}
    keywords = list()

    # Use MD5 to generate first part of the passbook
    for key in keys:
        if key in keywords:
            continue
        else:
            keywords.append(key)
    ori = len(keywords)

    # Generate rest of numbers and letters in a sequence uniquely
    while True:
        if len(keywords) == 36: break

        # Generate random letter uniquely
        add_letter = random_letter()
        if add_letter in keywords:
            continue
        else:
            keywords.append(add_letter)

        # Generate random number uniquely
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for num in numbers:
            if num in keywords:
                continue
            else:
                keywords.append(num)

    # Generate a new passbook
    index = 0
    for key in passbook:
        passbook[key] = keywords[index]
        index = index + 1
    passbook[' '] = '='

    # Process characters
    characters = list()
    for character in sentence:
        characters.append(character)

    # Encrypting character
    encrypted = list()
    try:
        for character in characters:
            encr = passbook[character]
            encrypted.append(encr)
        encrypted_sentence = "".join(encrypted)

        # Output encrypted sentence
        suffix = 36 - int(ori)
        suffix = 36 - suffix
        suffix = keywords[suffix:]
        suf = "".join(suffix)

        if len(encrypted_sentence) < 1:
            print('Nothing Found!')
        else:
            print(encrypted_sentence + '=' + current_time + '=' + suf)

    except:
        print('\nInvaild input!\nFor example: hey how are you doing mate')

#keywords[key] = keywords.get(key, 0)
