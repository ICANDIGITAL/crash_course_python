from collections import OrderedDict

glossary = OrderedDict()

glossary['variable'] = 'place to store value'
glossary['value'] = 'information stored'
glossary['list'] = 'set of stored values listed as elements'
glossary['dictionary'] = 'set of stored key-value pairs'
glossary['syntax error'] = 'typing error made by programmer'
glossary['set statement'] = 'allows for a negation of like terms while looping'
glossary['sorted statement'] = 'temporarily allows for alphabetical looping'
glossary['key'] = 'act as a variable within a dictionary'
glossary['string'] = 'alphabetical character(s) stored in variables'
glossary['del statement'] = 'used to permanently delete items from lists or dictionary'

for term, meaning in sorted(glossary.items()):
    print(term.title() + ':\n\t' + meaning.upper())
