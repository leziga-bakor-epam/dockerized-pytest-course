from scripts.chp2.video4.mapmaker_challenge import Point

import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Senegal", 99.6937, -189.44406)
    assert str(exp.value) == "Invalid latitude, longitude combination."

    with pytest.raises(TypeError) as exp:
        Point(5, 12.11386, -55.08269)
    assert str(exp.value) == "Invalid name. City name must be of type string"

    """
    Your solution here! You will need to edit the following source code
    file to get your test running:

        File path:
        scripts/chp2/video4/mapmaker_challenge import

    It has already been imported for you on the first line of this file
    """
