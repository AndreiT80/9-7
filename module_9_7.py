# Домашнее задание по теме "Декораторы"


from functools import wraps

def gen_primes(n=2):
    D = {}
    q = 2
    for i in range(n):
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def is_prime(func):
    # Декаратор
    @wraps(func)
    def inner(*args):
        i = func(*args)
        return (f'Составное \nСумма = {i}', f'Простое \nСумма = {i}')[i in gen_primes(i + 1)]

    return inner

@is_prime
def sum_three(*args):
    # Функция принимает три положительных ненулевых значения и возвращает их сумму
    if len(args) != 3 or any(i <= 0 for i in args):
        raise ValueError

    return sum(args)

result = sum_three(2, 3, 6)
print(result)
