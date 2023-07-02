#!/usr/bin/python3
"""
Module to multiply 2 matrices the lazy way
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices by using the module NumPy
    (the lazy way)

    Args:
        m_a : Argument
        m_b : Argument

    """
    return np.matmul(m_a, m_b)
