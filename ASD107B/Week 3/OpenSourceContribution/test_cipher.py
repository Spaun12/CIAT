
from Caesar_cipher import main  

def test_encrypt_known_input():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}  # Complete the key
    cipher = main(key)
    cipher.blank_string = "abc"  # Directly set the string to be encrypted
    result = cipher.encrypt_string()
    assert result == "def", f"Expected 'def', got '{result}'"

def test_decrypt_known_output():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}  # Complete the key
    cipher = main(key)
    result = cipher.decrypt_string("def")
    assert result == "abc", f"Expected 'abc', got '{result}'"

def test_encrypt_empty_string():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}  # Complete the key
    cipher = main(key)
    cipher.blank_string = ""
    assert cipher.encrypt_string() == '', "Expected empty string, got something else"

def test_decrypt_empty_string():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}  # Complete the key
    cipher = main(key)
    assert cipher.decrypt_string("") == '', "Expected empty string, got something else"

def test_non_alpha_characters():
    key = {"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}  # Complete the key
    cipher = main(key)
    cipher.blank_string = '123'
    assert cipher.encrypt_string() == '123', "Expected unchanged non-alpha string"
    assert cipher.decrypt_string('123') == '123', "Expected unchanged non-alpha string"

