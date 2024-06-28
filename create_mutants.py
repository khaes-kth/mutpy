import pandas as pd
import os
from mutpy import commandline
import sys

def main(argv):    
    human_eval = pd.read_json("ds/HumanEval.jsonl", lines=True)

    for i, d in enumerate(human_eval.to_dict('records')):
        src = d['prompt'] + d['canonical_solution']
        test = d['test']
        test = f'''from mutants.human_eval.m{i}.src{i} import {d["entry_point"]}
{test}
from unittest import TestCase 
class CalculatorTest(TestCase): 
	
	# test case for checking non prime nums 
	def test(self): 
		check({d["entry_point"]})'''
        cur_dir = f'mutants/human_eval/m{i}'
        os.system(f"mkdir {cur_dir}")
        with open(f"{cur_dir}/src{i}.py", "w") as f:
            f.write(src)
        with open(f"{cur_dir}/test{i}.py", "w") as f:
            f.write(test)
        try:
            commandline.main(f'/home/khesoem/phd/projects/leq/mutpy/mut.py --target mutants.human_eval.m{i}.src{i} --unit-test mutants.human_eval.m{i}.test{i} -m --runner unittest'.split(" "))
        except:
            pass            

if __name__ == '__main__':
    main(sys.argv)