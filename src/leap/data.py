"""A module for synthetic data that we use in test and examples."""

from leap import core, binary_problems
from leap import ops as op


def _build_test_pop():
    """Construct a synthetic population for illustrating example operations."""
    pop = [core.Individual([1, 0, 1, 1, 0], core.IdentityDecoder(), binary_problems.MaxOnes()),
           core.Individual([0, 0, 1, 0, 0], core.IdentityDecoder(), binary_problems.MaxOnes()),
           core.Individual([0, 1, 1, 1, 1], core.IdentityDecoder(), binary_problems.MaxOnes()),
           core.Individual([1, 0, 0, 0, 1], core.IdentityDecoder(), binary_problems.MaxOnes())]
    pop, _ = op.evaluate(iter(pop))

    # Assign distinct values to an attribute on each individual
    attrs = [('foo', ['GREEN', 15, 'BLUE', 72.81]),
             ('bar', ['Colorless', 'green', 'ideas', 'sleep']),
             ('baz', [['a', 'b', 'c'], [1, 2, 3], [None, None, None], [0.1, 0.2, 0.3]])]
    for attr, vals in attrs:
        for (ind, val) in zip(pop, vals):
            ind.attributes[attr] = val

    return pop


"""A synthetic population for illustrating example operations"""
test_population = _build_test_pop()
