"""List of the functions for a home task #2."""


def is_digit(data):
    """Checks data for belonging to int or float numbers
    return boolean"""
    if type(data) in (int, float):
        return True
    return False


def gt_number_comparison(first_number, second_number):
    """Function #1. Comparing two numbers returns the greatest one"""
    if is_digit(first_number) and is_digit(second_number):
        if first_number > second_number:
            return first_number
        return second_number
    return 'Error. Unsupported format. Please use int, float'


def lt_number_comparison(first_number, second_number, third_number):
    """Function #2. Comparing three numbers returns the least one"""
    if is_digit(first_number) and is_digit(second_number) and is_digit(third_number):
        if first_number < second_number and first_number < third_number:
            return first_number
        if second_number < third_number:
            return second_number
        return third_number
    return 'Error. Unsupported format. Please use int, float'


def absolute_value(calculated_number):
    """Function #3. Takes any number and returns absolute value of it"""
    if isinstance(calculated_number, complex):
        result = (calculated_number.real**2+calculated_number.imag**2)**0.5
        return result
    if is_digit(calculated_number):
        result = (calculated_number**2)**0.5
        return result
    return 'Error. Unsupported format. Please use int, float, complex'


def my_sum(addend1, addend2):
    """Function #4. Takes two values and displaying their sum on a screen. Return None"""
    print(addend1+addend2)


def sign_definition (calculated_number):
    """Function #5. Takes number and give information about it's sign on a screen"""
    if is_digit(calculated_number):
        if calculated_number > 0:
            print('positive')
        elif calculated_number < 0:
            print('negative')
        else:
            print('Entered number is equal to zero')
    else:
        print('Error. Unsupported format. Please use int, float')
