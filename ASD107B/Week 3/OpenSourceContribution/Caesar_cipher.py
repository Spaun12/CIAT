class main: 
    def __init__(self,key:dict) -> None:
        self.key = key

    def get_input(self) -> None: 
        while True:
            blank_string = str(input("Enter string to decrypt: "))
            if blank_string.isalpha():
                blank_string = blank_string.lower()
                self.blank_string = blank_string
                break
            else:
                print("Input is not valid")
                continue

    def encrypt_string(self) -> str:
        output = ""
        for c in self.blank_string:
            output += self.key.get(c, c)  # Append the character directly if it's not in the key
        self.decrypted_string = output
        return output

    def decrypt_string(self, string: str) -> str:
        output = "" 
        string = string.lower()
        string = string.strip()
        if string == "":
            return ""  # Return empty string directly
        else: 
            for c in string:
                # Check if the character is in the values of the key dictionary
                if c in self.key.values():
                    # Find the key corresponding to the value and append it
                    output += [k for k, v in self.key.items() if v == c][0]
                else:
                    # If the character is not in the values, append it as is
                    output += c
        return output

if __name__ == "__main__":
    key ={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    main = main(key=key)
    main.get_input()
    print(main.encrypt_string())
