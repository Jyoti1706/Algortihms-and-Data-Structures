'''
Recursive Approach to solve a solution
'''

def sum_natural_number(number):
    if number <= 1:
        return number
    return number + sum_natural_number(number - 1)


print(sum_natural_number(10))
