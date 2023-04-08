import re

pattern = r'\b(?:\d{1,2}:)?(?:\d{1,2}:)?\d{1,2}\b'

with open('test_transcript.txt', 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if re.match(pattern, line.strip()):  # remove line if only timestamp
        continue
    else:
        new_lines.append(re.sub(pattern, '', line))  # remove timestamp only

with open('test_transcript.txt', 'w') as f:
    f.writelines(new_lines)