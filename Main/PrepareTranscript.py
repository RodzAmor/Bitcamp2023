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

charCount = 0
batchCount = 0
batches = []
with open('test_transcript.txt', 'r') as f:
    lines = f.readlines()
    currentBatch = []
    for line in lines:
        charCount += len(line)
        currentBatch.append(line)
        if (charCount >= 4000):
            fname = 'batch' + str(batchCount) + '.txt'
            batches.append(fname)
            with open(fname, 'w') as batch:
                batch.writelines(currentBatch)                    
            # reset the count and current batch list for the next batch
            currentBatch.clear()
            charCount = 0
            batchCount += 1


print(charCount)
