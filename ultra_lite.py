# Генератор
print('======Генератор======')
def generator_example(num):
    for i in range(num):
        yield (i ** 3)

gen = generator_example(5)
print(next(gen))
print(next(gen))
print(next(gen))

# Тернарный оператор
print()
print('=Тернарный  оператор=')
age = 20
def check_adult(age):
    check = 0
    if age >= 18:
        check = 1
    else:
        check = 0
    return check

check_adult_l = lambda x: 1 if age >= 18 else 0
check = 1 if age >= 18 else 0
print(check_adult(age), check, check_adult_l(age))

# Декоратор
print()
print('======Декоратор======')

def show_type(f):
    def wrapper(*args, **kwargs):
        print('Код до функции!')
        print(f(*args, **kwargs))
        print('Код после функции!')
    return wrapper

@show_type
def my_add(a, b):
    return a + b

my_add(10, 20)