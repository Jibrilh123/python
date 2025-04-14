class Bike:

    def __init__(self, max_speed, mileage):

        self.max_speed = max_speed
        self.mileage = mileage


ModelY = Bike(300,50)

print("Model Max Speed:", ModelY.max_speed)
print("Model Mileage:", ModelY.mileage)
    