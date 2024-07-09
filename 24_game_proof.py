from collections import Counter, defaultdict
from itertools import product, permutations
from math import factorial, prod
from functools import lru_cache
from tqdm import tqdm


@lru_cache(maxsize=None)
def evaluate_all_expressions(a, b, c, d):
    results = set()

    expressions = [
        ("a + b + c + d", lambda: a + b + c + d),
        ("a + b + c - d", lambda: a + b + c - d),
        ("a + b + c * d", lambda: a + b + c * d),
        ("a + b + c / d", lambda: a + b + c / d),
        ("a + b - c + d", lambda: a + b - c + d),
        ("a + b - c - d", lambda: a + b - c - d),
        ("a + b - c * d", lambda: a + b - c * d),
        ("a + b - c / d", lambda: a + b - c / d),
        ("a + b * c + d", lambda: a + b * c + d),
        ("a + b * c - d", lambda: a + b * c - d),
        ("a + b * c * d", lambda: a + b * c * d),
        ("a + b * c / d", lambda: a + b * c / d),
        ("a + b / c + d", lambda: a + b / c + d),
        ("a + b / c - d", lambda: a + b / c - d),
        ("a + b / c * d", lambda: a + b / c * d),
        ("a + b / c / d", lambda: a + b / c / d),
        ("a - b + c + d", lambda: a - b + c + d),
        ("a - b + c - d", lambda: a - b + c - d),
        ("a - b + c * d", lambda: a - b + c * d),
        ("a - b + c / d", lambda: a - b + c / d),
        ("a - b - c + d", lambda: a - b - c + d),
        ("a - b - c - d", lambda: a - b - c - d),
        ("a - b - c * d", lambda: a - b - c * d),
        ("a - b - c / d", lambda: a - b - c / d),
        ("a - b * c + d", lambda: a - b * c + d),
        ("a - b * c - d", lambda: a - b * c - d),
        ("a - b * c * d", lambda: a - b * c * d),
        ("a - b * c / d", lambda: a - b * c / d),
        ("a - b / c + d", lambda: a - b / c + d),
        ("a - b / c - d", lambda: a - b / c - d),
        ("a - b / c * d", lambda: a - b / c * d),
        ("a - b / c / d", lambda: a - b / c / d),
        ("a * b + c + d", lambda: a * b + c + d),
        ("a * b + c - d", lambda: a * b + c - d),
        ("a * b + c * d", lambda: a * b + c * d),
        ("a * b + c / d", lambda: a * b + c / d),
        ("a * b - c + d", lambda: a * b - c + d),
        ("a * b - c - d", lambda: a * b - c - d),
        ("a * b - c * d", lambda: a * b - c * d),
        ("a * b - c / d", lambda: a * b - c / d),
        ("a * b * c + d", lambda: a * b * c + d),
        ("a * b * c - d", lambda: a * b * c - d),
        ("a * b * c * d", lambda: a * b * c * d),
        ("a * b * c / d", lambda: a * b * c / d),
        ("a * b / c + d", lambda: a * b / c + d),
        ("a * b / c - d", lambda: a * b / c - d),
        ("a * b / c * d", lambda: a * b / c * d),
        ("a * b / c / d", lambda: a * b / c / d),
        ("a / b + c + d", lambda: a / b + c + d),
        ("a / b + c - d", lambda: a / b + c - d),
        ("a / b + c * d", lambda: a / b + c * d),
        ("a / b + c / d", lambda: a / b + c / d),
        ("a / b - c + d", lambda: a / b - c + d),
        ("a / b - c - d", lambda: a / b - c - d),
        ("a / b - c * d", lambda: a / b - c * d),
        ("a / b - c / d", lambda: a / b - c / d),
        ("a / b * c + d", lambda: a / b * c + d),
        ("a / b * c - d", lambda: a / b * c - d),
        ("a / b * c * d", lambda: a / b * c * d),
        ("a / b * c / d", lambda: a / b * c / d),
        ("a / b / c + d", lambda: a / b / c + d),
        ("a / b / c - d", lambda: a / b / c - d),
        ("a / b / c * d", lambda: a / b / c * d),
        ("a / b / c / d", lambda: a / b / c / d),
        # Parenthesized groupings
        ("(a + b) + (c + d)", lambda: (a + b) + (c + d)),
        ("(a + b) + (c - d)", lambda: (a + b) + (c - d)),
        ("(a + b) + (c * d)", lambda: (a + b) + (c * d)),
        ("(a + b) + (c / d)", lambda: (a + b) + (c / d)),
        ("(a + b) - (c + d)", lambda: (a + b) - (c + d)),
        ("(a + b) - (c - d)", lambda: (a + b) - (c - d)),
        ("(a + b) - (c * d)", lambda: (a + b) - (c * d)),
        ("(a + b) - (c / d)", lambda: (a + b) - (c / d)),
        ("(a + b) * (c + d)", lambda: (a + b) * (c + d)),
        ("(a + b) * (c - d)", lambda: (a + b) * (c - d)),
        ("(a + b) * (c * d)", lambda: (a + b) * (c * d)),
        ("(a + b) * (c / d)", lambda: (a + b) * (c / d)),
        ("(a + b) / (c + d)", lambda: (a + b) / (c + d)),
        ("(a + b) / (c - d)", lambda: (a + b) / (c - d)),
        ("(a + b) / (c * d)", lambda: (a + b) / (c * d)),
        ("(a + b) / (c / d)", lambda: (a + b) / (c / d)),
        ("(a - b) + (c + d)", lambda: (a - b) + (c + d)),
        ("(a - b) + (c - d)", lambda: (a - b) + (c - d)),
        ("(a - b) + (c * d)", lambda: (a - b) + (c * d)),
        ("(a - b) + (c / d)", lambda: (a - b) + (c / d)),
        ("(a - b) - (c + d)", lambda: (a - b) - (c + d)),
        ("(a - b) - (c - d)", lambda: (a - b) - (c - d)),
        ("(a - b) - (c * d)", lambda: (a - b) - (c * d)),
        ("(a - b) - (c / d)", lambda: (a - b) - (c / d)),
        ("(a - b) * (c + d)", lambda: (a - b) * (c + d)),
        ("(a - b) * (c - d)", lambda: (a - b) * (c - d)),
        ("(a - b) * (c * d)", lambda: (a - b) * (c * d)),
        ("(a - b) * (c / d)", lambda: (a - b) * (c / d)),
        ("(a - b) / (c + d)", lambda: (a - b) / (c + d)),
        ("(a - b) / (c - d)", lambda: (a - b) / (c - d)),
        ("(a - b) / (c * d)", lambda: (a - b) / (c * d)),
        ("(a - b) / (c / d)", lambda: (a - b) / (c / d)),
        ("(a * b) + (c + d)", lambda: (a * b) + (c + d)),
        ("(a * b) + (c - d)", lambda: (a * b) + (c - d)),
        ("(a * b) + (c * d)", lambda: (a * b) + (c * d)),
        ("(a * b) + (c / d)", lambda: (a * b) + (c / d)),
        ("(a * b) - (c + d)", lambda: (a * b) - (c + d)),
        ("(a * b) - (c - d)", lambda: (a * b) - (c - d)),
        ("(a * b) - (c * d)", lambda: (a * b) - (c * d)),
        ("(a * b) - (c / d)", lambda: (a * b) - (c / d)),
        ("(a * b) * (c + d)", lambda: (a * b) * (c + d)),
        ("(a * b) * (c - d)", lambda: (a * b) * (c - d)),
        ("(a * b) * (c * d)", lambda: (a * b) * (c * d)),
        ("(a * b) * (c / d)", lambda: (a * b) * (c / d)),
        ("(a * b) / (c + d)", lambda: (a * b) / (c + d)),
        ("(a * b) / (c - d)", lambda: (a * b) / (c - d)),
        ("(a * b) / (c * d)", lambda: (a * b) / (c * d)),
        ("(a * b) / (c / d)", lambda: (a * b) / (c / d)),
        ("(a / b) + (c + d)", lambda: (a / b) + (c + d)),
        ("(a / b) + (c - d)", lambda: (a / b) + (c - d)),
        ("(a / b) + (c * d)", lambda: (a / b) + (c * d)),
        ("(a / b) + (c / d)", lambda: (a / b) + (c / d)),
        ("(a / b) - (c + d)", lambda: (a / b) - (c + d)),
        ("(a / b) - (c - d)", lambda: (a / b) - (c - d)),
        ("(a / b) - (c * d)", lambda: (a / b) - (c * d)),
        ("(a / b) - (c / d)", lambda: (a / b) - (c / d)),
        ("(a / b) * (c + d)", lambda: (a / b) * (c + d)),
        ("(a / b) * (c - d)", lambda: (a / b) * (c - d)),
        ("(a / b) * (c * d)", lambda: (a / b) * (c * d)),
        ("(a / b) * (c / d)", lambda: (a / b) * (c / d)),
        ("(a / b) / (c + d)", lambda: (a / b) / (c + d)),
        ("(a / b) / (c - d)", lambda: (a / b) / (c - d)),
        ("(a / b) / (c * d)", lambda: (a / b) / (c * d)),
        ("(a / b) / (c / d)", lambda: (a / b) / (c / d)),
        ("((a + b) + c) + d", lambda: ((a + b) + c) + d),
        ("((a + b) + c) - d", lambda: ((a + b) + c) - d),
        ("((a + b) + c) * d", lambda: ((a + b) + c) * d),
        ("((a + b) + c) / d", lambda: ((a + b) + c) / d),
        ("((a + b) - c) + d", lambda: ((a + b) - c) + d),
        ("((a + b) - c) - d", lambda: ((a + b) - c) - d),
        ("((a + b) - c) * d", lambda: ((a + b) - c) * d),
        ("((a + b) - c) / d", lambda: ((a + b) - c) / d),
        ("((a + b) * c) + d", lambda: ((a + b) * c) + d),
        ("((a + b) * c) - d", lambda: ((a + b) * c) - d),
        ("((a + b) * c) * d", lambda: ((a + b) * c) * d),
        ("((a + b) * c) / d", lambda: ((a + b) * c) / d),
        ("((a + b) / c) + d", lambda: ((a + b) / c) + d),
        ("((a + b) / c) - d", lambda: ((a + b) / c) - d),
        ("((a + b) / c) * d", lambda: ((a + b) / c) * d),
        ("((a + b) / c) / d", lambda: ((a + b) / c) / d),
        ("((a - b) + c) + d", lambda: ((a - b) + c) + d),
        ("((a - b) + c) - d", lambda: ((a - b) + c) - d),
        ("((a - b) + c) * d", lambda: ((a - b) + c) * d),
        ("((a - b) + c) / d", lambda: ((a - b) + c) / d),
        ("((a - b) - c) + d", lambda: ((a - b) - c) + d),
        ("((a - b) - c) - d", lambda: ((a - b) - c) - d),
        ("((a - b) - c) * d", lambda: ((a - b) - c) * d),
        ("((a - b) - c) / d", lambda: ((a - b) - c) / d),
        ("((a - b) * c) + d", lambda: ((a - b) * c) + d),
        ("((a - b) * c) - d", lambda: ((a - b) * c) - d),
        ("((a - b) * c) * d", lambda: ((a - b) * c) * d),
        ("((a - b) * c) / d", lambda: ((a - b) * c) / d),
        ("((a - b) / c) + d", lambda: ((a - b) / c) + d),
        ("((a - b) / c) - d", lambda: ((a - b) / c) - d),
        ("((a - b) / c) * d", lambda: ((a - b) / c) * d),
        ("((a - b) / c) / d", lambda: ((a - b) / c) / d),
        ("((a * b) + c) + d", lambda: ((a * b) + c) + d),
        ("((a * b) + c) - d", lambda: ((a * b) + c) - d),
        ("((a * b) + c) * d", lambda: ((a * b) + c) * d),
        ("((a * b) + c) / d", lambda: ((a * b) + c) / d),
        ("((a * b) - c) + d", lambda: ((a * b) - c) + d),
        ("((a * b) - c) - d", lambda: ((a * b) - c) - d),
        ("((a * b) - c) * d", lambda: ((a * b) - c) * d),
        ("((a * b) - c) / d", lambda: ((a * b) - c) / d),
        ("((a * b) * c) + d", lambda: ((a * b) * c) + d),
        ("((a * b) * c) - d", lambda: ((a * b) * c) - d),
        ("((a * b) * c) * d", lambda: ((a * b) * c) * d),
        ("((a * b) * c) / d", lambda: ((a * b) * c) / d),
        ("((a * b) / c) + d", lambda: ((a * b) / c) + d),
        ("((a * b) / c) - d", lambda: ((a * b) / c) - d),
        ("((a * b) / c) * d", lambda: ((a * b) / c) * d),
        ("((a * b) / c) / d", lambda: ((a * b) / c) / d),
        ("((a / b) + c) + d", lambda: ((a / b) + c) + d),
        ("((a / b) + c) - d", lambda: ((a / b) + c) - d),
        ("((a / b) + c) * d", lambda: ((a / b) + c) * d),
        ("((a / b) + c) / d", lambda: ((a / b) + c) / d),
        ("((a / b) - c) + d", lambda: ((a / b) - c) + d),
        ("((a / b) - c) - d", lambda: ((a / b) - c) - d),
        ("((a / b) - c) * d", lambda: ((a / b) - c) * d),
        ("((a / b) - c) / d", lambda: ((a / b) - c) / d),
        ("((a / b) * c) + d", lambda: ((a / b) * c) + d),
        ("((a / b) * c) - d", lambda: ((a / b) * c) - d),
        ("((a / b) * c) * d", lambda: ((a / b) * c) * d),
        ("((a / b) * c) / d", lambda: ((a / b) * c) / d),
        ("((a / b) / c) + d", lambda: ((a / b) / c) + d),
        ("((a / b) / c) - d", lambda: ((a / b) / c) - d),
        ("((a / b) / c) * d", lambda: ((a / b) / c) * d),
        ("((a / b) / c) / d", lambda: ((a / b) / c) / d),
        ("(a + (b + c)) + d", lambda: (a + (b + c)) + d),
        ("(a + (b + c)) - d", lambda: (a + (b + c)) - d),
        ("(a + (b + c)) * d", lambda: (a + (b + c)) * d),
        ("(a + (b + c)) / d", lambda: (a + (b + c)) / d),
        ("(a + (b - c)) + d", lambda: (a + (b - c)) + d),
        ("(a + (b - c)) - d", lambda: (a + (b - c)) - d),
        ("(a + (b - c)) * d", lambda: (a + (b - c)) * d),
        ("(a + (b - c)) / d", lambda: (a + (b - c)) / d),
        ("(a + (b * c)) + d", lambda: (a + (b * c)) + d),
        ("(a + (b * c)) - d", lambda: (a + (b * c)) - d),
        ("(a + (b * c)) * d", lambda: (a + (b * c)) * d),
        ("(a + (b * c)) / d", lambda: (a + (b * c)) / d),
        ("(a + (b / c)) + d", lambda: (a + (b / c)) + d),
        ("(a + (b / c)) - d", lambda: (a + (b / c)) - d),
        ("(a + (b / c)) * d", lambda: (a + (b / c)) * d),
        ("(a + (b / c)) / d", lambda: (a + (b / c)) / d),
        ("(a - (b + c)) + d", lambda: (a - (b + c)) + d),
        ("(a - (b + c)) - d", lambda: (a - (b + c)) - d),
        ("(a - (b + c)) * d", lambda: (a - (b + c)) * d),
        ("(a - (b + c)) / d", lambda: (a - (b + c)) / d),
        ("(a - (b - c)) + d", lambda: (a - (b - c)) + d),
        ("(a - (b - c)) - d", lambda: (a - (b - c)) - d),
        ("(a - (b - c)) * d", lambda: (a - (b - c)) * d),
        ("(a - (b - c)) / d", lambda: (a - (b - c)) / d),
        ("(a - (b * c)) + d", lambda: (a - (b * c)) + d),
        ("(a - (b * c)) - d", lambda: (a - (b * c)) - d),
        ("(a - (b * c)) * d", lambda: (a - (b * c)) * d),
        ("(a - (b * c)) / d", lambda: (a - (b * c)) / d),
        ("(a - (b / c)) + d", lambda: (a - (b / c)) + d),
        ("(a - (b / c)) - d", lambda: (a - (b / c)) - d),
        ("(a - (b / c)) * d", lambda: (a - (b / c)) * d),
        ("(a - (b / c)) / d", lambda: (a - (b / c)) / d),
        ("(a * (b + c)) + d", lambda: (a * (b + c)) + d),
        ("(a * (b + c)) - d", lambda: (a * (b + c)) - d),
        ("(a * (b + c)) * d", lambda: (a * (b + c)) * d),
        ("(a * (b + c)) / d", lambda: (a * (b + c)) / d),
        ("(a * (b - c)) + d", lambda: (a * (b - c)) + d),
        ("(a * (b - c)) - d", lambda: (a * (b - c)) - d),
        ("(a * (b - c)) * d", lambda: (a * (b - c)) * d),
        ("(a * (b - c)) / d", lambda: (a * (b - c)) / d),
        ("(a * (b * c)) + d", lambda: (a * (b * c)) + d),
        ("(a * (b * c)) - d", lambda: (a * (b * c)) - d),
        ("(a * (b * c)) * d", lambda: (a * (b * c)) * d),
        ("(a * (b * c)) / d", lambda: (a * (b * c)) / d),
        ("(a * (b / c)) + d", lambda: (a * (b / c)) + d),
        ("(a * (b / c)) - d", lambda: (a * (b / c)) - d),
        ("(a * (b / c)) * d", lambda: (a * (b / c)) * d),
        ("(a * (b / c)) / d", lambda: (a * (b / c)) / d),
        ("(a / (b + c)) + d", lambda: (a / (b + c)) + d),
        ("(a / (b + c)) - d", lambda: (a / (b + c)) - d),
        ("(a / (b + c)) * d", lambda: (a / (b + c)) * d),
        ("(a / (b + c)) / d", lambda: (a / (b + c)) / d),
        ("(a / (b - c)) + d", lambda: (a / (b - c)) + d),
        ("(a / (b - c)) - d", lambda: (a / (b - c)) - d),
        ("(a / (b - c)) * d", lambda: (a / (b - c)) * d),
        ("(a / (b - c)) / d", lambda: (a / (b - c)) / d),
        ("(a / (b * c)) + d", lambda: (a / (b * c)) + d),
        ("(a / (b * c)) - d", lambda: (a / (b * c)) - d),
        ("(a / (b * c)) * d", lambda: (a / (b * c)) * d),
        ("(a / (b * c)) / d", lambda: (a / (b * c)) / d),
        ("(a / (b / c)) + d", lambda: (a / (b / c)) + d),
        ("(a / (b / c)) - d", lambda: (a / (b / c)) - d),
        ("(a / (b / c)) * d", lambda: (a / (b / c)) * d),
        ("(a / (b / c)) / d", lambda: (a / (b / c)) / d),
        ("a + ((b + c) + d)", lambda: a + ((b + c) + d)),
        ("a + ((b + c) - d)", lambda: a + ((b + c) - d)),
        ("a + ((b + c) * d)", lambda: a + ((b + c) * d)),
        ("a + ((b + c) / d)", lambda: a + ((b + c) / d)),
        ("a + ((b - c) + d)", lambda: a + ((b - c) + d)),
        ("a + ((b - c) - d)", lambda: a + ((b - c) - d)),
        ("a + ((b - c) * d)", lambda: a + ((b - c) * d)),
        ("a + ((b - c) / d)", lambda: a + ((b - c) / d)),
        ("a + ((b * c) + d)", lambda: a + ((b * c) + d)),
        ("a + ((b * c) - d)", lambda: a + ((b * c) - d)),
        ("a + ((b * c) * d)", lambda: a + ((b * c) * d)),
        ("a + ((b * c) / d)", lambda: a + ((b * c) / d)),
        ("a + ((b / c) + d)", lambda: a + ((b / c) + d)),
        ("a + ((b / c) - d)", lambda: a + ((b / c) - d)),
        ("a + ((b / c) * d)", lambda: a + ((b / c) * d)),
        ("a + ((b / c) / d)", lambda: a + ((b / c) / d)),
        ("a - ((b + c) + d)", lambda: a - ((b + c) + d)),
        ("a - ((b + c) - d)", lambda: a - ((b + c) - d)),
        ("a - ((b + c) * d)", lambda: a - ((b + c) * d)),
        ("a - ((b + c) / d)", lambda: a - ((b + c) / d)),
        ("a - ((b - c) + d)", lambda: a - ((b - c) + d)),
        ("a - ((b - c) - d)", lambda: a - ((b - c) - d)),
        ("a - ((b - c) * d)", lambda: a - ((b - c) * d)),
        ("a - ((b - c) / d)", lambda: a - ((b - c) / d)),
        ("a - ((b * c) + d)", lambda: a - ((b * c) + d)),
        ("a - ((b * c) - d)", lambda: a - ((b * c) - d)),
        ("a - ((b * c) * d)", lambda: a - ((b * c) * d)),
        ("a - ((b * c) / d)", lambda: a - ((b * c) / d)),
        ("a - ((b / c) + d)", lambda: a - ((b / c) + d)),
        ("a - ((b / c) - d)", lambda: a - ((b / c) - d)),
        ("a - ((b / c) * d)", lambda: a - ((b / c) * d)),
        ("a - ((b / c) / d)", lambda: a - ((b / c) / d)),
        ("a * ((b + c) + d)", lambda: a * ((b + c) + d)),
        ("a * ((b + c) - d)", lambda: a * ((b + c) - d)),
        ("a * ((b + c) * d)", lambda: a * ((b + c) * d)),
        ("a * ((b + c) / d)", lambda: a * ((b + c) / d)),
        ("a * ((b - c) + d)", lambda: a * ((b - c) + d)),
        ("a * ((b - c) - d)", lambda: a * ((b - c) - d)),
        ("a * ((b - c) * d)", lambda: a * ((b - c) * d)),
        ("a * ((b - c) / d)", lambda: a * ((b - c) / d)),
        ("a * ((b * c) + d)", lambda: a * ((b * c) + d)),
        ("a * ((b * c) - d)", lambda: a * ((b * c) - d)),
        ("a * ((b * c) * d)", lambda: a * ((b * c) * d)),
        ("a * ((b * c) / d)", lambda: a * ((b * c) / d)),
        ("a * ((b / c) + d)", lambda: a * ((b / c) + d)),
        ("a * ((b / c) - d)", lambda: a * ((b / c) - d)),
        ("a * ((b / c) * d)", lambda: a * ((b / c) * d)),
        ("a * ((b / c) / d)", lambda: a * ((b / c) / d)),
        ("a / ((b + c) + d)", lambda: a / ((b + c) + d)),
        ("a / ((b + c) - d)", lambda: a / ((b + c) - d)),
        ("a / ((b + c) * d)", lambda: a / ((b + c) * d)),
        ("a / ((b + c) / d)", lambda: a / ((b + c) / d)),
        ("a / ((b - c) + d)", lambda: a / ((b - c) + d)),
        ("a / ((b - c) - d)", lambda: a / ((b - c) - d)),
        ("a / ((b - c) * d)", lambda: a / ((b - c) * d)),
        ("a / ((b - c) / d)", lambda: a / ((b - c) / d)),
        ("a / ((b * c) + d)", lambda: a / ((b * c) + d)),
        ("a / ((b * c) - d)", lambda: a / ((b * c) - d)),
        ("a / ((b * c) * d)", lambda: a / ((b * c) * d)),
        ("a / ((b * c) / d)", lambda: a / ((b * c) / d)),
        ("a / ((b / c) + d)", lambda: a / ((b / c) + d)),
        ("a / ((b / c) - d)", lambda: a / ((b / c) - d)),
        ("a / ((b / c) * d)", lambda: a / ((b / c) * d)),
        ("a / ((b / c) / d)", lambda: a / ((b / c) / d)),
        ("a + (b + (c + d))", lambda: a + (b + (c + d))),
        ("a + (b + (c - d))", lambda: a + (b + (c - d))),
        ("a + (b + (c * d))", lambda: a + (b + (c * d))),
        ("a + (b + (c / d))", lambda: a + (b + (c / d))),
        ("a + (b - (c + d))", lambda: a + (b - (c + d))),
        ("a + (b - (c - d))", lambda: a + (b - (c - d))),
        ("a + (b - (c * d))", lambda: a + (b - (c * d))),
        ("a + (b - (c / d))", lambda: a + (b - (c / d))),
        ("a + (b * (c + d))", lambda: a + (b * (c + d))),
        ("a + (b * (c - d))", lambda: a + (b * (c - d))),
        ("a + (b * (c * d))", lambda: a + (b * (c * d))),
        ("a + (b * (c / d))", lambda: a + (b * (c / d))),
        ("a + (b / (c + d))", lambda: a + (b / (c + d))),
        ("a + (b / (c - d))", lambda: a + (b / (c - d))),
        ("a + (b / (c * d))", lambda: a + (b / (c * d))),
        ("a + (b / (c / d))", lambda: a + (b / (c / d))),
        ("a - (b + (c + d))", lambda: a - (b + (c + d))),
        ("a - (b + (c - d))", lambda: a - (b + (c - d))),
        ("a - (b + (c * d))", lambda: a - (b + (c * d))),
        ("a - (b + (c / d))", lambda: a - (b + (c / d))),
        ("a - (b - (c + d))", lambda: a - (b - (c + d))),
        ("a - (b - (c - d))", lambda: a - (b - (c - d))),
        ("a - (b - (c * d))", lambda: a - (b - (c * d))),
        ("a - (b - (c / d))", lambda: a - (b - (c / d))),
        ("a - (b * (c + d))", lambda: a - (b * (c + d))),
        ("a - (b * (c - d))", lambda: a - (b * (c - d))),
        ("a - (b * (c * d))", lambda: a - (b * (c * d))),
        ("a - (b * (c / d))", lambda: a - (b * (c / d))),
        ("a - (b / (c + d))", lambda: a - (b / (c + d))),
        ("a - (b / (c - d))", lambda: a - (b / (c - d))),
        ("a - (b / (c * d))", lambda: a - (b / (c * d))),
        ("a - (b / (c / d))", lambda: a - (b / (c / d))),
        ("a * (b + (c + d))", lambda: a * (b + (c + d))),
        ("a * (b + (c - d))", lambda: a * (b + (c - d))),
        ("a * (b + (c * d))", lambda: a * (b + (c * d))),
        ("a * (b + (c / d))", lambda: a * (b + (c / d))),
        ("a * (b - (c + d))", lambda: a * (b - (c + d))),
        ("a * (b - (c - d))", lambda: a * (b - (c - d))),
        ("a * (b - (c * d))", lambda: a * (b - (c * d))),
        ("a * (b - (c / d))", lambda: a * (b - (c / d))),
        ("a * (b * (c + d))", lambda: a * (b * (c + d))),
        ("a * (b * (c - d))", lambda: a * (b * (c - d))),
        ("a * (b * (c * d))", lambda: a * (b * (c * d))),
        ("a * (b * (c / d))", lambda: a * (b * (c / d))),
        ("a * (b / (c + d))", lambda: a * (b / (c + d))),
        ("a * (b / (c - d))", lambda: a * (b / (c - d))),
        ("a * (b / (c * d))", lambda: a * (b / (c * d))),
        ("a * (b / (c / d))", lambda: a * (b / (c / d))),
        ("a / (b + (c + d))", lambda: a / (b + (c + d))),
        ("a / (b + (c - d))", lambda: a / (b + (c - d))),
        ("a / (b + (c * d))", lambda: a / (b + (c * d))),
        ("a / (b + (c / d))", lambda: a / (b + (c / d))),
        ("a / (b - (c + d))", lambda: a / (b - (c + d))),
        ("a / (b - (c - d))", lambda: a / (b - (c - d))),
        ("a / (b - (c * d))", lambda: a / (b - (c * d))),
        ("a / (b - (c / d))", lambda: a / (b - (c / d))),
        ("a / (b * (c + d))", lambda: a / (b * (c + d))),
        ("a / (b * (c - d))", lambda: a / (b * (c - d))),
        ("a / (b * (c * d))", lambda: a / (b * (c * d))),
        ("a / (b * (c / d))", lambda: a / (b * (c / d))),
        ("a / (b / (c + d))", lambda: a / (b / (c + d))),
        ("a / (b / (c - d))", lambda: a / (b / (c - d))),
        ("a / (b / (c * d))", lambda: a / (b / (c * d))),
        ("a / (b / (c / d))", lambda: a / (b / (c / d))),
    ]

    for expr, fn in expressions:
        try:
            result = fn()
            if result not in results:
                results.add(
                    round(result, 8)
                )  # Round to handle floating-point precision issues
        except ZeroDivisionError:
            continue

    return results


def get_weight(a, b, c, d):
    counts = Counter([a, b, c, d])
    return prod(prod(range(4, 4 - count, -1)) for count in counts.values())


def generate_distribution():
    distribution = defaultdict(int)
    total_iterations = 13**4
    factorial_cache = {i: factorial(i) for i in range(5)}

    with tqdm(total=total_iterations, ncols=100) as pbar:
        for combination in product(range(1, 14), repeat=4):
            unique_results = set()
            for perm in permutations(combination):
                unique_results.update(evaluate_all_expressions(*perm))
            weight = get_weight(*combination)
            for result in unique_results:
                distribution[result] += weight
            pbar.update(1)

    return distribution


if __name__ == "__main__":
    distribution = generate_distribution()
    KEEP_PRINTING = True
    for k, v in sorted(distribution.items(), key=lambda x: x[1], reverse=True):
        if KEEP_PRINTING:
            print(f"{k}: {v}")
        if abs(k - 5.5) < 0.01:
            KEEP_PRINTING = False

# 2: 6358392
# -2: 6168096
# 3: 6118104
# 0.5: 6090624
# 4: 6031368
# -3: 5966592
# 6: 5899680
# -4: 5892288
# 5: 5817384
# -0.5: 5815464
# 1: 5796600
# -1: 5785080
# -6: 5761944
# 7: 5732808
# 9: 5711040
# -5: 5706720
# 8: 5699136
# 10: 5669760
# 12: 5669760
# 1.5: 5648040
# 14: 5595816
# -8: 5580408
# -7: 5569440
# 15: 5557680
# -9: 5549112
# 11: 5506344
# 16: 5459976
# -10: 5421312
# -12: 5417760
# 0.66666667: 5390832
# 18: 5389488
# 0.33333333: 5374008
# 0.25: 5339328
# 0: 5299320
# 13: 5279256
# 20: 5265768
# -11: 5229408
# 24: 5227608
# -1.5: 5225904
# -14: 5194872
# 2.5: 5166408
# -15: 5074560
# -0.33333333: 4992312
# -0.66666667: 4979256
# -0.25: 4959960
# 36: 4951200
# -18: 4947120
# 3.5: 4923912
# 21: 4917096
# 22: 4905816
# -16: 4905456
# -13: 4886640
# 17: 4876680
# 1.33333333: 4844208
# -20: 4806480
# 28: 4761744
# -24: 4757856
# 5.5: 4732200
