from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
running = True


def caesar(start_text, shift_amount, cipher_direction):
  cipher_text = ""
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      if cipher_direction == "encode":
        position += shift_amount
      elif cipher_direction == "decode":
        position -= shift_amount
      cipher_text += alphabet[position]
    else:
      cipher_text += char
  print(f"The {cipher_direction}d text is {cipher_text}")


print(logo)
while running:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift %= 26
  caesar(text,shift,direction)
  again = input("Run again? type Yes or No:\n").lower()
  if again == "no":
    running = False
    print("Have a lovely day.")
