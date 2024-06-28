from mutants.human_eval.m31.src31 import is_prime


METADATA = {}


def check(candidate):
    assert candidate(6) == False
    assert candidate(101) == True
    assert candidate(11) == True
    assert candidate(13441) == True
    assert candidate(61) == True
    assert candidate(4) == False
    assert candidate(1) == False
    assert candidate(5) == True
    assert candidate(11) == True
    assert candidate(17) == True
    assert candidate(5 * 17) == False
    assert candidate(11 * 7) == False
    assert candidate(13441 * 19) == False


from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check(is_prime)