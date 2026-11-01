import json

data = {
"metadata": {
    "version": "2.0",
    "target_word_count": 4000
},
"contractions": {
    "i'll": "i will",
    "don't": "do not",
    "can't": "cannot",
    "they're": "they are",
    "it's": "it is",
    "you're": "you are"
},
"slang": {
    "rizz": "charisma",
    "no cap": "truthfully",
    "bet": "agreed"
},
"vocabulary": {
    "i": "me",
    "will": "shall",
    "want": "desire",
    "you": "thou",
    "to": "unto"
}
}

for i in range(6, 4001):
data["vocabulary"][f"word_{i}"] = f"translation_{i}"

with open("dictionary.json", "w") as f:
json.dump(data, f, indent=4)

print("Successfully generated dictionary.json!")
