catNames = []
while True:
    print('Укажите имя кота или кошки ' + str(len(catNames) + 1) +' (<Enter> для завершения):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # конкатенация списков
print('Имена котов и кошек:')
for name in catNames:
    print(' ' + name)
