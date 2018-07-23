if(__name__ == '__main__'):

    # just test cases ignore pls

    # base p2w cases
    # root = build_tree('x')
    # a = play2win(root, 'E', 'x', '') == 1
    # print('can win: True', play2win_helper(root, 'E', 'x', '', 'E', 1))
    # print('1. returns:', a, '\n')

    # root = build_tree('x')
    # a = play2win(root, 'A', 'x', '') == 0
    # print('can win: True', play2win_helper(root, 'A', 'x', '', 'A', 0))
    # print('2. returns:', a, '\n')

    # root = build_tree('(x*y)')
    # a = play2win(root, 'EA', 'xy', '') == 1
    # print('can win: False', play2win_helper(root, 'EA', 'xy', '', 'E', 1))
    # print('3. returns:', a, '\n')

    # root = build_tree('(x*y)')
    # a = play2win(root, 'EE', 'xy', '') == 1
    # print('can win: True', play2win_helper(root, 'EE', 'xy', '', 'E', 1))
    # print('4. returns:', a, '\n')

    # root = build_tree('(x*y)')
    # a = play2win(root, 'AE', 'xy', '') == 0
    # print('can win: True', play2win_helper(root, 'AE', 'xy', '', 'A', 0))
    # print('5. returns:', a, '\n')

    # root = build_tree('(x*y)')
    # a = play2win(root, 'AA', 'xy', '') == 0
    # print('can win: True', play2win_helper(root, 'AA', 'xy', '', 'A', 0))
    # print('6. returns:', a, '\n')

    # root = build_tree('(x+y)')
    # a = play2win(root, 'EA', 'xy', '') == 1
    # print('can win: True', play2win_helper(root, 'EA', 'xy', '', 'E', 1))
    # print('7. returns:', a, '\n')

    # root = build_tree('(x+y)')
    # a = play2win(root, 'EE', 'xy', '') == 1
    # print('can win: True', play2win_helper(root, 'EE', 'xy', '', 'E', 1))
    # print('8. returns:', a, '\n')

    # root = build_tree('(x+y)')
    # a = play2win(root, 'AE', 'xy', '') == 0
    # print('can win: False', play2win_helper(root, 'AE', 'xy', '', 'A', 0))
    # print('9. returns:', a, '\n')

    # root = build_tree('(x+y)')
    # a = play2win(root, 'AA', 'xy', '') == 0
    # print('can win: True', play2win_helper(root, 'AA', 'xy', '', 'A', 0))
    # print('10. returns:', a, '\n')

    # root = build_tree('-x')
    # a = play2win(root, 'A', 'x', '') == 1
    # print('can win: True', play2win_helper(root, 'A', 'x', '', 'A', 0))
    # print('11. returns:', a, '\n')

    # root = build_tree('-x')
    # a = play2win(root, 'E', 'x', '') == 0
    # print('can win: True', play2win_helper(root, 'E', 'x', '', 'E', 1))
    # print('12. returns:', a, '\n')

    # # hard p2w cases
    # root = build_tree('((-x*y)+z)')
    # a = play2win(root, 'EAE', 'xyz', '') == 1
    # print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    # print('13. returns:', a, '\n')

    # root = build_tree('((-x+y)*z)')
    # a = play2win(root, 'EAE', 'xyz', '') == 0
    # print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    # print('13.1. returns:', a, '\n')

    # # DO EXAMPLES, TEST FOR already picked

    # root = build_tree('((-x+y)*z)')
    # a = play2win(root, 'EAE', 'xyz', '') == 0
    # print('can win: True', play2win_helper(root, 'EAE', 'xyz', '', 'E', 1))
    # print('13.1. returns:', a, '\n')

    # root = build_tree('((-x+y)*z)')
    # a = play2win(root, 'EAE', 'xyz', '1') == 0
    # print('can win: True', play2win_helper(root, 'EAE', 'xyz', '1', 'A', 0))
    # print('13.2. returns:', a, '\n')

    # root = build_tree('((-x+y)*z)')
    # a = play2win(root, 'EAE', 'xyz', '10') == 1
    # print('can win: False', play2win_helper(root, 'EAE', 'xyz', '10', 'E', 1))
    # print('13.3. returns:', a, '\n')

    # root = build_tree('((-x+y)*z)')
    # a = play2win(root, 'EAE', 'xyz', '11') == 1
    # print('can win: True', play2win_helper(root, 'EAE', 'xyz', '11', 'E', 1))
    # print('13.3. returns:', a, '\n')

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
    pass