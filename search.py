import argparse
from pyroFAE1 import pyroFAE1
from pyroFAE2 import pyroFAE2
from pyroFAE3 import pyroFAE3

parser = argparse.ArgumentParser(
    prog = 'search.py',
    description = 'Performs a search for an optimizied neural network weight set for a simulated robot using FAEry Algorithms')
parser.add_argument('-m', '--method', choices=['1', '2', '3'], default='1')

args = parser.parse_args()

if args.method == '1':
    evolutionary_algorithm = pyroFAE1()
elif args.method == '2':
    evolutionary_algorithm = pyroFAE2()
elif args.method == '3':
    evolutionary_algorithm = pyroFAE3()
else:
    exit()


evolutionary_algorithm.evolve()

exit()