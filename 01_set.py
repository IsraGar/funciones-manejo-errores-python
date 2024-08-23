set_countries = {'col', 'mex', 'bol'}
print(set_countries)

set_numbers = {1,2,2,443,23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'asd', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)