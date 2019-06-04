def alphabet_position(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    return alphabet.index(letter)

def rotate_character(char, rot):
    
    ordVal = ord(char)
    if ordVal<65 or (ordVal>90 and ordVal<97) or ordVal>122:
        return char
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
   
    rotate_character = alphabet_position(char) + rot
    encrypted = ''
    
    
    if rotate_character < 26:
        encrypted = alphabet[rotate_character]
    else:
        rotate_character = (alphabet_position(char) + rot) % 26
        encrypted = alphabet[rotate_character]
        
    if ordVal > 96:
        encrypted = encrypted.lower()
    else:
        encrypted = encrypted.upper()

    
    return encrypted