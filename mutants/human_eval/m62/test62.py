from mutants.human_eval.m62.src62 import derivative


METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert candidate([1, 2, 3]) == [2, 6]
    assert candidate([3, 2, 1]) == [2, 2]
    assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
    assert candidate([1]) == []


from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check(derivative)