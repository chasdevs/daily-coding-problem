#     cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.
#
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(cons_output):
    def return_first_param(a, b):
        return a
    return cons_output(return_first_param)

def cdr(cons_output):
    def return_last_param(a, b):
        return b
    return cons_output(return_last_param)

