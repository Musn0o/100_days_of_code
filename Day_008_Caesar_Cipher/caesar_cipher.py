# List containing all lowercase English alphabet letters.
# This list is doubled to simplify wrapping around the alphabet (e.g., 'z' shifted by 1 becomes 'a').
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Cipher ASCII Art Logo
# This logo is displayed at the start of the program for visual appeal.
logo = """
  _ __  _ __
 | '_ \\| '_ \\
 | |_) | |_) |
 | .__/| .__/
 |_|   |_|

"""
print(logo)

# Define the caesar function which handles both encoding and decoding.
# It takes the plain text/cipher text, shift amount, and direction (encode/decode) as input.
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    # If the direction is 'decode', reverse the shift amount.
    # This makes the single function work for both operations.
    if cipher_direction == "decode":
        shift_amount *= -1

    # Iterate through each character in the input text.
    for char in start_text:
        # Check if the character is an alphabet letter.
        if char in alphabet:
            # Find the current position of the letter in the alphabet list.
            position = alphabet.index(char)
            # Calculate the new position after shifting.
            # Using modulo 26 ensures the shift wraps around the alphabet (0-25).
            new_position = (position + shift_amount) % 26
            # Append the letter at the new position to the end_text.
            end_text += alphabet[new_position]
        else:
            # If the character is not a letter (e.g., space, number, symbol),
            # append it directly to the end_text without shifting.
            end_text += char
    # Print the final encoded or decoded result.
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Main program loop: allows the user to run the cipher multiple times.
should_continue = True
while should_continue:
    # Get user input for direction (encode/decode).
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Get user input for the message.
    text = input("Type your message:\n").lower()
    # Get user input for the shift number.
    shift = int(input("Type the shift number:\n"))

    # Call the caesar function with the collected inputs.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to run the program again.
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")

