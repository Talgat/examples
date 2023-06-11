birthdays = {'Beka' : 'november 9', 'Olzhas':'november 13','Nikita':'november 3',}

while True:
	print('Vvedite imya (<Enter> dlya vhoda:')
	name = input()
	if name == '':
		break
	if name in birthdays:
		print(name + ': den rozhdeniya - ' + birthdays[name])
	else:
		print('Ya ne znayu, kogda den rozhdeniya u ' + name)
		print('Koga den rozhdeniya u etogo cheloveka?')
		bday = input()
		birthdays[name] = bday
		print('Data rozhdeniya ' + name + ' vnesena v bazu')
