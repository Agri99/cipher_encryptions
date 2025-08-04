upp_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_alpha = "abcdefghijklmnopqrstuvwxyz"

def char_shift(char, offset, direction):
    if char.isupper():
        index = upp_alpha.find(char)
        new_index = (index + offset * direction) % len(upp_alpha)
        return upp_alpha[new_index]
    elif char.islower():
        index = low_alpha.find(char)
        new_index = (index + offset * direction) % len(low_alpha)
        return low_alpha[new_index]
    else:
        return char

def caesar(message, key):
    final_message = ""
    if not isinstance(key, int):
        raise ValueError("[!] Key must be integer!")
    for char in message:
        final_message += char_shift(char, key, 1)
    return final_message

def vigenere(message, key, direction):
    final_message = ""
    if not isinstance(key, str):
        raise ValueError("[!] The key must be string")
    key = ''.join([char for char in key if char.isalpha()]).lower() # Sanitize to letter
    key_index = 0
    for char in message:
        if char.isalpha:
            new_key = key[key_index % len(key)]
            offset = low_alpha.find(new_key)
            final_message += char_shift(char, offset, direction)
            key_index += 1
        else:
            final_message += char
    return final_message

def run_test():
    print("Running Test...")

    assert caesar("abc", 1) == "bcd", "Caesar Basic Shift Failed"
    assert caesar("ABC", 2) == "CDE", "Caesar Uppercase Failed"
    assert caesar("xyz", 3) == "abc", "Caesar Wrap-around Failed"

    encrypted = vigenere("Hello World!", "Python", 1)
    expected = "Wcesc Lmksr!"
    assert encrypted == expected, f"Vigenere Encryption Failed: {encrypted} != {expected}"

    decrypted = vigenere(encrypted, "Python", -1)
    assert decrypted == "Hello World!", f"Vigenere Decryption Failed: {decrypted} != Hello World!"

    print("[!] All Test Passed!")

def cli_menu():
    print("\n=== Cipher CLI Menu ===")
    print("1) Encrypt with Caesar")
    print("2) Decrypt with Caesar")
    print("3) Encrypt with Vigenere")
    print("4) Decrypt with Vigenere")
    print("0) Exit")
    choice = input("Select an option:")

    if choice == "1":
        text = input("Enter text to encrypt: ")
        key = int(input("Enter Caesar key(integer): "))
        print("\n---Encrypted:", caesar(text, key))
    elif choice == "2":
        text = input("Enter text to decrypt: ")
        key = int(input("Enter Caesar key(ineteger): "))
        print("\n---Decrypted:", caesar(text, -key))
    elif choice == "3":
        text = input("Enter text to encrypt: ")
        key = input("Enter Vigenere key(letter only): ")
        print("\n---Encrypted:", vigenere(text, key, 1))
    elif choice == "4":
        text = input("Enter text to decrypt: ")
        key = input("Enter Vigenere key(letter only): ")
        print("\n---Decrypted:", vigenere(text, key, -1))
    elif choice == "0":
        print("\n\n~~Goodbye!~~")
        exit()
    else:
        print("[!] Invalid Option.")


if __name__ == "__main__":
    run_test()
    while True:
        cli_menu()

