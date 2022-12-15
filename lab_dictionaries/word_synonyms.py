count_the_words = int(input())
synonyms_dictionaries = {}

for words in range(count_the_words):
    synonym = input()
    word = input()
    if synonym not in synonyms_dictionaries.keys():
        synonyms_dictionaries[synonym] = []
    synonyms_dictionaries[synonym].append(word)
for word, synonym1 in synonyms_dictionaries.items():
    print(f"{word} - {', '.join(synonym1)}")
