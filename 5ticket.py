import random
def get_jokes(n):
    jokes = ''
    i = 0
    while i < n-1:
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        jokes = jokes + ' ' + noun + ' ' +adverb +' '+adjective +','
        i+=1
    jokes = jokes + ' ' + random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives) + '.'
    return jokes

#print(get_jokes(5))