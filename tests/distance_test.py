from mlproject.distance import haversine

def test_type_distance():
    res = haversine(48.865070, 2.380009, -34.59972, -58.38194)
    assert type(res) == type(32.3)

def accuracy():
    res = haversine(48.865070, 2.380009, -34.59972, -58.38194)
    assert round(res) == 11051