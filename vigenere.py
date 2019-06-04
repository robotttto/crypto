from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    message = ''    
    index = 0
    for char in text:

        rotation = alphabet_position(key[index])
        ordVal = ord(char)
        
        if ordVal<65 or ordVal>90 and ordVal<97 or ordVal>122:
            message += char
        if ordVal<65 or ordVal>90 and ordVal<97 or ordVal>122:
            index -= 1

        else:            
            message += rotate_character(char, rotation)           

        if index == (len(key) - 1): 
            index = 0
        else: 
            index += 1

    return message    

def main():
    text = input("Type a message:")
    key = input("Encryption key:")
    print (encrypt(text,key))

if __name__ == "__main__":
    main()


