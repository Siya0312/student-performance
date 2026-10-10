import pytest

from src.student_performance import calculate_cgpa, get_performance


def test_calculate_cgpa():
    assert calculate_cgpa([9.0, 8.5, 8.0, 9.5], [4, 3, 3, 2]) == 8.71


def test_calculate_cgpa_with_equal_credits():
    assert calculate_cgpa([8.0, 10.0], [3, 3]) == 9.0


def test_empty_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([], [])


def test_mismatched_lengths():
    with pytest.raises(ValueError):
        calculate_cgpa([8.0, 9.0], [3])


def test_invalid_grade_point():
    with pytest.raises(ValueError):
        calculate_cgpa([11.0], [3])


def test_invalid_credit():
    with pytest.raises(ValueError):
        calculate_cgpa([8.0], [0])


def test_performance_categories():
    assert get_performance(9.2) == "Outstanding"
    assert get_performance(8.5) == "Excellent"
    assert get_performance(7.5) == "Good"
    assert get_performance(6.5) == "Satisfactory"
    assert get_performance(5.5) == "Needs Improvement"


def test_invalid_cgpa():
    with pytest.raises(ValueError):
        get_performance(11.0)
