def get_phonetic_pronunciation(word):
    DICC = {
    "wife":"waif",
    "bus":"bas",
    "life":"laif",
    "beer":"biir"
    }

    return DICC.get(word.lower(),word.lower())

def split_into_syllables(word):
    accum = []

    syllable = ""
    for c in word:
        syllable += c
        if c in "aeiou":
            accum.append(syllable)
            syllable = ""
    if syllable:
        accum.append(syllable)

    return accum
