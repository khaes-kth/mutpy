from mutants.human_eval.m75.src75 import is_multiply_prime
def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check(is_multiply_prime)