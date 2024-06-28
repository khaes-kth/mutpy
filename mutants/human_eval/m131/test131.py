from mutants.human_eval.m131.src131 import digits
def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check(digits)