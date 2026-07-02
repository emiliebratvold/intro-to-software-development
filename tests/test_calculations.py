from geo_calculator.calculations import find_average

def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result

def test_find_average() -> None:
    test_list = [1, 2, 3, 4, 5]  # Arrange: set up the inputs
    average = find_average(test_list)  # Act: run the thing under test
    assert average == 3.0  # Assert: check the result

#kommentar fikset

#prover igjen
