import pytest
from house_painting_quote import painting_quote, paint_litres, crew_days


def test_painting_quote_branches():
    assert painting_quote("emulsion", 100, 1, False) == 5000
    assert painting_quote("enamel", 2500, 1, False) == 67500
    assert painting_quote("enamel", 500, 2, True) == 32500


def test_painting_quote_errors():
    with pytest.raises(ValueError):
        painting_quote("unknown", 100, 1, False)
    with pytest.raises(ValueError):
        painting_quote("emulsion", 0, 1, False)
    with pytest.raises(ValueError):
        painting_quote("emulsion", 100, 0, False)
    with pytest.raises(ValueError):
        painting_quote("distemper", 100, 1, True)


def test_paint_litres_branches():
    assert paint_litres(200, 1, "smooth") == 2
    assert paint_litres(120, 1, "rough") == 2
    assert paint_litres(101, 1, "smooth") == 2


def test_paint_litres_error():
    with pytest.raises(ValueError):
        paint_litres(100, 1, "unknown")


def test_crew_days_branches():
    assert crew_days(800, 2, False) == 1
    assert crew_days(900, 2, False) == 2
    assert crew_days(800, 2, True) == 3


def test_crew_days_error():
    with pytest.raises(ValueError):
        crew_days(800, 0, False)