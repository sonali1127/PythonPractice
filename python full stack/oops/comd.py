import argparse

parser = argparse.ArgumentParser()

# Add command line arguments as optional arguments with defaults
parser.add_argument("--arg1", help="Description of argument 1", default=12, type=int)
parser.add_argument("--arg2", help="Description of argument 2", default=13, type=int)
##parser.add_argument("arg1", help="Description of argument 1", nargs="?", default=12, type=int)
# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.arg1)
print(args.arg2)

'''

nargs    Value Meaning	            ExampleInput	          Example Output
"?"	     Optional, at most 1 value	python script.py	      Uses default
"*"	     0 or more values	        python script.py a b c	  ['a', 'b', 'c']
"+"	     1 or more values	        python script.py a b	  ['a', 'b']
N	     Exactly N values	        python script.py a b	  ['a', 'b']
'''