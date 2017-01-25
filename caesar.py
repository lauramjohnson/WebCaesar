
def alphabet_position(letter):
    alpha =  "abcdefghijklmnopqrstuvwxyz"
    alpha_pos = alpha.find(letter.lower())
    return alpha_pos

def rotate_character(char, rot):
    alpha =  "abcdefghijklmnopqrstuvwxyz"
    new_letter = alpha[(alphabet_position(char) + rot) % 26]
    if char.isupper():
        new_letter = new_letter.upper()
    elif not char.isalpha():
        new_letter = char
    return new_letter

def encrypt(text, rot):
    encrypted = ""
    for letter in text:
        encrypted = encrypted + rotate_character(letter,rot)
    return encrypted
