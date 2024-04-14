from random import shuffle 

def randomize():
    numbers = list(range(1, 9))
    shuffle(numbers)
    numbers_for_matrix = numbers[0:4]
    return numbers_for_matrix

numbers_for_a = randomize()
numbers_for_b = randomize()

matrix = (numbers_for_a, numbers_for_b)

l_l_a_value = matrix[0][0]
l_r_a_value = matrix[0][1]
r_l_a_value = matrix[0][2]
r_r_a_value = matrix[0][3]
l_l_b_value = matrix[1][0]
l_r_b_value = matrix[1][1]
r_l_b_value = matrix[1][2]
r_r_b_value = matrix[1][3]


b_goes_left_a_best_outcome = max(matrix[0][0], matrix[0][2])
b_goes_left_a_best_outcome_index = matrix[0].index(b_goes_left_a_best_outcome)
b_goes_right_a_best_outcome = max(matrix[0][1], matrix[0][3])
b_goes_right_a_best_outcome_index = matrix[0].index(b_goes_right_a_best_outcome)
a_goes_left_b_best_outcome = max(matrix[1][0], matrix[1][1])
a_goes_left_b_best_outcome_index = matrix[1].index(a_goes_left_b_best_outcome)
a_goes_right_b_best_outcome = max(matrix[1][2], matrix[1][3])
a_goes_right_b_best_outcome_index = matrix[1].index(a_goes_right_b_best_outcome)

print('      Left | Right')
print('      -----------')
print(f'Left  {l_l_a_value}, {l_l_b_value} | {l_r_a_value}, {l_r_b_value}')
print('      -----------')
print(f'Right {r_l_a_value}, {r_l_b_value} | {r_r_a_value}, {r_r_b_value}')
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
