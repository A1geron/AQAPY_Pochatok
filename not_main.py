"""HW3. Some decorator"""
import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            result = None
            for _ in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            return 'Error.', result, 'is not your lucky number.'
        return inner
    return wrapper


# examples of implemented 'retry' decorator
@retry(desired_value=3)
def get_random_value1():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values1(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value2():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values2(choices, size=2):
    return random.choices(choices, k=size)

# print_square functions
def print_square_cycle(size):
    print('*' * size)
    for _ in range(size-2):
        inner_string = '*' + ' ' * (size - 2) + '*'
        print(inner_string)
    if size > 1:
        print('*' * size)


def inner_square(counter, sized):
    if counter <= 0:
        print('*' * (sized + 2))
        return None
    resulting_raw = '*' + ' ' * sized + '*'
    print(resulting_raw)
    return inner_square(counter-1, sized)


def print_square(size):
    print('*' * size)
    if size <= 1:
        return None
    return inner_square(size - 2, size - 2)


if __name__ == '__main__':
    get_random_value1()
    get_random_value2()
    get_random_values1([1, 2, 3, 4])
    get_random_values1([1, 2, 3, 4], 3)
    get_random_values2([1, 2, 3, 4], size=1)
    print_square_cycle(4)
    print_square(4)
