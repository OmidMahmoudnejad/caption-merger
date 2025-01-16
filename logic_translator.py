import re
import asyncio
from googletrans import Translator

# Initialize the translator with a longer timeout
translator = Translator(timeout=10)

# Read files with Unicode support
with open('file3.txt', 'r', encoding='utf-8') as f2:
    lines2 = f2.readlines()

# Filter lines from file2 to include only non-number starting lines
filtered_lines2 = [line.strip() for line in lines2 if not re.match(r'^\d', line) and line.strip()]

# If file2 has no valid lines, set it to an empty list
if not filtered_lines2:
    filtered_lines2 = [""]

# Async function to translate lines
async def translate_lines(lines):
    translated_lines = []
    for line in lines:
        try:
            translation = await translator.translate(line, src='en', dest='fa')
            translated_text = translation.text
        except Exception as e:
            print(f"Error translating line '{line}': {e}")
            translated_text = line  # Use original text in case of error
        translated_lines.append(translated_text)
        # Print translated line to terminal
        print(f"Translated: {translated_text}")
        # Print the original line under the translated one
        print(f"Original: {line}")
        # Print an extra newline in terminal
        print()

    return translated_lines

# Run the translation asynchronously
async def main():
    translated_lines = await translate_lines(filtered_lines2)

    # Prepare the updated content using translated lines
    updated_lines = []
    for idx, line in enumerate(translated_lines):
        updated_lines.append(line)  # Add the translated line
        updated_lines.append(filtered_lines2[idx])  # Add the original line under the translated one
        # Append an extra newline after each pair of translated and original lines
        updated_lines.append("")

    # Save the updated content to a new file named output.txt
    with open('output_translator_3.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("\n".join(updated_lines).strip() + "\n")

    print("File updated successfully. The updated content has been saved to 'output.txt'.")

# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())