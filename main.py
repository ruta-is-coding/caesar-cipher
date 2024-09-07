from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    final_text = ""
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            final_text += letter
            continue

        original_index = alphabet.index(letter)
        new_index = original_index + shift_amount
        new_index %= len(alphabet)
        final_text += alphabet[new_index]

    print(f"Here is the {encode_or_decode}d result: {final_text}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction != 'encode' and direction != 'decode':
        print("\nWrong choice! Please type 'encode' or 'decode'.\n")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == 'yes':
        continue
    elif restart == 'no':
        break
    else:
        print("Wrong input choice!")
        break
