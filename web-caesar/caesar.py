def alphabet_position(letter):
    letter = ord(letter)
    if letter > 64 and letter < 91:
        letter = letter - 65
        return letter
    elif letter> 96 and letter < 123:
        letter = letter - 97
        return letter


def rotate_character(char, rot):
    char = ord(char)
    if char > 64 and char < 91:
        char = ((char - 65) + rot) % 26
        return chr(char + 65)
    elif char > 96  and char < 123:
        char = ((char - 97) + rot) % 26
        return chr(char + 97)
    else:
        return chr(char)


def encrypt(text, rot):

        new_str = ""
        rot = int(rot)
        for letter in text:
            # print(letter)
            new_letter = rotate_character(letter, rot)
            new_str += new_letter
        return new_str


def main():
    message = input("Please enter message to encrypt")
    key = input("Please enter a positive numeric key")
    print(encrypt(message, key))
    if __name__ == "__main__":
        main()
