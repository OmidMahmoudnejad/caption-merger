import re

# Read files with Unicode support
with open('file1.txt', 'r', encoding='utf-8') as f1, open('file2.txt', 'r', encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

# Filter lines from file2 to include only non-number starting lines
filtered_lines2 = [line.strip() for line in lines2 if not re.match(r'^\d', line) and line.strip()]

# If file2 has no valid lines, set it to an empty list
if not filtered_lines2:
    filtered_lines2 = [""]

# Prepare the updated content for file1
updated_lines = []
file2_index = 0  # To cycle through file2 lines if needed

for line in lines1:
    updated_lines.append(line.strip())  # Add the original line
    if not re.match(r'^\d', line) and line.strip():  # Check if the line is a non-empty text line
        # Append a line from file2 under the current line
        updated_lines.append(filtered_lines2[file2_index % len(filtered_lines2)])
        file2_index += 1

# Save the updated content to a new file named output.txt
with open('output_caption_merger.txt', 'w', encoding='utf-8') as output_file:
    output_file.write("\n".join(updated_lines).strip() + "\n")

print("File updated successfully. The updated content has been saved to 'output.txt'.")