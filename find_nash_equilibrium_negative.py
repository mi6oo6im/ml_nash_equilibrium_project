def find_nash_equilibrium(numbers_for_a, numbers_for_b):
    
    #build the game matrix:


    matrix = (numbers_for_a, numbers_for_b)

    # get all possible outcomes as objects {coordinate; value}:
    l_l_a = {'coordinates': (0, 0), 'value': matrix[0][0]} # if b goes left, a goes left value for A
    l_r_a = {'coordinates': (0, 1), 'value': matrix[0][1]} # if b goes left, a goes right value for A
    r_l_a = {'coordinates': (0, 2), 'value': matrix[0][2]} # if b goes right, a goes left value for A
    r_r_a = {'coordinates': (0, 3), 'value': matrix[0][3]} # if b goes right, a goes right value for A
    l_l_b = {'coordinates': (1, 0), 'value': matrix[1][0]} # if a goes left, b goes left value for B
    l_r_b = {'coordinates': (1, 1), 'value': matrix[1][1]} # if a goes left, b goes right value for B
    r_l_b = {'coordinates': (1, 2), 'value': matrix[1][2]} # if a goes right, b goes left value for B
    r_r_b = {'coordinates': (1, 3), 'value': matrix[1][3]} # if a goes right, b goes right value for B

    # find best outcomes for each oposing player decision from type "A goes left - B best outcome":
    find_min_and_index = lambda x, y: (x['value'], x['coordinates'][1]) if x['value'] < y['value'] else (y['value'], y['coordinates'][1])

    b_goes_left_a_best_outcome, b_goes_left_a_best_outcome_index = find_min_and_index(l_l_a, l_r_a)
    b_goes_right_a_best_outcome, b_goes_right_a_best_outcome_index = find_min_and_index(r_l_a, r_r_a)
    a_goes_left_b_best_outcome, a_goes_left_b_best_outcome_index = find_min_and_index(l_l_b, r_l_b)
    a_goes_right_b_best_outcome, a_goes_right_b_best_outcome_index = find_min_and_index(l_r_b, r_r_b)

    # QA:
    print('      Left | Right')
    print('      -----------')
    print(f"Left  {l_l_a['value']}, {l_l_b['value']} | {r_l_a['value']}, {r_l_b['value']}")
    print('      -----------')
    print(f"Right {l_r_a['value']}, {l_r_b['value']} | {r_r_a['value']}, {r_r_b['value']}")
    print('      -----------')
    print(f'b_goes_left_a_best_outcome: {b_goes_left_a_best_outcome}')
    print(f'b_goes_left_a_best_outcome_index: {b_goes_left_a_best_outcome_index}')
    print(f'b_goes_right_a_best_outcome: {b_goes_right_a_best_outcome}')
    print(f'b_goes_right_a_best_outcome_index: {b_goes_right_a_best_outcome_index}')
    print(f'a_goes_left_b_best_outcome:{a_goes_left_b_best_outcome}')
    print(f'a_goes_left_b_best_outcome_index: {a_goes_left_b_best_outcome_index}')
    print(f'a_goes_right_b_best_outcome: {a_goes_right_b_best_outcome}')
    print(f'a_goes_right_b_best_outcome_index: {a_goes_right_b_best_outcome_index}')

    # check if Nash Equilibrium exist for the given matrix:
    if b_goes_left_a_best_outcome_index == a_goes_left_b_best_outcome_index or \
    b_goes_left_a_best_outcome_index == a_goes_right_b_best_outcome_index or \
    b_goes_right_a_best_outcome_index == a_goes_left_b_best_outcome_index or \
    b_goes_right_a_best_outcome_index == a_goes_right_b_best_outcome_index:
        print('We have a Nash equalibrium')
        set_intersection = set([b_goes_left_a_best_outcome_index, b_goes_right_a_best_outcome_index])\
            .intersection(set([a_goes_left_b_best_outcome_index, a_goes_right_b_best_outcome_index]))
        print(f'The Nash Equalibrium is on indexes {set_intersection}')
        number_of_nas = len(set_intersection)
        print(f'There are {number_of_nas} Nash equilibriums')
        nash_sums = [numbers_for_a[x] + numbers_for_b[x] for x in list(set_intersection)]
        min_of_nash_sums = min(nash_sums)
        print(f'The sums of NAs are {nash_sums}')
        print(f'The larger NA is {min_of_nash_sums}')
    else: 
        print('There is no Nash Equilibrium')
        return 0, 0, 0



    # find and return best Nash Equilibrium, best outcome for A payoff sum and best outcome for B payoff sum:
    min_a = min(numbers_for_a)
    b_for_min_a = numbers_for_b[numbers_for_a.index(min_a)]
    sum_for_min_a = min_a + b_for_min_a
    min_b = min(numbers_for_b)
    a_for_min_b = numbers_for_a[numbers_for_b.index(min_b)]
    sum_for_min_b = min_b + a_for_min_b

    # QA:
    print(f'min for A is {min_a} with B {b_for_min_a}')
    print(f'min for B is {min_b} with A {a_for_min_b}')
    print(f'sum for min A is {sum_for_min_a} and sum for min for B is {sum_for_min_b}')
    
    return min_of_nash_sums, sum_for_min_a, sum_for_min_b


nums_for_a = [5, 20, 0, 1]
nums_for_b = [5, 0, 20, 1]
find_nash_equilibrium(nums_for_a, nums_for_b)