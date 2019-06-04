from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted += ' '
        else:
            encrypted += rotate_character(char, rot) 
    return encrypted
    


def main():
    text = input("Type a message:")
    rot = int(input("Rotate by:"))
    print (encrypt(text,rot))

if __name__ == "__main__":
    main()