"""
A project to demonstrate a possible IPython bug.
"""


def afunction(arg1, arg2):
    """
    :param arg1: Argument 1
    :param arg2: Argument 2
    :return: None

    Here is an ipython directive with savefig.

    .. ipython:: python

        import numpy as np
        import matplotlib.pyplot as plt

        x = np.random.randn(100)
        y = x

        @savefig saved_figure.png
        plt.plot(x, y, 'o')
    """

    pass
