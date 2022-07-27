"""Assignment operators
@see: https://www.w3schools.com/python/python_operators.asp
Assignment operators are used to assign values to variables
"""


def test_assignment_operator():
    """Assignment operator """

    # Assignment: =
    number = 5
    assert number == 5

    # Multiple assignment.
    # The variables first_variable and second_variable simultaneously get the new values 0 and 1.
    first_variable, second_variable = 0, 1
    assert first_variable == 0
    assert second_variable == 1

    # You may even switch variable values using multiple assignment.
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 1
    assert second_variable == 0