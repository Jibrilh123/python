class Cars:

    model = "Car"

    def __init__(self, name, year):
        self.name = name
        self.year = year

        
Audi = Cars("AudiR8", 2025)
BMW = Cars("BWMM5", 2020)

print("Audi is a {}".format(Audi.model))
print("BMW is also a {}".format(BMW.model))

print("{} is a {}  model  ".format( Audi.name, Audi.year))
print("{} is  a{} model".format( BMW.name, BMW.year))
    