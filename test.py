def build_tree_helper(formula, start, end):
    # vars to keep track of '(' and ')'
    left_bracket_count = 0
    right_bracket_count = 0
    left_bracket_found = False
    right_bracket_found = False
    left_bracket_index = -1
    right_bracket_index = -1

    # loop left to right
    for i in range(start , end):


        bracket_difference = left_bracket_count - right_bracket_count


        # find when there is 1 ( and another connective
        # ignore when there is ) before (
        # fix this
        if(formula[i] == '(') and (not left_bracket_found):
            left_bracket_index = i
            left_bracket_count += 1

        elif(formula[i] == ')') and bracket_difference == 1:
            right_bracket_index = i
            right_bracket_count += 1

        elif((formula[i] == '*' or formula[i] == '+' or formula[i] == '-')
             and bracket_difference <= 1):
            connective_index = i
            connective = formula[i]

    return left_bracket_index, right_bracket_index, connective

a = '(x+y)'
print(build_tree_helper(a, 0, len(a)))