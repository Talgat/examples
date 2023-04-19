import random
for i in range(3, -1, -1):
    print(i)
print('___')
for i in range(5):
    print(random.randint(1,10))

print('Привет', end='')
print('Мир')

print('коты', 'собаки', 'мыши', sep=', ')

def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
spam()

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)
number =2
number // 2
print(number)
