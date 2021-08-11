def num_syl(word):
    return len(word.split('-'))

x = input('Write your word separate by the dash to denote syllables: ')

print('The number of syllables in ' + x + ' is ' + str(num_syl(x)))

