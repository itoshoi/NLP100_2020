def cipher(string):
    result = ''
    for c in string:
        result += chr(219 - ord(c)) if c.islower() else c
    return result


encryption = cipher("Hello World !")
decryption = cipher(encryption)
print(encryption)
print(decryption)
