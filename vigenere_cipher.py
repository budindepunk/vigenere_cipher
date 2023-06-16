
alphabet = "abcdefghijklmnopqrstuvwxyz"
def vigenere_decode(message, keyword):
    keyphrase = ""
    decoded = ""
    i = 0
    for character in message:
        if character.isalpha():
            if i == len(keyword):
                i = 0
            keyphrase = keyphrase + keyword[i]
            i += 1
        else:
            keyphrase = keyphrase + character
    
    for i in range(0, len(message)):
        if message[i].isalpha():
            
            index_m = alphabet.find(message[i])
            index_k = alphabet.find(keyphrase[i])
            index_d = (index_m - index_k) % len(alphabet)
            char = alphabet[index_d]
            
            decoded = decoded + char
        else:
            decoded = decoded + message[i]
    print("the decrypted message is: " + decoded)

def vigenere_encode(message, keyword):
    keyphrase = ""
    encoded = ""
    i = 0
    for character in message:
        if character.isalpha():
            if i == len(keyword):
                i = 0
            keyphrase = keyphrase + keyword[i]
            i += 1
        else:
            keyphrase = keyphrase + character
    
    for i in range(0, len(message)):
        if message[i].isalpha():
            
            index_m = alphabet.find(message[i])
            index_k = alphabet.find(keyphrase[i])
            index_d = (index_m + index_k) % len(alphabet)
            char = alphabet[index_d]
            
            encoded = encoded + char
        else:
            encoded = encoded + message[i]
    print("the encrypted message is: " + encoded)

while True:
    task = input("what do you need to do? type 'e' for encryption, 'd' for decryption\n")
    if task.lower() not in ('d', 'e'):
        print("please type either 'e' or 'd'")
        continue
    else:
        break

message = input("message:\n")
keyword = input("keyword:\n")

if task == "d":
    vigenere_decode(message, keyword)
elif task == "e":
    vigenere_encode(message, keyword)