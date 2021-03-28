"""
Logan Mondal Bhamidipaty
March 27, 2021

Automatically generates "dense" crosswords given a desire output dimension
and input word list.

Inspiration for this project came from an in-class example
from Lecturer Keith for CS 106B @ Stanford (Winter 2021).
(LINK TO PRESENTATION: https://web.stanford.edu/class/cs106b/lectures/10/Slides10.pdf)

Q: What's different with my implementation?
A: Besides being in Python, my code also doesn't use function recursion;
instead it relies on Python generators and deque to implement backtracking.
"""
import numpy as np
from collections import deque
import time

M = 3
N = 3


class Lexicon:
    def __init__(self, filename):
        self.prefixes = [set() for i in range(M)]
        self.vert = set()
        self.horz = set()
        for line in open(filename):
            line = line.strip()
            if len(line) == M:
                for i in range(1, len(line)):
                    self.prefixes[i].add(line[:i])
                self.vert.add(line)
            if len(line) == N:
                self.horz.add(line)


def main():
    puzzle = np.empty((M, N), dtype=str)
    eng = Lexicon("data/words_1000.txt")
    print("Finding solution...")
    if finish(puzzle, eng):
        print(puzzle)
        print("Solution found!")
    else:
        print("No solution found.")


def finish(puzzle: np.ndarray, eng: Lexicon):
    row_index = 0
    bank = deque([])
    generators = [make_generator(eng.horz) for i in range(M)]
    while True:
        try:
            gen = generators[row_index]
            word = next(gen)
            insert(puzzle, row_index, word, bank)
            if len(bank) < M:
                if possible(puzzle, eng):
                    row_index += 1
                else:
                    undo(puzzle, row_index, bank)
            else:  # len(bank) == M:
                if valid(puzzle, eng):
                    return True
                else:
                    undo(puzzle, row_index, bank)
        except StopIteration:
            if row_index == 0:
                return False
            else:
                undo(puzzle, row_index, bank)
                generators[row_index] = make_generator(eng.horz)
                row_index -= 1


def insert(puzzle: np.ndarray, row_index: int, word: str, bank: deque) -> int:
    puzzle[row_index] = tokenize(word)
    bank.append(word)


def undo(puzzle: np.ndarray, row_index: int, bank: deque) -> int:
    puzzle[row_index] = np.ndarray((1, N), dtype=str)
    bank.pop()


def make_generator(s):
    yield from s


def valid(puzzle, eng):
    return all([''.join(col) in eng.vert for col in puzzle.T])


def tokenize(s):
    return [ch for ch in s]


def possible(puzzle: np.ndarray, eng):
    for col in puzzle.T:
        prefix = ''.join(col)
        if prefix not in eng.prefixes[len(prefix)]:
            return False
    return True


if __name__ == "__main__":
    t0 = time.time()
    main()
    t1 = time.time()
    print(t1 - t0)