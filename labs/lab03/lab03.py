HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    if column == 0:
        return 1;
    elif row == column:
        return 1
    elif row > column and row >= 1 and column >= 1:
        return pascal(row-1,column) + pascal(row-1,column-1)
    else:
        return 0


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    def repeat(x):
        if n == 0:
            return x
        elif n == 1:
            return f(x)
        else:
            return f(repeated(f,n-1)(x))

    return repeat



def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 0:
        return 0
    else:
        if (x%10) == 8:
            return num_eights(x//10) + 1
        else:
            return num_eights(x//10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # result , i = 0, 1
    # increase = 1
    # while i <= n:
    #     if increase == 1:
    #         result = result + 1
    #     else:
    #         result = result - 1

    #     if num_eights(i) > 0 or i%8 == 0:
    #         increase =  1 - increase
    #     i += 1

    # return result

# this is ok for this function, but the recursion operations is too much
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif n == 3:
    #     return 3
    # else:
    #     if num_eights(n-1)>0 or (n-1)%8 == 0:
    #         return pingpong(n-2)
    #     else:
    #         return 2*pingpong(n-1) - pingpong(n-2)

    def helper(i,result,direction):
        if i == n:
            return result
        elif num_eights(i)>0 or i%8 == 0:
            return helper(i+1,result-direction,direction*-1)
        else:
            return helper(i+1,result+direction,direction)

    return helper(1,1,1)
