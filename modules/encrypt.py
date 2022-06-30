

def encrypt(text,s):
    """
    Encrypt a string using Caesar Cipher.

    Params:
    text: Text to be encrypt.
    s: Integer denoting the required shift.

    Returns:
    the encrypted text.
    """
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt numeric characters
        elif (char.isnumeric()):
            result += chr((ord(char) + s - 48) % 10 + 48)

        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        
        # If that character is not a character or not a number
        else:
            result += char
 
    return result

def decrypt(text,s):
    """
    Decrypt a string using Caesar Cipher.

    Params:
    text: Text to be decrypt.
    s: Integer denoting the required shift.

    Returns:
    the decrypted text.
    """
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Decrypt numeric characters
        elif (char.isnumeric()):
            result += chr((ord(char) - s - 48) % 10 + 48)

        # Decrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) - s - 97) % 26 + 97)

        # If that character is not a character or not a number
        else:
            result += char
 
    return result
