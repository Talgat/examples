def collatz(number):
    while number != 1:
        if number % 2 == 0 :
            res = number // 2
            print(res)
            number = res

            continue
        elif number % 2 == 1:
            res = 3 * number + 1
            print(res)
            number = res

            continue


while True:
    try:
        print('Vvedite chislo - ')
        n = int(input())
        collatz(n)
    except ValueError:
        print('Vvedite tseloe chislo!')

