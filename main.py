#This is a text encryption-decryption program Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        original_index = alphabet.index(letter)
        new_index = original_index + shift_amount
        new_index %= len(alphabet)

        encrypted_text += alphabet[new_index]
    print(f"Here is the encoded result: {encrypted_text}")


encrypt(original_text=text, shift_amount=shift)
