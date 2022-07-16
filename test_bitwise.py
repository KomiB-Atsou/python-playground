"""Bitwise operators
@see: https://www.w3schools.com/python/python_operators.asp
Bitwise operators manipulate numbers on bit level.
"""

def test_bitwise_operators():
    """ Bitwise operators """

    """
        AND
        Sets each bit to 1 if both bits are 1.
        Example : 
        5 = 0b0101
        3 = 0b0011
    """

    assert 5 & 3 == 1 # 0b0001

    # OR
    # Sets each bit to 1 if one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    assert 5 | 3 == 7 # 0b0111