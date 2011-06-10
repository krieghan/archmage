dictionary = {'verbs' : ['look',
                         'talk',
                         'ask',
                         'get',
                         'read'],
              'nouns' : ['me',
                         'mission',
                         'book',
                         'book of dominance',
                         'inventory'],
              'directions' : [],
              'articles' : [],
              'prepositions' : ['at', 
                                'to',
                                'about'],
              'pronouns' : [],
              'names' : [],
              'adjectives' : ['red']}
thesaurus = [['look',
              'examine'],
             ['talk',
              'speak'],
             ['get',
              'retrieve',
              'pick up']]

pluralReference = []

singleToPlural = {}
pluralToSingle = {}

for tup in pluralReference:
    singleToPlural[tup[0]] = tup[1]
    pluralToSingle[tup[1]] = tup[0]
