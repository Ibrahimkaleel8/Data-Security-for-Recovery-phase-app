def algo1_encrypt(input_s):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ! @#$%&abcdefghijklmnopqrstuvwxyz'
    shift_input = 32
    length = len(input_s)
    string_encrypted = ""

    for i in range(length):
        character = input_s[i]
        loc_of_characters = alphabets.find(character)
        new_loc = (loc_of_characters + shift_input) % 58  # shifting values from remainders
        string_encrypted += alphabets[new_loc]

    return string_encrypted

def algo1_decrypt(input_s):
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ! @#$%&abcdefghijklmnopqrstuvwxyz'
    shift_input = 32
    length = len(input_s)
    string_decrypted = ""

    for i in range(length):
        character = input_s[i]
        loc_of_characters = alphabets.find(character)
        new_loc = (loc_of_characters - shift_input) % 58  # shifting values from remainders
        string_decrypted += alphabets[new_loc]
    return string_decrypted

if __name__ == "__main__":
    input_s = input("string: ")
    string_encrypted = algo1_encrypt(input_s)
    string_decrypted = algo1_decrypt(string_encrypted)
    print("encrypted strings: ", string_encrypted)
    print("decrypted strings: ", string_decrypted)
