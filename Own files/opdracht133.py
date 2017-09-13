from unittest import *
import doctest
import io
from contextlib import redirect_stdout

def function_to_unittest(list):
    ordered = []
    for item in list:
        if item < 0:
            item *= -1
            item += 1

        if item % 2 == 1:
            if not is_prime(item):
                continue
        ordered = insert(item, ordered)
    return ordered


def insert(item, list):
    for index in range(0, len(list)):
        if list[index] > item:
            list.insert(index, item)
            break
    else:
        list.append(item)

    return list


def is_prime(n):
    if n < 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

class ExerciseTest(TestCase):
    def setUp(self):
        self.sorting = [4, 5, 1, 3, 2]
        self.negativeplusone = [-5, -6, -8]
        self.nonprimeodd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.complex = [-5, 12, -30, -48, 11]
        pass # Pass om syntax errors te voorkomen in de notebook

    #TODO definieer hieronder je tests
    # LET OP: de functies die je als tests schrijft moeten in de naam met 'test' beginnen!
    def test_sortnumbers(self):
        output = function_to_unittest(self.sorting)

        self.assertEqual([1, 2, 3, 4, 5], output, "test failed, Program does not sort")# does not remove 1 while it is a prime number

    def test_negativeplusone(self):
        output = function_to_unittest(self.negativeplusone)

        self.assertEqual([6, 7], output, "Test failed, program does not handle negative numbers correctly")

    def test_nonprimeodd(self):
        output = function_to_unittest(self.nonprimeodd)

        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8], output, "Test failed. program does not remove nonprime odd numbers")

    def test_complex(self):
        output = function_to_unittest(self.complex)

        self.assertEqual([6, 11, 12, 31], output, "Test failed. program is not able to handle multiple problems together")

test = ExerciseTest()
suite = TestLoader().loadTestsFromModule(test)
TextTestRunner().run(suite)
