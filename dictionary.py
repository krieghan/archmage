dictionary = {'verbs' : ['look',
                         'talk',
                         'ask',
                         'get',
                         'read',
                         'put'],
              'nouns' : ['me',
                         'mission',
                         'book',
                         'book of dominance',
                         'inventory'],
              'directions' : [],
              'articles' : [],
              'prepositions' : ['at', 
                                'to',
                                'about',
                                'in',
                                'on'],
              'pronouns' : [],
              'names' : [],
              'adjectives' : ['red']}
thesaurus = [['look',
              'examine'],
             ['talk',
              'speak'],
             ['get',
              'retrieve',
              'pick up'],
             ['put',
              'place',
              'drop']]

pluralReference = []

singleToPlural = {}
pluralToSingle = {}

for tup in pluralReference:
    singleToPlural[tup[0]] = tup[1]
    pluralToSingle[tup[1]] = tup[0]
