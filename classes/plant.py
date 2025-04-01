class Plant:
    def __init__(self, name, water_level, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming

    def change_water(self, water):
        self.water_level += water

        return self.water_level

    def change_sunlight(self, light):
        self.sunlight_hours += light

        return self.sunlight_hours

    def check_growth(self):
        growth_stage = "Sprout"
        sunlight_water_over_five = self.sunlight_hours + self.water_level >= 12

        if self.is_blooming or sunlight_water_over_five:
            growth_stage = "Mature"

        return f"{self.name}'s growth stage: {growth_stage}"
