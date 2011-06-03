dictionary = {'verbs' : ['look',
                         'talk',
                         'ask'],
              'nouns' : ['me',
                         'mission',
                         'book'],
              'directions' : [],
              'articles' : [],
              'prepositions' : ['at', 
                                'to',
                                'about'],
              'pronouns' : [],
              'names' : [],
              'adjectives' : []}
thesaurus = [['look',
              'examine'],
             ['talk',
              'speak']]

pluralReference = []

singleToPlural = {}
pluralToSingle = {}

for tup in pluralReference:
    singleToPlural[tup[0]] = tup[1]
    pluralToSingle[tup[1]] = tup[0]
