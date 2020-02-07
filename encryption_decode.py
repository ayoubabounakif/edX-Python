def my_encryption(string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    encrypted_msg = ""
    for i in string:
        index = character_set.find(i)
        encrypted_msg += secret_key[index]

    return encrypted_msg

x = input("Please type your message: ")
print (my_encryption(x))


def my_encryption_decode(string):
    character_set = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    secret_key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    decrypted_msg = ""
    for i in string:
        inedx = character_set.find(i)
        decrypted_msg += secret_key[inedx]

    return decrypted_msg

y = input("TYpe the crypted message:")
print (my_encryption_decode(y))
