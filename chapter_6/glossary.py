glossary = {
    'variable' : 'place to store value',
    'value' : 'information stored',
    'list' : 'set of stored values listed as elements',
    'dictionary' : 'set of stored key-value pairs',
    'syntax error' : 'typing error made by programmer',
    'set statement' : 'allows for a negation of like terms while looping',
    'sorted statement' : 'temporarily allows for alphabetical looping',
    'key' : 'act as a variable within a dictionary',
    'string' : 'alphabetical character(s) stored in variables',
    'del statement' : 'used to permanently delete items from lists or dictionary'
}

print('variable:'.title() +'\n\t' + glossary ['variable'].upper())
print('value:'.title() + '\n\t' + glossary ['value'].upper())
print('list:'.title() + '\n\t' + glossary ['list'].upper())
print('dictionary:'.title() + '\n\t' + glossary ['dictionary'].upper())
print('syntax error:'.title() + '\n\t' + glossary ['syntax error'].upper())

print('\n')
for term, meaning in sorted(glossary.items()):
    print(term.title() + ':\n\t' + meaning.upper())
