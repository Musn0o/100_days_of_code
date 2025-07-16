import os

# Placeholder used in the letter template
PLACEHOLDER = "[name]"

# Try to open the names file and handle errors if the file is not found
try:
    with open("Day_024_Mail_Merge_Project/Input/Names/invited_names.txt") as names_file:
        names = names_file.readlines()
except FileNotFoundError:
    print("Error: 'invited_names.txt' not found.")
    names = []

# Try to open the letter template and handle missing file errors
try:
    with open(
        "Day_024_Mail_Merge_Project/Input/Letters/starting_letter.txt"
    ) as letter_file:
        letter_contents = letter_file.read()
except FileNotFoundError:
    print("Error: 'starting_letter.txt' not found.")
    letter_contents = ""

# Proceed only if both files were successfully read
if names and letter_contents:
    for name in names:
        stripped_name = name.strip()  # Remove whitespace and newline characters
        # Replace the placeholder with the actual name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Ensure the output directory exists
        output_dir = "Day_024_Mail_Merge_Project/Output/ReadyToSend"
        os.makedirs(output_dir, exist_ok=True)

        # Write the personalized letter to a new file
        try:
            with open(
                f"{output_dir}/letter_for_{stripped_name}.txt", mode="w"
            ) as completed_letter:
                completed_letter.write(new_letter)
        except IOError:
            print(f"Error writing file for {stripped_name}")
