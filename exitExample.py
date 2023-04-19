import sys
while True:
    print('Vvedite "exit" dlya vyhoda.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('Vy vveli '+response+'.')
