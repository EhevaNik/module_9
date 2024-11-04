# Домашнее задание по теме "Декораторы"
def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in range(2, int(result ** 0.5) + 1):
            if result > 1:
                return 'Простое'
            else:
                return 'Составное'
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    print(result)
    return result

result = sum_three(2, 3, 6)
print(result)