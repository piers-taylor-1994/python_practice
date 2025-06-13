alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
_text = input("Type your message:\n").lower()
_shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(direction, text, shift):
    if direction == "encode":
        output = ""
        for letter in text.lower():
            if letter in alphabet:
                index = alphabet.index(letter) + shift
                index = index % len(alphabet)
                output += alphabet[index]
            else:
                output += letter
        print(output)
    else:
        output = ""
        for letter in text.lower():
            if letter in alphabet:
                index = alphabet.index(letter) - shift
                index = index % len(alphabet)
                output += alphabet[index]
            else:
                output += letter
        print(output)
caesar(_direction, _text, _shift)