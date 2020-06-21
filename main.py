from encryption import encryption
from decryption import decryption
import time


while True:
    try:
        sentence = input('Please input your sentence: ')
    except:
        print('\nProgram Interrupted by Ctrl + C!')
        break
    if sentence == 'q':
        print('\nExited!')
        break
    elif '=' in sentence:
        print('Decrypting···')
        time.sleep( 1 )
        print('Decrypting······')
        decryption(sentence)
    else:
        encryption(sentence)


#keywords[key] = keywords.get(key, 0)
