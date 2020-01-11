search_list = [
    'Jone', 'Aric', 'Luise', 'Frank', 'Wey'
    ]

found = False

for s in search_list:
    if s.startswith('C'):
        found = True
        # do something when found
        print('Found')
        break

if not found:
    # do something when not found
    print('Not found')
