#!/usr/bin/python3
"""
Module to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    A function that multiplies 2 matrices manually.

    Args:
        m_a : Argument
        m_b : Argument

    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for element in m_a:
        if type(element) is not list:
            raise TypeError("m_a must be a list of lists")
    for element in m_b:
        if type(element) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    length = len(m_a[0])
    for row in m_a:
        if len(row) != length:
            raise TypeError("each row of m_a must be of the same size")
    length = len(m_b[0])
    for row in m_b:
        if len(row) != length:
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = []
    for row in m_a:
        new_row = []
        for column in zip(*m_b):
            adds = 0
            for i in range(len(row)):
                adds += row[i] * column[i]
            new_row.append(adds)
        new_m.append(new_row)
    return new_m
