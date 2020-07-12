from datetime import datetime

def run_only_beteen(_from=7, _to=22):
    def disable_at_night(func):
        def wrapper():
            if _from <= datetime.now().hour < _to:
                func()
            else:
                pass
        return wrapper
    return disable_at_night

@run_only_beteen(12, 22)
def say_something():
    print("Hello!!")

# say_something()

def start_stop(func):
    def wrapper(*args, **kwargs):
        print('START')
        result = func(*args, **kwargs)
        if result is not None:
            print(result)
        print('STOP')
    return wrapper

@start_stop
def hello():
    print('hello')

@start_stop
def triangle_area(a, h):
    return a * h / 2

# hello()
# triangle_area(4, 3)
# triangle_area(a=4, h=3)

# Zadanie
# Udekoruj dowolną funkcję zwracającą jakąś wartość, tak, by możliwe było
# zbadanie czasu jej wykonania.


def time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        stop = datetime.now()
        print(f'Time: {stop - start}')
    return wrapper

@time
def fib_iter(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]

#fib_iter(100000)

# Zadanie
# Zoptymalizuj rekurencyjną funkcję zwracającą n-ty wyraz ciągu
# Fibonacciego.

def memoize(function):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return decorated_function


@memoize
def fib_rek(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib_rek(n-1) + fib_rek(n-2)

# fib_rek(1000)

#fib_rek(3)

# Zadanie
# Napisz dekorator, który spowoduje, że przy wywołaniu udekorowanej
# funkcji wypisze się na ekran informacja po raz który ta funkcja jest
# wywoływana, np.: "Funkcja <nazwa funkcji> została uruchomiona <n>
# raz"

def counted(func):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        print(wrapped.calls)
        func(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

@counted
def hello2():
    print('hello')

# for i in range(5):
#     hello2()

# Zadanie
# Stwórz funkcję wyświetlającą na ekranie dowolny napis, a następnie
# dekorator, który będzie wykonywał tę funkcję n razy (gdzie n jest
# parametrem przekazywanym do dekoratora).

def n_times(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@n_times(5)
def hello3():
    print('hello')

# hello3()

# Zadanie
# Napisz dekorator, który będzie wymagał podania hasła przed właściwym
# wywołaniem funkcji. Jeśli zostanie podane błędne hasło to niech będzie
# wypisany komunikat o braku dostępu.

def password(f):
    def wrapper():
        user_pass = input('Password: ')
        if user_pass == 'pass':
            f()
        else:
            print('Wrong password.')
    return wrapper

@password
def hello4():
    print('hello')

# hello4()

# Zadanie 1
# Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji
# będzie wyświetlał informacje o jej nazwie, przekazanych parametrach
# oraz zwracanym wyniku.

def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Funkcja {func.__name__}({args} {kwargs}) zwróciła {result}.')
    return wrapper

@debug
def func(a, b, c):
    return a + b * c

# print(func(3, b=2, c=4))

# Zadanie 2
# Stwórz dekorator o nazwie multiply, który
# przyjmuje argument n i zwiększa n-krotnie
# rezultat wykonania udekorowanej funkcji

def multiply(n=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * n
        return wrapper
    return decorator

@multiply(3)
def func1():
    return 'Ala ma kota.\n'

@multiply(5)
def func2(a, b):
    return a + b

print(func1())
print(func2(2, 3))
