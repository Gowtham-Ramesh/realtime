import numpy as np
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Your Name")
args = parser.parse_args()

a = []
b="hi"
c="Naga"
for i in range(0,5):
	a.append(i)

print(*a, b, c, sep=",")
print(args.name)
#print(b)
#print(c)
#print("it should work now")