"""
# Copyright Nick Cheng, Ao Gao, 2016, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

# Do not change this import statement, or add any of your own!
from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

# Do not change any of the class declarations above this comment.

# Add your functions here.

def build_tree(formula):
    '''
    (str) -> FormulaTree/None
    takes string <formula> and returns the FormulaTree representing the
    formula and is the root of the tree. Returns None if formula is not valid
    A forumla is valid if:

    >>>
    >>>
    True
    '''

    # empty strings are invalid
    if formula == '':
        result = None
    else:
        result = build_tree_helper(formula, 0, len(formula) - 1)
    return result

def build_tree_helper(formula, start, end):
    '''
    (str) -> FormulaTree
    takes string <formula> and returns the FormulaTree representing the
    formula.
    returns None is there are invalid bracketing
    end is inclusive
    >>>
    >>>
    True
    '''
    # if no conditions are met
    result = None

    # base case/ charcter check:
    if (start == end):

        if (formula[start].isalpha() and formula[start].islower()):
            # result is a leaf node with var
            result = Leaf(formula[start])

    # base case, formula starts with
    elif (formula[start] == '-'):
        sub_result = build_tree_helper(formula, start + 1, end)
        if sub_result is None:
            result = None
        else:
            result = NotTree(build_tree_helper(formula, start + 1, end))
    # else:
    else:

        # vars to keep track of '(' and ')'
        left_bracket_count = 0
        right_bracket_count = 0

        exit_loop = False
        i = start

        # find the most outer brackets and the connective associated with them
        while (i <= end and not exit_loop):

            bracket_difference = left_bracket_count - right_bracket_count

            if(formula[i] == '('):
                left_bracket_count += 1
            elif(formula[i] == ')'):
                right_bracket_count += 1

            if bracket_difference < 0:
                exit_loop = True


            # connective count to throw exceptions****************
            elif((formula[i] == '*' or formula[i] == '+')
                 and bracket_difference <= 1): # might not need this one
                connective = formula[i]


                # use divide and conquer, and build the tree
                left = build_tree_helper(formula,
                                         start + 1,
                                         i - 1 )

                right = build_tree_helper(formula,
                                          i + 1,
                                          end - 1)
                if(left is None or right is None):
                    result = None

                elif(connective == '*'):
                    result = AndTree(left, right)

                elif(connective == '+'):
                    result = OrTree(left, right)

                # exit the rest of the while loop
                exit_loop = True

            # increment the loop
            i += 1

    return result
    # return result


def draw_formula_tree(root):
    '''
    (FormulaTree) -> str
    take in <root> representing the root of the formula tree
    returns a string representing the tree. see formate below
    will return an empty string if the root is None
    The FormulaTree rooted at <root> is a valid formula if:
    NotTree has only 1 child
    OrTree and AndTree has left child and right child
    REQ: the given root represents a valid formula
    >>>
    >>>
    '''
    if root is not None:
        result = draw_formula_tree_helper(root, 0)
    else:
        result = ''

    return result


def draw_formula_tree_helper (root, depth):
    '''
    (FormulaTree) -> str
    counter is how far from the left
    '''
    # for debugging
    # counter is how many times it moved back
    # how many times children are drawn

    result = ''

    # base case: if leaf, draw at given location

    # for i in range(0, spaces):
        # result = result + ' '

    if isinstance(root, Leaf):
        result = result + root.get_symbol()

    # else:
    else:

        if (type(root) is AndTree) or (type(root) is OrTree):

            result = result + root.get_symbol()

            sub_result = draw_formula_tree_helper(root.get_children()[1], depth + 1)
            result = result + ' ' + sub_result + '\n'

            for i in range(0, depth + 1):
                result = result + '  '

            # left child second
            sub_result = draw_formula_tree_helper(root.get_children()[0], depth + 1)
            result = result + sub_result

        elif type(root) is NotTree:

            result = result + root.get_symbol()
            sub_result = draw_formula_tree_helper(root.get_children()[0], depth + 1)
            result = result + ' ' + sub_result

    return result

# ************************ say what valid formula is ***********************

def evaluate(root, variables, values):
    '''
    (FormulaTree, str, str) -> bool
    Takes in a FormulaTree rooted at <root> that represents a boolean formula
    assigns <values> to formula and evaluates the formula
    <variable> contains all the variables used in the formula
    <value> contains all the values for the variables respectively
    1 represents True and 0 represents False
    REQ: FormulaTree at root represents a valid formula
    REQ: all Leafs has corresponding variables and values
    REQ: variables contain only lowercase alphabetical characters
    REQ: every variable only appears once in variables
    REQ: len(variables) == len(values)
    REQ: root is not None
    REQ: simplest formula is one Leaf
    '''
    # to find * use min(a, b)
    # to find + use max(a, b)
    # to find - do 1 - truth value a

    # base case evaluate the leaf
    if type(root) is Leaf:
        symbol = root.get_symbol()
        index = variables.find(symbol)
        var_value = values[index]
        result = var_value
    # else: evaluate the chlidren to find the value of root
    else:
        if type(root) is AndTree:
            left_child = root.get_children()[0]
            right_child = root.get_children()[1]
            result = min(evaluate(left_child, variables, values),
                         evaluate(right_child, variables, values))

        elif type(root) is OrTree:
            left_child = root.get_children()[0]
            right_child = root.get_children()[1]
            result = max(evaluate(left_child, variables, values),
                         evaluate(right_child, variables, values))

        # type NotTree
        else:
            child = root.get_children()[0]
            result = 1 - evaluate(child, variables, values)

    return int(result)


def play2win(root, turns, variables, values):
    '''
    (FormulaTree, str, str, str) -> int
    Takes in a FormulaTree rooted at <root> that represents a boolean formula
    <wanted> is the wanted outcome for <winner>
    returns an int that guarantees a win for the current player
    returns 1 for player E if no possible next move to guarantee win exits
    returns 0 for player A if no possible next move to guarantee win exits
    REQ: len(variables) < len(values), there is a next move

    REQ:
    '''
    # if return result is wrong, just do post processing, so helper finds if there is guarantee win
    # pass in 1 or 0 to values to check if there is a guarantee win
    # just need to pass either, put else around everything

    # find who is trying to win with the next move
    # initialize the default value as result
    if turns[len(values)] == 'E':
        winner = 'E'
        default = 1
    else:
        winner = 'A'
        default = 0

    # case no wins, initialize it as no wins
    result = default

    default_win = play2win_helper(root, turns, variables, values + str(default), winner, result)
    # if default move guarantee win
    if default_win:
        # return default
        result = default

    else:
        # this is to avoid running the helper twice for some cases

        # if winnable with the non default choice then change result to it
        other_win = play2win_helper(root, turns, variables, values + str(1 - default), winner, result)

        if other_win:
            result = 1 - default

    return result


def play2win_helper(root, turns, variables, values, winner, wanted):
    '''
    (Formula,str, str, str) -> (int, bool) <- maybe dont need this
    looks for a guarantee win
    '''
    # determine which player's turn it is and corresponding default move
    # initialize result of that

    moves_left_num = len(variables) - len(values)

    # base case: evaluate the given case
    if moves_left_num == 0:

        move = evaluate(root, variables, values)

        guarantee_win = move == wanted

        return guarantee_win

    # base case: pick 1 var to evaluate
    elif moves_left_num == 1:
        move0 = evaluate(root, variables, values + '0')
        move1 = evaluate(root, variables, values + '1')

        # find who's turn it is
        winner_turn = turns[len(values)] == winner

        if winner_turn:
            guarantee_win = move0 == wanted or move1 == wanted

        else:
            guarantee_win = move0 == wanted and move1 == wanted

        return guarantee_win

    # else:
    else:

        default_win = play2win_helper(root, turns, variables,
                                      values + str(wanted), winner, wanted)
        other_win = play2win_helper(root, turns, variables,
                                    values + str(1 - wanted), winner, wanted)

        # if current turn is <winner>
        if turns[len(values)] == winner:
            # default OR other move guarantees win for <winner>
            # change to guarantee = default or other
            if default_win:
                guarantee_win = True
            elif other_win:
                guarantee_win = True
            else:
                guarantee_win = False
        # elif current turn is opponent
        else:
            # any move guarantee lose for <winner> FIX
            if (not default_win) or (not other_win):
                guarantee_win = False

            # ??????????????????????????????????????????????????????????????????????????? FIX
            # both moves guarantee win for <winner>
            else:
                guarantee_win = True

    return guarantee_win
    # else: fill in the otehr values and check for guarantee win


if(__name__ == '__main__'):
    # base p2w cases
    root = build_tree('x')
    a = play2win(root, 'E', 'x', '') == 1
    print('can win: True', play2win_helper(root, 'E', 'x', '', 'E', 1))
    print('1. returns:', a, '\n')

    root = build_tree('x')
    a = play2win(root, 'A', 'x', '') == 0
    print('can win: True', play2win_helper(root, 'A', 'x', '', 'A', 0))
    print('2. returns:', a, '\n')

    root = build_tree('(x*y)')
    a = play2win(root, 'EA', 'xy', '') == 1
    print('can win: False', play2win_helper(root, 'EA', 'xy', '', 'E', 1))
    print('3. returns:', a, '\n')

    root = build_tree('(x*y)')
    a = play2win(root, 'EE', 'xy', '') == 1
    print('can win: True', play2win_helper(root, 'EE', 'xy', '', 'E', 1))
    print('4. returns:', a, '\n')

    root = build_tree('(x*y)')
    a = play2win(root, 'AE', 'xy', '') == 0
    print('can win: True', play2win_helper(root, 'AE', 'xy', '', 'A', 0))
    print('5. returns:', a, '\n')

    root = build_tree('(x*y)')
    a = play2win(root, 'AA', 'xy', '') == 0
    print('can win: True', play2win_helper(root, 'AA', 'xy', '', 'A', 0))
    print('6. returns:', a, '\n')

    root = build_tree('(x+y)')
    a = play2win(root, 'EA', 'xy', '') == 1
    print('can win: True', play2win_helper(root, 'EA', 'xy', '', 'E', 1))
    print('7. returns:', a, '\n')

    root = build_tree('(x+y)')
    a = play2win(root, 'EE', 'xy', '') == 1
    print('can win: True', play2win_helper(root, 'EE', 'xy', '', 'E', 1))
    print('8. returns:', a, '\n')

    root = build_tree('(x+y)')
    a = play2win(root, 'AE', 'xy', '') == 0
    print('can win: False', play2win_helper(root, 'AE', 'xy', '', 'A', 0))
    print('9. returns:', a, '\n')

    root = build_tree('(x+y)')
    a = play2win(root, 'AA', 'xy', '') == 0
    print('can win: True', play2win_helper(root, 'AA', 'xy', '', 'A', 0))
    print('10. returns:', a, '\n')

    root = build_tree('-x')
    a = play2win(root, 'A', 'x', '') == 1
    print('can win: True', play2win_helper(root, 'A', 'x', '', 'A', 0))
    print('11. returns:', a, '\n')

    root = build_tree('-x')
    a = play2win(root, 'E', 'x', '') == 0
    print('can win: True', play2win_helper(root, 'E', 'x', '', 'E', 1))
    print('12. returns:', a, '\n')

    # hard p2w cases
    root = build_tree('((-x*y)+z)')
    a = play2win(root, 'EAE', 'xyz', '') == 1
    print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    print('13. returns:', a, '\n')

    root = build_tree('((-x+y)*z)')
    a = play2win(root, 'EAE', 'xyz', '') == 0
    print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    print('13.1. returns:', a, '\n')

    # DO EXAMPLES, TEST FOR already picked

    root = build_tree('((-x+y)*z)')
    a = play2win(root, 'EAE', 'xyz', '') == 0
    print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    print('13.1. returns:', a, '\n')

    root = build_tree('((-x+y)*z)')
    a = play2win(root, 'EAE', 'xyz', '1') == 0
    print('can win: False', play2win_helper(root, 'EAE', 'xyz', '1', 'E', 1))
    print('13.1. returns:', a, '\n')

    # root = build_tree('(x*y)')
    # a = play2win(root, 'EE', 'xy', '') == 1
    # print('gw need: False', 'gw need: False')
    # print('returns:', a, '\n')


    # root = build_tree('(x*y)')
    # print(play2win(root, 'EE', 'xy', '') == 1)
    # print('gw', play2win_helper(root, 'EE', 'xy', '', 'E', 1), 'need: True')

    # root = build_tree('(x*y)')
    # print(play2win(root, 'AE', 'xy', '') == 0)
    # print('gw1', play2win_helper(root, 'AE', 'xy', '', 'A', 0), 'need: False')


    # root = build_tree('x')
    # print(play2win(root, 'E', 'x', '') == 1)
    # root = build_tree('x')
    # print(play2win(root, 'A', 'x', '') == 0)

    # # * no possible win, ret default W
    # root = build_tree('(x*y)')
    # print(play2win(root, 'EA', 'xy', '') == 1)
    # root = build_tree('(x*y)')
    # print(play2win(root, 'AE', 'xy', '') == 0)

    # # guarantee win, ret non default L
    # root = build_tree('(x*y)')
    # print(play2win(root, 'EA', 'xy', '0') == 0)
    # root = build_tree('(x*y)')
    # print(play2win(root, 'AE', 'xy', '1') == 1)


    # root = build_tree('(x+y)')
    # print(play2win(root, 'EA', 'xy', '') == 1)

    # root = build_tree('(x+y)')
    # print(play2win(root, 'AE', 'xy', '') == 0)











    # tree = build_tree('x')
    # print(evaluate(tree, 'x', '0') == 0)

    # tree = build_tree('-x')
    # print(evaluate(tree, 'x', '0') == 1)

    # tree = build_tree('-(x*x)')
    # print(evaluate(tree, 'x', '0') == 1)

    # tree = build_tree('(x*y)')
    # print(evaluate(tree, 'xy', '01') == 0)

    # tree = build_tree('(x+y)')
    # print(evaluate(tree, 'xy', '01') == 1)

    # tree = build_tree('((x+y)*(x*y))')
    # print(evaluate(tree, 'xy', '01') == 0)

    # tree = build_tree('(((x*y)*z)*w)')
    # print(evaluate(tree, 'xy', '01') == 0)

    # tree = build_tree('(((x+y)+z)+w)')
    # print(evaluate(tree, 'xy', '01') == 1)



    # MOREEEEEEEEEE TESTSSSSSSS
    # plswork = build_tree('-x')
    # plswork = draw_formula_tree(plswork)
    # print(plswork == '- x' )

    # plswork = build_tree('(x*y)')
    # plswork = draw_formula_tree(plswork)
    # print(plswork == '* y\n  x' )
    # print(plswork)


    # plswork = build_tree('(x+y)')
    # plswork = draw_formula_tree(plswork)
    # print(plswork == '+ y\n  x' )
    # print(plswork)


    # plswork = build_tree('((-x+y)*-(-y+x))')
    # plswork = draw_formula_tree(plswork)
    # print(plswork == '* - + x\n      - y\n  + y\n    - x')
    # print(plswork)

    # plswork = build_tree('(((x*y)*--z)*w)')
    # plswork = draw_formula_tree(plswork)
    # print(plswork)


    # print(build_tree(''))

    # plswork = build_tree('x')
    # print(1, repr(plswork) == "Leaf('x')" )

    # plswork = build_tree('-x')
    # print(2, repr(plswork) == "NotTree(Leaf('x'))")

    # plswork = build_tree('(x+y)')
    # print(3, repr(plswork) == "OrTree(Leaf('x'), Leaf('y'))")

    # plswork = build_tree('(x*y)')
    # print(4, repr(plswork) == "AndTree(Leaf('x'), Leaf('y'))")

    # plswork = build_tree('(x+-y)')
    # print(5, repr(plswork) == "OrTree(Leaf('x'), NotTree(Leaf('y')))")

    # plswork = build_tree('(-x+y)')
    # print(5.1, repr(plswork) == "OrTree(NotTree(Leaf('x')), Leaf('y'))")

    # plswork = build_tree('-(x*y)')
    # print(5.2, repr(plswork) == "NotTree(AndTree(Leaf('x'), Leaf('y')))")

    # plswork = build_tree('(-x*-y)')
    # print(5.2, repr(plswork) == "AndTree(NotTree(Leaf('x')), NotTree(Leaf('y')))")

    # plswork = build_tree('((x+y)+z)')
    # print(6, repr(plswork) == "OrTree(OrTree(Leaf('x'), Leaf('y')), Leaf('z'))")

    # plswork = build_tree('(((x*y)*z)*w)')
    # print(7, repr(plswork) == "AndTree(AndTree(AndTree(Leaf('x'), Leaf('y')), Leaf('z')), Leaf('w'))")

    # plswork = build_tree('--x')
    # print(8, repr(plswork) == "NotTree(NotTree(Leaf('x')))")

    # plswork = build_tree('-----x')
    # print(9, repr(plswork) == "NotTree(NotTree(NotTree(NotTree(NotTree(Leaf('x'))))))")

    # plswork = build_tree('(-x*(y+z))')
    # print(10.1, repr(plswork) == "AndTree(NotTree(Leaf('x')), OrTree(Leaf('y'), Leaf('z')))")


    # plswork = build_tree('((x+y)*((y+z)*(-y+-z)))')
    # print(10.2, repr(plswork) == "AndTree(OrTree(Leaf('x'), Leaf('y')), AndTree(OrTree(Leaf('y'), Leaf('z')), OrTree(NotTree(Leaf('y')), NotTree(Leaf('z')))))")
    # plswork = build_tree('(---x*y)')
    # print(10.3, repr(plswork) == "AndTree(NotTree(NotTree(NotTree(Leaf('x')))), Leaf('y'))")

    # plswork = build_tree('!a')
    # print(plswork)
    # plswork = build_tree('(x+y*z)')
    # print(plswork)
    # plswork = build_tree('(x*y*z)')
    # print(plswork)
    # plswork = build_tree('((x+y)*(x-y)*(x+z))')
    # print(plswork)
    # plswork = build_tree('(x+(u*v*w*z)+y)')
    # print(plswork)
    # plswork = build_tree('-x-y')
    # print(plswork)
    # plswork = build_tree('(x+y*x+y)')
    # print(plswork)
    # plswork = build_tree('x)')
    # print(plswork)
    # plswork = build_tree('++++x')
    # print(plswork)
    # plswork = build_tree('-(-a)')
    # print(plswork)
    # plswork = build_tree('(x+y)*(x+z)')
    # print(plswork)
    # plswork = build_tree('-(ab)')
    # print(plswork)
    # plswork = build_tree('(a+(B*-c))')
    # print(plswork)
    # plswork = build_tree('(x * c)')
    # print(plswork)
    # plswork = build_tree('-+x')
    # print(plswork)
    # plswork = build_tree('!a')
    # print(plswork)
    # plswork = build_tree('(x+x(()')
    # print(plswork)
    # plswork = build_tree('((x+y))')
    # print(plswork)
    # plswork = build_tree(')x+y(')
    # print(plswork)
    # plswork = build_tree('x+y')
    # print(plswork)
