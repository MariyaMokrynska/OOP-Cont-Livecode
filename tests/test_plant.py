from classes.plant import Plant


def test_plant_class_instatiation():
    # Arrange
    name = "Orchid"
    water_level = 5
    sunlight_hours = 3
    is_blooming = True
    # Act
    plant = Plant(
        name,
        water_level,
        sunlight_hours,
        is_blooming
    )

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == is_blooming


def test_plant_class_instatiation_default_is_blooming():
    # Arrange
    name = "Orchid"
    water_level = 5
    sunlight_hours = 3
    # Act
    plant = Plant(
        name,
        water_level,
        sunlight_hours
    )

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == False


def test_change_water_increases_water_level():
    # Arrange
    name = "Oxalis"
    original_water_level = 2
    sunlight_hours = 7
    is_blooming = True

    plant = Plant(
        name,
        original_water_level,
        sunlight_hours,
        is_blooming
    )
    add_water = 3
    # Act
    new_water_level = plant.change_water(add_water)

    # Assert
    # attribute
    assert plant.water_level == 5
    # return value
    assert new_water_level == 5

    # not coz don't know if == 5, can both get updated incorrectly
    # asser plant.water_level == new_water_level


def test_check_growth_water_sunlight_over_five():
    # Arrange
    name = "Purple Trumpet"
    water_level = 6
    sunlight_hours = 6
    is_blooming = False

    plant = Plant(
        name,
        water_level,
        sunlight_hours,
        is_blooming
    )

    # Act
    plant_growth_stage = plant.check_growth()

    # Assert
    assert plant_growth_stage == "Purple Trumpet's growth stage: Mature"
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert not plant.is_blooming
