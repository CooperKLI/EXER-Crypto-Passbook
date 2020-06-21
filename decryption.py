import hashlib

def decryption(sentence):
    desentence = sentence.split('=')

    # Get method value
    length = len(desentence)
    timestamp = int(length) - 2
    timestamp = desentence[timestamp]
    random_key = int(length) - 1
    random_key = desentence[random_key]
    content = int(length) - 2
    content = desentence[:content]

    #Identify timestamp use MD5
    time_key = hashlib.md5(timestamp.encode()).hexdigest()

    passbook = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,'0': 0,'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0}
    keywords = list()

    #ReCreate Passbook
    for key in time_key:
        if key in keywords:
            continue
        else:
            keywords.append(key)
    for key in random_key:
        keywords.append(key)

    #RePair Passbook
    index = 0
    for k,v in passbook.items():
        passbook[k] = keywords[index]
        index = index + 1
    passbook[' '] = '='

    #Decrypting
    complete_sentence = list()
    sentence = "=".join(content)
    for character in sentence:
        for k,v in passbook.items():
            if character == v:
                complete_sentence.append(k)
            else:
                continue
    completed = "".join(complete_sentence)

    print(completed)
