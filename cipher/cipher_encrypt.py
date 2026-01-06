import string

UPPER_ALPHA = string.ascii_uppercase
LOWER_ALPHA = string.ascii_lowercase
ALPHABET_LEN = 26

def char_shift(char: str, offset: int, direction: int) -> str:
    if char in UPPER_ALPHA:
        i = UPPER_ALPHA.index(char)
        return UPPER_ALPHA[(i + offset * direction) % ALPHABET_LEN]
    if char in LOWER_ALPHA:
        i = LOWER_ALPHA.index(char)
        return LOWER_ALPHA[(i + offset * direction) % ALPHABET_LEN]
    return char

def caesar(message: str, shift: int, direction: int) -> str:
    return ''.join(char_shift(c, shift, direction) for c in message)

def vigenere(message: str, key: str, direction: int) -> str:
    if not key.isalpha():
        raise ValueError('Key must contain letters only.')
    
    result = []
    key = key.lower()
    ki =0

    for char in message:
        if char.isalpha():
            offset = ord(key[ki % len(key)]) - ord('a')
            result.append(char_shift(char, offset, direction))
            ki += 1
        else:
            result.append(char)
    return ''.join(result)

def main():
    print("\n=== Cipher CLI Menu ===")
    print("1) Encrypt with Caesar")
    print("2) Decrypt with Caesar")
    print("3) Encrypt with Vigenere")
    print("4) Decrypt with Vigenere")
    print("0) Exit")

    choice = input("Select an option: ")

    message = input("Enter message: ")

    if choice in {"1", "2"}:
        shift = int(input("Enter shift: "))
        direction = 1 if choice == "1" else -1
        print(caesar(message, shift, direction))
    
    elif choice in {"3", "4"}:
        key = input("Enter key (letters only): ")
        direction = 1 if choice == "3" else -1
        print(vigenere(message, key, direction))

    elif choice == "0":
        print("\n\n~~Goodbye!~~")
        exit()

    else:
        print("[!] Invalid Option.")


if __name__ == "__main__":
    main()

