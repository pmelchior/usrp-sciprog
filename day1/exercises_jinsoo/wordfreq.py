import re
import string
import sys
frequency = {}
document_text = open(sys.argv[1], 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

k1 = sorted(frequency, key=frequency.get, reverse=True)

for words in k1:
    print(words, frequency[words])
