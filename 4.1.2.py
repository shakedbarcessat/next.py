def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    sentence=(words[char] for char in sentence.split(' '))
    str=""
    for c in sentence:
        str+= c + " "
    return str

print(translate("el gato esta en la casa"))
