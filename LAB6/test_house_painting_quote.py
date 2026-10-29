import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days

#Example test cases:
def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500

def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2

#Write the rest of the test cases so that the code is 90- 100% covered.
import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


# Painting quote tests
def test_exterior_enamel():
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_interior_emulsion():
    assert painting_quote("emulsion", 100, 1, False) == 5000


def test_unknown_paint():
    with pytest.raises(ValueError):
        painting_quote("unknown", 100, 1, False)


def test_invalid_area():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 1, False)


def test_invalid_coats():
    with pytest.raises(ValueError):
        painting_quote("emulsion", 100, 0, False)


def test_exterior_distemper():
    with pytest.raises(ValueError):
        painting_quote("distemper", 100, 1, True)


def test_large_area_discount():
    assert painting_quote("enamel", 2500, 1, False) == 67500


def test_minimum_cost():
    assert painting_quote("distemper", 100, 1, False) == 5000


# Paint litres tests
def test_smooth_litres():
    assert paint_litres(200, 1, "smooth") == 2


def test_rough_litres():
    assert paint_litres(120, 1, "rough") == 2


def test_unknown_surface():
    with pytest.raises(ValueError):
        paint_litres(100, 1, "unknown")


def test_extra_litre():
    assert paint_litres(101, 1, "smooth") == 2


def test_exact_litres():
    assert paint_litres(200, 1, "smooth") == 2


# Crew days tests
def test_crew_days_exact():
    assert crew_days(800, 2, False) == 1


def test_crew_days_remainder():
    assert crew_days(900, 2, False) == 2


def test_wallpaper_removal():
    assert crew_days(800, 2, True) == 3


def test_no_painters():
    with pytest.raises(ValueError):
        crew_days(800, 0, False)
