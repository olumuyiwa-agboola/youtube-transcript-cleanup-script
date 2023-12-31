import re
import sys

if len(sys.argv) != 2:
    print("Usage: python ./transcripts-cleanup.py name_of_transcript ...")
    sys.exit(1)  # Exit with an error code

# Access command line arguments
script_name = sys.argv[0]
name_of_transcript = sys.argv[1]

print(f"Script name: {script_name}")
print(f"Arguments: {name_of_transcript}")

def remove_timestamps(text):
    # define regex pattern to match timestamps
    timestamp_pattern = re.compile(r'\d+:\d+')

    # replace timestampswith an empty string
    cleaned_text = re.sub(timestamp_pattern, '', text)

    return cleaned_text

def remove_line_breaks(text):
    # define regex pattern to match line break
    line_break_pattern = re.compile(r'\n')

    # replace timestamps, empty lines and line breaks with an empty string
    cleaned_text = re.sub(line_break_pattern, '', text)

    return cleaned_text

def clean_text(text):
    return remove_timestamps(remove_line_breaks(text))


def convert_to_multiline_string(text, words_per_line=10):
    # split text into words
    words = text.split()

    # wrap the words into lines
    lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]

    multiline_string = '\n'.join(lines)

    return multiline_string

original_text = './original/' + name_of_transcript + '.txt' 
with open(original_text, 'r') as file:
    content = file.read()

cleaned_text = './cleaned/' + name_of_transcript + '.txt'
with open(cleaned_text, 'w') as file:
    # Write the text to the file
    file.write(convert_to_multiline_string(clean_text(content)))