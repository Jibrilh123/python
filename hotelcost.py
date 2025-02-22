    def hotel_cost(nights):
        return 150*nights

    def plane_ride_cost(city):
        if "Los santos" == city:
            return 200
        elif "SanAndreas" == city:
            return 350
        elif " Los Angeles" == city:
            return 500
        
    def rental_car_cost(days):
        if days>=7:
            return 50*days - 50
        elif days>=3:
            return 50*days - 20
        else:
            return 40*days
        
    def trip_cost(city, days, spending_money):
        return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

    print(f"cost of car rental: {rental_car_cost(6)}, plane cost is {plane_ride_cost("SanAndreas")}, and the hotel cost is {hotel_cost(6)}, the total cost of the trip is {trip_cost("SanAndreas",6,1000)}")
    print(trip_cost("Los Angeles", 5,500))
        