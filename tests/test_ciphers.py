from cipher.cipher_encrypt import caesar, vigenere

def test_caesar_encrypt_decrypt():
    text = "Hello, World!"
    encrypted = caesar(text, 3, 1)
    decrypted = caesar(encrypted, 3, -1)
    assert decrypted == text

def test_vigenere_encrypt_decrypt():
    text = "Attack at dawn!"
    key = "LEMON"
    encrypted = vigenere(text, key, 1)
    decrypted = vigenere(encrypted, key, -1)
    assert decrypted == text

def test_preserves_symbols():
    text = "123! @#?"
    encrypted = caesar(text, 5, 1)
    assert encrypted == text