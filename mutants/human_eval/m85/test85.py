from mutants.human_eval.m85.src85 import add
def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check(add)