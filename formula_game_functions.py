"""
# Copyright Nick Cheng, 2016
# Copyright Ao Gao, 2018
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
    Takes string <formula> and returns the root of the FormulaTree that
    represents <formula>. Returns None if formula is not valid
    a valid formula contains the following:
    - boolean variables: lowercase alphabetical letters
    - connectives: '*' represents AND, '+' represent OR, '-' represent NOT
    - parentheses: '(' and ')'
    rules for formula:
    - the simpliest formula is just a boolean variable
    - more complex formulas uses connectives and variables
    - arguments for '*' and '+' are always enclosed by parentheses
    - arugments for connectives are formulas
    any string that cannot be constructed with rules above are not valid
    (i.e empty, invalid characters, using connectives without using brackets)
    >>> a = build_tree('(x+y)')
    >>> repr(a) == "OrTree(Leaf('x'), Leaf('y'))"
    True
    >>> a = build_tree('(-x*(y+z))')
    >>> repr(a) == "AndTree(NotTree(Leaf('x')), OrTree(Leaf('y'), Leaf('z')))"
    True
    >>> build_tree('(x+y*z)') == None
    True
    '''

    # empty strings break helper fnc, they are invalid, directly ret None
    if formula == '':
        result = None
    else:
        # else run the helper function
        result = build_tree_helper(formula, 0, len(formula) - 1)
    return result


def build_tree_helper(formula, start, end):
    '''
    (str, int, int) -> FormulaTree/None
    takes string <formula> and returns the root of the FormulaTree that
    represents <formula>. Returns None if formula is not valid
    <start> is starting index of <formula> to start building tree
    <end> is ending index of <formula> to start building tree, is inclusive
    this function is recursive
    a valid formula contains the following:
    - boolean variables: lowercase alphabetical letters
    - connectives: '*' represents AND, '+' represent OR, '-' represent NOT
    - parentheses: '(' and ')'
    rules for formula:
    - the simpliest formula is just a boolean variable
    - more complex formulas uses connectives and variables
    - arguments for '*' and '+' are always enclosed by parentheses
    - arugments for connectives are formulas
    any string that cannot be constructed with rules above are not valid
    (i.e empty, invalid characters, using connectives without using brackets)
    >>> a = build_tree_helper('(x+y)', 0 ,len('(x+y)') - 1)
    >>> repr(a) == "OrTree(Leaf('x'), Leaf('y'))"
    True
    >>> a = build_tree_helper('(-x*(y+z))', 1, 2)
    >>> repr(a) == "NotTree(Leaf('x'))"
    True
    '''
    # initialize result as None, so iff no valid conditions are met, ret None
    result = None

    # base case: 1 character
    if (start == end):

        # if the charcter is lowercase alphabetical letter
        if (formula[start].isalpha() and formula[start].islower()):

            # result is a Leaf node with the given letter
            result = Leaf(formula[start])

    # base case: formula starts with '-'
    elif (formula[start] == '-'):

        # check whether rest of the formula is valid
        sub_result = build_tree_helper(formula, start + 1, end)

        # if the rest of the formula is not valid
        if sub_result is None:

            # the whole formula is not valid
            result = None

        else:
            # else attach the FormulaTree representing the rest of the formula
            # to NotTree and ret
            result = NotTree(sub_result)

    # else recursive step
    else:

        # vars to keep track of '(' and ')'
        left_bracket_count = 0
        right_bracket_count = 0

        # vars for efficient while loop
        exit_loop = False
        i = start

        # find the most outer brackets and the connective associated with them
        # iterate through forumula until they are found
        while (i <= end and not exit_loop):

            bracket_difference = left_bracket_count - right_bracket_count

            # keep track of how many of each bracket is in the formula
            if(formula[i] == '('):
                left_bracket_count += 1
            elif(formula[i] == ')'):
                right_bracket_count += 1

            # if there are more ')' than '(' then formula is invalid
            # exit loop and return None
            if bracket_difference < 0:
                exit_loop = True

            # connective for outer brackets is when <bracket_difference>  <= 1
            # and the current character is '*' or '+'
            elif((formula[i] == '*' or formula[i] == '+') and
                 bracket_difference <= 1):

                connective = formula[i]

                # divide and conquer, and build the tree to the left and right
                # of the connective
                left = build_tree_helper(formula, start + 1, i - 1)
                right = build_tree_helper(formula, i + 1, end - 1)

                # if any part of that is invalid, then whole forulma is invalid
                if(left is None or right is None):
                    result = None

                # set the left and right tree as the children of the found
                # connective
                elif(connective == '*'):
                    result = AndTree(left, right)
                elif(connective == '+'):
                    result = OrTree(left, right)

                # exit the rest of the while loop, if connective is found
                exit_loop = True

            # increment the loop
            i += 1

    # return result
    return result


def draw_formula_tree(root):
    '''
    (FormulaTree) -> str
    take FormulaTree <root> that represents a valid forumla
    returns a string representing the tree.
    will return an empty string if the root is None
    The FormulaTree rooted at <root> represents a valid formula if:
    - <root> is not None
    - NotTree has only 1 child
    - OrTree and AndTree has left child and right child
    - child(ren) of connective are either (Leaf/OrTree/AndTree/NotTree)
    - The leaf of the tree is a LeafTree lowercase letter (variable)
    REQ: <root> represents a valid formula tree
    >>> a = build_tree('(x*y)')
    >>> draw_formula_tree(a)
    '* y\\n  x'
    >>> a = build_tree('((-x+y)*-(-y+x))')
    >>> draw_formula_tree(a)
    '* - + x\\n      - y\\n  + y\\n    - x'
    '''
    # run the helper function if the root (root should repr valid formula)
    result = draw_formula_tree_helper(root, 0)

    return result


def draw_formula_tree_helper(root, depth):
    '''
    (FormulaTree, int) -> str
    take FormulaTree <root> that represents a valid forumla
    returns a string representing the tree.
    will return an empty string if the root is None
    <depth> is the the depth of the current node in the tree
    The FormulaTree rooted at <root> represents a valid formula if:
    - <root> is not None
    - NotTree has only 1 child
    - OrTree and AndTree has left child and right child
    - child(ren) of connective are either (Leaf/OrTree/AndTree/NotTree)
    - The leaf of the tree is a LeafTree lowercase letter (variable)
    REQ: <root> represents a valid formula tree
    >>> a = build_tree('(x*y)')
    >>> draw_formula_tree_helper(a, 0)
    '* y\\n  x'
    >>> a = build_tree('(x*y)')
    >>> draw_formula_tree_helper(a, 2)
    '* y\\n      x'
    '''

    # initialize result to draw to
    result = ''

    # base case: if leaf, draw at given location
    if isinstance(root, Leaf):
        result = result + root.get_symbol()

    else:

        # if root is a BinaryTree
        if (type(root) is AndTree) or (type(root) is OrTree):

            # add symbol of the tree tor result
            result = result + root.get_symbol()

            # increase depth and draw the rest the the right childs
            sub_result = draw_formula_tree_helper(root.get_children()[1],
                                                  depth + 1)

            # draw new line at the end of all the right childs
            result = result + ' ' + sub_result + '\n'

            # draw 2 spaces for each level of depth the left child is in
            for i in range(0, depth + 1):
                result = result + '  '

            # increase depth and draw left child after drawinf right child
            sub_result = draw_formula_tree_helper(root.get_children()[0],
                                                  depth + 1)
            result = result + sub_result

        # if root is a UnaryTree
        elif type(root) is NotTree:

            # draw the -  symbol
            result = result + root.get_symbol()

            # increase the depth and draw the rest of the formula
            sub_result = draw_formula_tree_helper(root.get_children()[0],
                                                  depth + 1)
            result = result + ' ' + sub_result

    return result


def evaluate(root, variables, values):
    '''
    (FormulaTree, str, str) -> int
    Takes in a FormulaTree rooted at <root> that represents a valid
    boolean formula
    assigns <values> to formula and evaluates the formula
    <variable> contains all the variables used in the formula
    <value> contains all the values for the variables respectively
    1 represents True and 0 represents False
    The FormulaTree rooted at <root> represents a valid formula if:
    - <root> is not None
    - NotTree has only 1 child
    - OrTree and AndTree has left child and right child
    - child(ren) of connective are either (Leaf/OrTree/AndTree/NotTree)
    - The leaf of the tree is a LeafTree lowercase letter (variable)
    REQ: <root> represents a valid formula tree
    REQ: all Leafs are assigned values by <variables> and <values>
    REQ: <variables> is a combination of lowercase alphabetical characters
    REQ: every variable only appears once in variables
    REQ: <values> contains only a combination of '1' and '0'
    REQ: len(variables) == len(values)
    >>> tree = build_tree('x')
    >>> evaluate(tree, 'x', '0') == 0
    True
    >>> tree = build_tree('(((x*y)*z)*w)')
    >>> evaluate(tree, 'xyzw', '0111') == 0
    True
    '''

    # base case evaluate the leaf
    if type(root) is Leaf:

        # find the symbol of Leaf
        symbol = root.get_symbol()

        # use index of symbol in <variables> to find the value of the
        # symbol in <values> which has the same index
        index = variables.find(symbol)
        var_value = values[index]

        # return value as int
        result = int(var_value)

    # else: evaluate the chlidren to find the value of root
    else:

        # if the root is Binary, evalute the left and right childs applying
        # the connectives to the value of the chlidren
        if type(root) is AndTree:
            left_child = root.get_children()[0]
            right_child = root.get_children()[1]

            # to find *, use min(a, b)
            result = min(evaluate(left_child, variables, values),
                         evaluate(right_child, variables, values))

        elif type(root) is OrTree:
            left_child = root.get_children()[0]
            right_child = root.get_children()[1]

            # to find +, use max(a, b)
            result = max(evaluate(left_child, variables, values),
                         evaluate(right_child, variables, values))

        # if the root is Unary, evalute the child applying before applying
        # conenctives to the valid of the chlid
        else:
            child = root.get_children()[0]

            # to find -, do 1 - truth value a
            result = 1 - evaluate(child, variables, values)

    return result


def play2win(root, turns, variables, values):
    '''
    (FormulaTree, str, str, str) -> int
    returns an int that guarantees a win for the current player
    returns 1 for player E if no possible next move to guarantee win exits
    returns 0 for player A if no possible next move to guarantee win exits
    The FormulaTree rooted at <root> represents a valid formula if:
    - <root> is not None
    - NotTree has only 1 child
    - OrTree and AndTree has left child and right child
    - child(ren) of connective are either (Leaf/OrTree/AndTree/NotTree)
    - The leaf of the tree is a LeafTree lowercase letter (variable)
    REQ: <root> represents a valid formula tree
    REQ: <turns> is a combination of 'E' and "A'
    REQ: <values> is a combination of '1' and '0'
    REQ: <variables> is a combination of lowercase alphabetical characters
    REQ: each letter only appears once in <variables>
    REQ: len(turns) == len(variables)
    REQ: len(variables) < len(values), ie. there is a next move
    >>> play2win(build_tree("(a*b)"), "EA", "ab", "0") == 0
    True
    >>> play2win(build_tree("-(-x+(-y*b))"), "AEA", "xyb", "1") == 1
    True
    '''

    # find who is trying to win with the next move
    # initialize the default value as result
    if turns[len(values)] == 'E':
        winner = 'E'
        default = 1
    else:
        winner = 'A'
        default = 0

    # case no wins, initialize result as no wins
    result = default

    # see if 'choosing' the default move will guarantee win
    default_win = play2win_helper(root, turns, variables,
                                  values + str(default), winner, result)

    # if default move guarantee win
    if default_win:
        # return default
        result = default

    else:
        # this is to avoid running the helper twice for some cases

        # if winnable with the non default choice then change result to it
        other_win = play2win_helper(root, turns, variables,
                                    values + str(1 - default), winner, result)
        if other_win:
            result = 1 - default
        # else result is still default b/c there are no possible wins

    return result


def play2win_helper(root, turns, variables, values, winner, wanted):
    '''
    (Formula, str, str, str, str, int) -> bool
    find if there is a guarantee winning strategy for the <winner>
    Takes in a FormulaTree rooted at <root> that represents a boolean formula
    <wanted> is the wanted outcome for <winner>
    The FormulaTree rooted at <root> represents a valid formula if:
    - <root> is not None
    - NotTree has only 1 child
    - OrTree and AndTree has left child and right child
    - child(ren) of connective are either (Leaf/OrTree/AndTree/NotTree)
    - The leaf of the tree is a LeafTree lowercase letter (variable)
    REQ: <root> represents a valid formula tree
    REQ: <turns> is a combination of 'E' and "A'
    REQ: <values> is a combination of '1' and '0'
    REQ: <variables> is a combination of lowercase alphabetical characters
    REQ: <winner> and <wanted> is either ('E' and 1) or ('A' and 0)
    REQ: each letter only appears once in <variables>
    REQ: len(turns) == len(variables)
    REQ: len(variables) < len(values), ie. there is a next move
    >>> tree = build_tree("(a*b)")
    >>> play2win_helper(tree, "EA", "ab", "0", 'A', 0)
    True
    >>> tree = build_tree("-(-x+(-y*b))")
    >>> play2win_helper(tree, "AEA", "xyb", "1", 'E', 1)
    True
    '''

    # see how many moves are left
    moves_left_num = len(variables) - len(values)

    # base case: evaluate the given case (from pick a move of p2w)
    if moves_left_num == 0:

        move = evaluate(root, variables, values)
        guarantee_win = move == wanted

        return guarantee_win

    # base case: pick 1 var to evaluate
    elif moves_left_num == 1:

        # all possible moves after current
        move0 = evaluate(root, variables, values + '0')
        move1 = evaluate(root, variables, values + '1')

        # find who's turn it is
        winner_turn = turns[len(values)] == winner

        # if winner/self turn
        if winner_turn:
            # if one of possible moves winner can make evaluates to <wanted>
            # then guarantee win is true
            guarantee_win = move0 == wanted or move1 == wanted

        # if opponent turn
        else:
            # if both of possible moves opponent can make evaluates to <wanted>
            # then guarantee win is true
            guarantee_win = move0 == wanted and move1 == wanted

        # return guarantee win
        return guarantee_win

    # else reursive step
    else:

        # pick values to the next move and see if those guarantee win
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
            # any move that does not guarantee win for <winner> makes
            # guarantee_win is False
            if (not default_win) or (not other_win):
                guarantee_win = False

            # if both moves guarantee win for <winner>
            # guarantee_win is True
            else:
                guarantee_win = True

    # return
    return guarantee_win
