run = True
while run:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar():
        if direction == "encode":
            encrypt()
    # TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
    def encrypt(original_text: str, shift_amount: int):
        output = ""
        for letter in original_text.lower():
            if letter in alphabet:
                index = alphabet.index(letter) + shift_amount
                index = index % len(alphabet)
                output += alphabet[index]
            else:
                output += letter
        print(output)


    def decrypt(original_text: str, shift_amount: int):
        output = ""
        for letter in original_text.lower():
            if letter in alphabet:
                index = alphabet.index(letter)
                index -= shift_amount
                if index < 0:
                    index -= 1
                print(index)
                output += alphabet[index]
            else:
                output += letter
        print(output)


    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.

    # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

    # TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
    #  message.
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Sorry, that is not a valid input")