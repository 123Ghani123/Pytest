import pytest
from src.area import compute_median_mean_diff

def test_compute_median_mean_diff():
    ages = [19, 22, 34, 26, 32, 30, 24, 24]
    ages2 = [181, 187, 196, 196, 198, 203, 207, 211, 215]
    assert compute_median_mean_diff(ages) == 1.38
    assert compute_median_mean_diff(ages2) == 1.33

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        compute_median_mean_diff(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        compute_median_mean_diff("2")

def test_calculate_area_square_positive():
    with pytest.raises(TypeError):
        compute_median_mean_diff(2)
        