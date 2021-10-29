#!/usr/bin/env python3

words = {
    "att": "to",
    "det": "it",
    "gillar": "like",
    "jag": "I",
    "mat": "food",
    "spela": "play",
    "tv-spel": "videogames",
    "roligt": "fun",
    "är": "is"
}

def main():
    print("""\
--------------------------
{title:^25}
--------------------------""".format(title="Advanced Translator"))

    while True:
        sentence = input("Sentence > ")

        out = []
        for word in sentence.split(' '):
            # Translate if translation is availabe
            word = word.lower()
            out.append(words[word] if word in words else word)

        print(' '.join(out))

if __name__ == '__main__':
    main()
