import read
from collections import Counter

df = read.load_data()

words = ""
for i in df["headline"]:
    words+=str(i)+' '

print(Counter(words.lower().split()).most_common(100))
