# CrosswordGenerator
generate "dense" crosswords

@ Logan Mondal Bhamidipaty

Automatically generates "dense" crosswords given a desire output dimensionand input word list.

Inspiration for this project came from an in-class example
from Lecturer Keith for CS 106B @ Stanford (Winter 2021).
(LINK TO PRESENTATION: https://web.stanford.edu/class/cs106b/lectures/10/Slides10.pdf)

Q: What's different with my implementation?
A: Besides being in Python, my code also doesn't use function recursion;
instead it relies on Python generators and deque to implement backtracking.
