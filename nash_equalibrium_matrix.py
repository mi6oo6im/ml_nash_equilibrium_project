from random import shuffle 

def randomize():
    numbers = list(range(1, 9))
    shuffle(numbers)
    numbers_for_matrix = numbers[0:4]
    return numbers_for_matrix

numbers_for_a = randomize()
numbers_for_b = randomize()

matrix = (numbers_for_a, numbers_for_b)


l_l_a = {'coordinates': (0, 0), 'value': matrix[0][0]}
l_r_a = {'coordinates': (0, 1), 'value': matrix[0][1]}
r_l_a = {'coordinates': (0, 2), 'value': matrix[0][2]}
r_r_a = {'coordinates': (0, 3), 'value': matrix[0][3]}
l_l_b = {'coordinates': (1, 0), 'value': matrix[1][0]}
l_r_b = {'coordinates': (1, 1), 'value': matrix[1][1]}
r_l_b = {'coordinates': (1, 2), 'value': matrix[1][2]}
r_r_b = {'coordinates': (1, 3), 'value': matrix[1][3]}

# b_goes_left_a_best_outcome = max(matrix[0][0], matrix[0][2])
# b_goes_left_a_best_outcome_index = matrix[0].index(b_goes_left_a_best_outcome)
# b_goes_right_a_best_outcome = max(matrix[0][1], matrix[0][3])
# b_goes_right_a_best_outcome_index = matrix[0].index(b_goes_right_a_best_outcome)
# a_goes_left_b_best_outcome = max(matrix[1][0], matrix[1][1])
# a_goes_left_b_best_outcome_index = matrix[1].index(a_goes_left_b_best_outcome)
# a_goes_right_b_best_outcome = max(matrix[1][2], matrix[1][3])
# a_goes_right_b_best_outcome_index = matrix[1].index(a_goes_right_b_best_outcome)

find_max_and_index = lambda x, y: (x['value'], x['coordinates'][1]) if x['value'] > y['value'] else (y['value'], y['coordinates'][1])

b_goes_left_a_best_outcome, b_goes_left_a_best_outcome_index = find_max_and_index(l_l_a, r_l_a)
b_goes_right_a_best_outcome, b_goes_right_a_best_outcome_index = find_max_and_index(r_l_a, r_r_a)
a_goes_left_b_best_outcome, a_goes_left_b_best_outcome_index = find_max_and_index(l_l_b, l_r_b)
a_goes_right_b_best_outcome, a_goes_right_b_best_outcome_index = find_max_and_index(r_l_b, r_r_b)

print('      Left | Right')
print('      -----------')
print(f"Left  {l_l_a['value']}, {l_l_b['value']} | {l_r_a['value']}, {l_r_b['value']}")
print('      -----------')
print(f"Right {r_l_a['value']}, {r_l_b['value']} | {r_r_a['value']}, {r_r_b['value']}")
print('      -----------')
print(f'b_goes_left_a_best_outcome: {b_goes_left_a_best_outcome}')
print(f'b_goes_left_a_best_outcome_index: {b_goes_left_a_best_outcome_index}')
print(f'b_goes_right_a_best_outcome: {b_goes_right_a_best_outcome}')
print(f'b_goes_right_a_best_outcome_index: {b_goes_right_a_best_outcome_index}')
print(f'a_goes_left_b_best_outcome:{a_goes_left_b_best_outcome}')
print(f'a_goes_left_b_best_outcome_index: {a_goes_left_b_best_outcome_index}')
print(f'a_goes_right_b_best_outcome: {a_goes_right_b_best_outcome}')
print(f'a_goes_right_b_best_outcome_index: {a_goes_right_b_best_outcome_index}')

if b_goes_left_a_best_outcome_index == a_goes_left_b_best_outcome_index or \
   b_goes_left_a_best_outcome_index == a_goes_right_b_best_outcome_index or \
   b_goes_right_a_best_outcome_index == a_goes_left_b_best_outcome_index or \
   b_goes_right_a_best_outcome_index == a_goes_right_b_best_outcome_index:
    print('We have a Nash equalibrium')
    set_intersection = set([b_goes_left_a_best_outcome_index, b_goes_right_a_best_outcome_index])\
        .intersection(set([a_goes_left_b_best_outcome_index,a_goes_right_b_best_outcome_index]))
    print(f'The Nash Equalibrium is on indexes {set_intersection}')
    
print(f'max for A is {max(numbers_for_a)}')
print(f'max for B is {max(numbers_for_b)}')
