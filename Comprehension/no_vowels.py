def is_vowel(chr):
    if chr in 'aeouei':
        return True
    return False


text = input()
no_vowels = [x for x in text if not is_vowel(x)]
print(''.join(no_vowels))
