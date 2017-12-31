# https://en.wikipedia.org/wiki/Triangular_number
# https://projecteuler.net/problem=1
# created 12.31.2017 by CB Fay
  
def L(a, b):
    return a * ((b-1)//a) * (((b-1)//a) + 1) // 2
    
print(L(3, 1000) + L(5, 1000) - L(15, 1000))


"""
Find the sum of multiples of a that are < limit b.

The largest multiple of 'a' we will add is:
((b-1)//a) * a

We can think of (b-1)//a as the highest...
triangular number; The bottom of the pyramid.

We subtract L(15, 1000) to account for repeated summations.
"""
