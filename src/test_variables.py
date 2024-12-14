def test_variables():
    """Test variables"""

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4 # type int
    variable_with_changed_type = 'Sally' # is now of type str

    assert variable_with_changed_type == 'Sally'