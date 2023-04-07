#!/usr/bin/python3.5
"""
Module composed by a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Function that multiplies 2 matrices
    Args:
        m_a: 1st matrix 
        m_b: 2nd  matrix 
    Returns:
        result of the multiplication
    """

    return (np.matmul(m_a, m_b))
