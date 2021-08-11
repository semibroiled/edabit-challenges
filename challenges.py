def number_syl(word):
    return len(word.split('-'))

x = input('Write you word separate by the dash to denote syllables')

print('The number of syllables in ' + x + ' is ' + str(number_syl(x)))

