import re

files = ['zaeem.xml', 'note.xml', 'index.html', 'bye.txt']

def search_files(files, ext: str):
    extension = re.compile(f'\.{ext}')
    results = filter(extension.search, files)
    return list(results)

print('Search files all .xml files present in list')
print('Result: ', search_files(files, 'xml'))

print("\nCoded By Durani Mohammed Zaeem; Roll no: 425")

""" 
nashra + 3
sara
rehan +2
ayaan
sadiya
qaseem+1
insha """