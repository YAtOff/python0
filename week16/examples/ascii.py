import string

print("ASCII table")
for i in range(128):
    string_value = chr(i)

    if string_value in string.whitespace:
        print(i, "WHITESPACE")
    elif string_value in string.ascii_letters:
        print(i, string_value, "ASCII_LETTER")
    elif string_value in string.punctuation:
        print(i, string_value, "PUNCTUATION")
    elif string_value in string.digits:
        print(i, string_value, "DIGIT")
    else:
        # Assume others are control characters.
        print(i, "CONTROL")

print("Alphabet")
for c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
    print(c, ord(c))
