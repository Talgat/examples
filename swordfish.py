while True:
    print('Kim syn ? ')
    name = input()
    if name != 'Tal':
        continue
    print('Salem!, Tal. Parol kakoy? (Eto ryba)')
    password = input()
    if password == 'ryba-mech':
        break
print('Dostup razreshen.')
