import nltk
from nltk.corpus import words


#helper function to turn letters to numbers
def convert_to_numb(str_of_words):
    numbers = []
    for letters in str_of_words:
        find_the_numb = ord(letters) - 96
        if find_the_numb <= 0:
            numbers.append(' ')
        else:
            numbers.append(find_the_numb)

    return numbers

#helper function to turn numbers to letters
def convert_to_words(str_of_numbs):
    num_to_letter = []
    finished_str = ""
    for number in str_of_numbs:
        if number == ' ':
            num_to_letter.append(' ')
        elif number == 0:
            num_to_letter.append(' ')
        else: 
            # run_it = str(number)
            char_num = number + 96
            find_the_letter = chr(char_num)
            num_to_letter.append(find_the_letter)
        
    for letters in num_to_letter:
        finished_str += letters

    return finished_str

#helper functions for multi word decryption & decryption without key
def multi_word_assist(sentence):
    split_it = sentence.split()
    for words in split_it:
        verify = check_words(words)
        if verify is True:
            continue
        else: 
            return False
    return True

def check_words(check_word):
    nltk.download('words', quiet=True)
    word_list = words.words()
    if check_word in word_list:
        return True
    else:
        return False









def encrypt (word, numb_shift):
    encrypt_text = []
    call_helper = convert_to_numb(word) 

    for number in call_helper: 
        if number == ' ':
            encrypt_text += (' ')
        elif number == 0:
            encrypt_text += (' ')
        else: 
            temp = int(number)
            temp2 = (temp + numb_shift) % 26
            encrypt_text.append(temp2)
        
    encrypt_helper = convert_to_words(encrypt_text)
    return encrypt_helper


def decrypt (encrypt_txt, numb_shift):
    decrypt_it = encrypt(encrypt_txt, -numb_shift)
    return decrypt_it


def crack (encrypt_txt):
    rounds = 26
    possible_words = []

    while rounds > 0:
        try_decrypting = decrypt(encrypt_txt, rounds)
        if len(try_decrypting) > 1:
            verify = multi_word_assist(try_decrypting)
        if verify is True:
            possible_words.append(try_decrypting)

        else:
            verify = check_words(try_decrypting)
        if verify is True:
            possible_words.append(try_decrypting)
        rounds -= 1

    if len(possible_words) == 0:
        print("No possible decryptions found")
        return "No possible decryptions found"
    elif len(possible_words) == 1:
        print(str(possible_words))
        return str(possible_words)
    else:
        print("Several possibilities found : ", str(possible_words))
        return ("Several possibilities found : ", str(possible_words))



if __name__=="__main__":
    print("ENCRYPT ONE", encrypt("hello", 1))
    # print("ENCRYPT BACK", encrypt("hello", 26))
    print("ENCRYPT WRAP 1", encrypt("hello", 53))
    # decrypt("jgtg ku c vjkpi", 2)
    # crack("jgtg ku c vjkpi")
