# Kobe Luna
# Student ID: P21590963
# Problem 1

import math

class MyMath:
    n = 115249

    @staticmethod
    def prime(num, i = 2):
        if(num <= 2):
            if(num == 2):
                return True
            else:
                False

        if(num % i == 0):
            return False

        if(i * i > num):
            return True

        return MyMath.prime(num, i + 1)
    
    @classmethod
    def gcd(cls,m,l):
        while l !=0:
            MyMath.n, l=l, MyMath.n%l

        return MyMath.n

k = MyMath()
print(k.n)
print(k.prime(k.n))
print(k.gcd(k.n,3))
