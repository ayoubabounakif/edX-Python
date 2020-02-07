###### MY CODE ######
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

def encryption_decode(string):
    character_set_decode = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
    secret_key_decode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    encrypted_msg_decode = ""
    for x in string:
        index_decode = character_set_decode.find(x)
        encrypted_msg_decode += secret_key_decode[index_decode]
    return encrypted_msg_decode

y = input("Type the message you wanna decode:")
print (encryption_decode(y))
